#!/usr/bin/env python3

import json
import argparse
from pprint import pprint

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--swagger", help="Swagger JSON file", required=True)
parser.add_argument("-t", "--template", help="The output markdown file", required=False)
parser.add_argument("-o", "--output", help="The output markdown file", required=True)

args = parser.parse_args()

def findDefintion(ref, definitions, type=None):
    for definition in definitions:
        if ref.endswith('/'+definition):
            return (definition, definitions[definition])

def findAllDefintions(ref, definitions, result, addSelf=False):
    definition = findDefintion(ref, definitions)
    if addSelf:
        result.append(definition)

    #find sub definitions
    if 'properties' in definition[1]:
        for prop in sorted(definition[1]['properties']):
            property = definition[1]['properties'][prop]
            if '$ref' in property and ref != property['$ref']:
                findAllDefintions(property['$ref'], definitions, result, True)
            elif 'items' in property and '$ref' in property['items'] and ref != property['items']['$ref']:
                findAllDefintions(property['items']['$ref'], definitions, result, True)


def findParametersOfType(parameterType, parameters): 
    params = []
    for p in parameters:
        if p['in'] == parameterType:
            params.append(p)

    return params

def parametersToTable(parameters):
    s =  'Parameter | Description | Required\n'
    s += '--------- | ----------- | --------\n'
    for param in parameters:
        s += param['name'] + ' | ' + (param['description'] if 'description' in param else '') + ' | ' + ('true' if 'required' in param else '') + '\n'
    return s

def exampleValue(type):
    return {
        'string': 'string',
        'double': 1.5,
        'number': 0,
        'integer': 0,
        'array': [],
        'boolean': False,
        'datetime': 1465032304000
    }.get(type, '') 

def exampleStringToValue(prop):

    type = prop['type']
    value = prop['example']
    format = None
    if ('format' in prop):
        format = prop['format']

    if type == 'double':
        return float(value)
    
    if type == 'number' or type == 'integer':
        try:
            return int(value)
        except:
            return float(value)


    if type == 'datetime': 
        return int(value)

    if type == 'boolean':
        return {
            'true': True,
            'True': True,
            'false': False,
            'False': False
        }.get(value)

    if type == 'string' and format == 'date-time':
        return int(value)
        
    if type == 'string' and value == 'null':
        return None

    return value

def ordinaryPropertyToType(prop):
    if 'format' in prop and prop['format'] == 'date-time':
        return 'number'
    else:
        return prop['type']

def ordinaryPropertyToValue(prop):
    if 'example' in prop:
        return exampleStringToValue(prop)
    else:
        return exampleValue(prop['type'])

def splitIntoArray(str):
    if str.startswith('['):
        return str[1:-1].split(',')
    return str.split(',')


def modelToJsonExampleDict(d, name, model, definitions):

    for prop in model['properties']:

        if 'type' in model['properties'][prop] and model['properties'][prop]['type'] == 'array':
            if '$ref' in model['properties'][prop]['items']:
                (bodyName,bodyModel) = findDefintion(model['properties'][prop]['items']['$ref'], definitions)
                if bodyName != name:
                    d[prop] = [ modelToJsonExampleDict({}, bodyName, bodyModel, definitions) ]
            elif 'example' in model['properties'][prop]:
                try:
                    d[prop] = json.loads(model['properties'][prop]['example'])
                except:
                    d[prop] = [exampleValue(model['properties'][prop]['items']['type']), exampleValue(model['properties'][prop]['items']['type'])]

            elif 'type' in model['properties'][prop]['items']:
                d[prop] = [exampleValue(model['properties'][prop]['items']['type']), exampleValue(model['properties'][prop]['items']['type'])]
            else:
                d[prop] = []
        elif '$ref' not in model['properties'][prop]:
            d[prop] = ordinaryPropertyToValue(model['properties'][prop])
        elif '$ref' in model['properties'][prop]:
            (bodyName,bodyModel) = findDefintion(model['properties'][prop]['$ref'], definitions)
            d[prop] = modelToJsonExampleDict({}, bodyName, bodyModel, definitions)

    return d



class ModelConverter:
    def __init__(self, definitions):
        self.definitions = definitions

    def toExampleJson(self, title, name, model, type = 'object'):
        d = modelToJsonExampleDict({}, name, model, self.definitions)

        jsonObj = [];
        if type == 'array':
            jsonObj.append(d)
        else:
            jsonObj = d

        s = '> ' + title +'\n\n'
        s += '```json\n'
        s += json.dumps(jsonObj, sort_keys=True, indent=2) + '\n'
        s += '```\n'
        
        return s

    def toTable(self, model):

        s =  'Parameter | Type | Required | Description\n'
        s += '--------- | ---- | -------- | -----------\n'
        for prop in sorted(model['properties']):

            # building up the type
            t = ''
            if 'type' in model['properties'][prop]:
                # string,double,array,...
                t = ordinaryPropertyToType(model['properties'][prop])

            if 'items' in model['properties'][prop] and 'type' in model['properties'][prop]['items'] and len(t) > 0:
                # array[string|double|...]
                t += '[' + model['properties'][prop]['items']['type'] + ']'
            elif 'items' in model['properties'][prop] and '$ref' in model['properties'][prop]['items'] and len(t) > 0:
                # array[class]
                (name,m) = findDefintion(model['properties'][prop]['items']['$ref'], self.definitions)
                t += '[' + name + ']'
            elif '$ref' in model['properties'][prop]:
                # only class
                (name,m) = findDefintion(model['properties'][prop]['$ref'], self.definitions)
                t += name

            req = ''
            if 'required' in model and prop in model['required'] :
                req = 'true'

            d = ''
            if 'description' in model['properties'][prop]:
                d = model['properties'][prop]['description']
                if 'enum' in model['properties'][prop]:
                    d += '. Values: '
                    i = 0
                    for e in model['properties'][prop]['enum']:
                        d += '<code style="white-space: nowrap;">'+e+'</code>'
                        i += 1
                        if i < len(model['properties'][prop]['enum']):
                            d += ', '

            s += prop + ' | ' + t + ' | ' + req + ' | ' + d + '\n'

        return s

