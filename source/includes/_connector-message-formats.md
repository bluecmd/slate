## Message formats
The Tink API is designed around REST at its core, and uses standard HTTP verbs and status codes to communicate requests and response statuses. For the JSON formatted data, properties use camel-case and enum-like string properties have capitalized property values.

String properties are encoded using UTF-8, and date properties are represented by ISO-8601 format, but without the colon in the time zone specification (i.e. +0100 instead of +01:00) is preferred."
