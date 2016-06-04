# Message formats

The Tink API is designed around REST at its core, and uses standard HTTP verbs and status codes to communicate requests and response statuses. For the JSON encoded data, properties use camel-case and enum-like string properties have capitalized property values.

String properties are encoded using UTF-8, and date long properties are represented by UNIX-timestamps.