class TagConverter:
    def __init__(self, operations, definitions):
        self.operations = operations
        self.definitions = definitions;

    def convert(self, tag):
        s = '# ' + tag['name'] + '\n\n'
        if 'description' in tag:
            s += tag['description'] + '\n\n'

        paths = []
        for path in sorted(self.operations):
            def find(path):
                for method in sorted(self.operations[path]):
                    if tag['name'] in self.operations[path][method]['tags']:
                        paths.append(path)
                        return
            find(path)

        for path in paths:
            oc = OperationConverter(path, self.operations[path], self.definitions)
            s += oc.convert()

        return s


class OperationConverter:
    def __init__(self, path, operation, definitions):
        self.path = path
        self.operation = operation
        self.definitions = definitions

    def convert(self):

        s = ''
        for method in sorted(self.operation):
            s += '## ' + self.operation[method]['summary'] + '\n\n'
            if 'description' in self.operation[method]:
                s += self.operation[method]['description'] + '\n\n'

            s += '`'+method.upper()+' '+self.path+'`' + '\n\n'

            modelConverter = ModelConverter(self.definitions)

            response = None
            responseRef = None
            responseType = None

            requestBody = None
            requestBodyRef = None

            queryParam = []
            pathParam = []
            headerParam = []

            if 'responses' in self.operation[method]:
                responses = self.operation[method]['responses']
                if '200' in responses:
                    if 'schema' in responses['200']:
                        if '$ref' in responses['200']['schema']:
                            responseRef = responses['200']['schema']['$ref']
                            response = findDefintion(responseRef, self.definitions)
                            responseType = 'object'
                        elif '$ref' in responses['200']['schema']['items']:
                            responseRef = responses['200']['schema']['items']['$ref']
                            response = findDefintion(responseRef, self.definitions)
                            responseType = responses['200']['schema']['type']

            if 'parameters' in self.operation[method]:
                queryParam = findParametersOfType('query', self.operation[method]['parameters'])
                pathParam = findParametersOfType('path', self.operation[method]['parameters'])
                headerParam = findParametersOfType('header', self.operation[method]['parameters'])

                body = findParametersOfType('body', self.operation[method]['parameters'])
                if len(body) > 0:
                    requestBody = body[0]

                    if '$ref' in requestBody['schema']:
                        requestBodyRef = requestBody['schema']['$ref']
                        (bodyName,bodyModel) = findDefintion(requestBodyRef, self.definitions)
                    else:
                        requestBodyRef = requestBody['schema']['items']['$ref']
                        (bodyName,bodyModel) = findDefintion(requestBodyRef, self.definitions)




            # Right pane: Request example
            if requestBody is not None:
                s += modelConverter.toExampleJson('Request Example', bodyName, bodyModel) + '\n\n'

            # Center pane: Path Parameters
            if len(pathParam) > 0 :
                s += '### Parameters' + '\n\n'
                s += parametersToTable(pathParam) + '\n\n'

            # Center pane: Query Parameters
            if len(headerParam) > 0:
                s += '### Header Parameters' + '\n\n'
                s += parametersToTable(headerParam) + '\n\n'

            # Center pane: Query Parameters
            if len(queryParam) > 0:
                s += '### Query Parameters' + '\n\n'
                s += parametersToTable(queryParam) + '\n\n'

            # Center pane: Request Body
            if requestBody is not None:
                s += '### Body: ' + bodyName + '\n\n'
                s += requestBody['description'] + '\n\n'
                s += modelConverter.toTable(bodyModel) + '\n\n'

                #Sub models
                result = []
                findAllDefintions(requestBodyRef, self.definitions, result)
                for subType in result:
                    s += '#### ' + subType[0] + '\n\n'
                    s += modelConverter.toTable(subType[1]) + '\n\n'


            # Right pane: Response example
            if response is not None:
                s += modelConverter.toExampleJson('Response Example', response[0], response[1], responseType) + '\n\n'

            # Center pane: Response Body
            if response is not None:
                if responseType == 'array':
                    s += '### Response: ' + responseType + '[' + response[0] + ']' + '\n\n'
                else :
                    s += '### Response: ' + response[0] + '\n\n'
                s += modelConverter.toTable(response[1]) + '\n\n'

                #Sub models
                result = []
                findAllDefintions(responseRef, self.definitions, result)
                for subType in result:
                    s += '#### ' + subType[0] + '\n\n'
                    s += modelConverter.toTable(subType[1]) + '\n\n'

        return s





with open(args.swagger) as swagger:   
    data = json.load(swagger)

tc = TagConverter(data['paths'], data['definitions'])

s = ''
for tag in data['tags']:
    s += tc.convert(tag)

f = open(args.output, 'w')

if args.template is not None:
    t = open(args.template, 'r')
    template = t.read()
    s = template + s
    t.close()

f.write(s)
f.close()

