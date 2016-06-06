#!/bin/sh

CURRENT_PATH=`pwd`

source config.sh

SERVE=false
if [ $# -gt 0 ] && [ $1 = "serve" ]; then
	SERVE=true
fi

MODULE=main-api
TEMPLATE=source/index.html.md.main-api.template
if [ $# -eq 1 ] && [ $1 != "serve" ]; then
	MODULE=$1
elif [ $# -eq 2 ]; then
	MODULE=$2
	TEMPLATE=source/index.html.md.$2.template
fi

echo "\ncd $TINK_BACKEND"
cd $TINK_BACKEND
echo "\nmvn -pl src/main-api,src/connector-api compile -DskipTests=true"
mvn -pl src/main-api,src/connector-api compile -DskipTests=true

echo "\ncp src/$MODULE/target/generated/swagger/swagger.json $CURRENT_PATH/"
cp src/$MODULE/target/generated/swagger/swagger.json $CURRENT_PATH/

echo "\ncd $CURRENT_PATH"
cd $CURRENT_PATH

echo "\n./swagger2markdown.py -s swagger.json -o source/index.html.md -t $TEMPLATE"
./swagger2markdown.py -s swagger.json -o source/index.html.md -t $TEMPLATE

if [ $SERVE ]; then
    echo "\nbundle exec middleman server"
	bundle exec middleman server
else
	echo "\nbundle exec middleman build --clean"
	bundle exec middleman build --clean
fi

