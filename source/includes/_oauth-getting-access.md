## Getting access

> GET /oauth/manager/client

```json
{
  "clients" : [ {
    "name" : "Account Checker",
    "id" : "...",
    "redirectUris" : [ "urn:ietf:wg:oauth:2.0:oob", "http://localhost:8881/", "https://link-example.appspot.com/" ],
    "scope" : "accounts:read,user:read",
    "secret" : "...",
    "url" : "https://www.tink.se",
    "iconUrl" : "..."
  } ]
}
```

Before starting, a set of OAuth2 client credentials needs to be generated and distributed to the 3rd-party API consumer. The OAuth2 client credentials contains the scope privileged and the client secret that should be submitted to receive the access token. The client secret should be treated confidentially, while the client id can be bundled in publicly available apps. These credentials provides different levels of permissions, which determines what types of information that are shared with the 3rd-party API consumer. Requests for access to the API can be directed to hello@tink.se, with a short description of what you would like to build on top of it. Please also provide a Tink user (email), this user will get elevated access to be able to read and update the OAuth2 client credentials.

We have not yet built some fancy web interface where you can see and change your OAuth2 client credentials. However, we've made it possible to GET and PUT the OAuth2Client object on the API. Once your Tink user has got elevated access, it will be able to make GET and PUT requests towards: https://www.tink.se/api/v1/oauth/manager/client

