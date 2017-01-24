## Access user data

```bash
$ curl -X POST 'https://www.tink.se/api/v1/accounts' \
         -H 'Accept: application/json' \
         -H 'Authorization: Bearer d84ed046f09e4a06b4cc576e74b7172c'
```

Once you have a valid access token, you can use that to access user data using the Tink API. The access token is used as a bearer token in the HTTP Authentication header and more information about how the Tink API works can be found in the API-reference section.
