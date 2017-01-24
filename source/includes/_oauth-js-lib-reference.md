## Javascript Library: Link Reference

### The `tink` object

The tink object has a bunch of constants for easy use (you can easily see them with `console.log('tink', tink);`). Other than that the method of interest on the tink object is `start`.

### `start(container, options)`
Parameter | Description
--------- | -----------
container | The DOM object in-which tink-link will create the iframe.
options | An object with options to tink-link. Described in detail below.

### Options

```json
{
  "product": "auto_authorize",
  "clientId": "38c299bde2bd4127b56ed12a5dc6c3a3",
  "oauth": {
    "redirectUri": "https://www.example.com/redirect",
    "scopes": [
      "accounts:read",
      "user:read"
    ]
  },
  "input": {
    "providerName": "handelsbanken-bankid",
    "username": "yyyymmddnnnn"
  },
  "locale": "sv_SE",
  "origin": "ios-app",
  "openBankIdButton": "show",
  "success": function(type, token) {},
  "error": function(status, message, data) {}
}
```

Parameter | Description
----- | -----------
product | The kind of product of tink-link. Currently only 'auto_authorize' and 'sign_transfer' is possible.
clientId | Your client id string provided by tink.
oauth | Object with the `redirectUri` string and `scopes` array of strings parameters.
input | Object with the `providerName` and `username` string parameters. Username is the 12-digit SSN.
locale | String parameter to define the locale, currently supports `sv_SE` and `en_US`. Defaults to `sv_SE`.
origin | String parameter for client to define the origin of this request (e.g. 'ios-app', 'web-main', etc.).
openBankIdButton | Can be set to `show`, `hide` or `auto-open` in order to control the Open BankID link of the potential BankID prompt.
success | Callback function that will be called on successful authorization or signing.
error | Callback function that will be called on any failed authorization or signing.

##### Success Callback

Parameter | Description
--------- | -----------
type | The type of the object. In the authorization case, it will be 'code'. 
obj | Depends on the type, will be a simple string in the 'code' case (`6915ab99857fec1e6f2f6c078`).

##### Error Callback

Parameter | Description
--------- | -----------
status | An enumerable defined below in Error Statuses
message | A message for developers describing the error somewhat. 
data | An object with string parameter `type` and object `obj`.

##### Error Statuses

Status | Description
------ | -----------
BAD_REQUEST | When link or OAuth2Client was initiated/configured badly
SERVICE_UNAVAILABLE | When Tink is completely unavailable
TEMPORARY_ERROR | Unexpected error
TEMPORARY_DISABLED | The chosen provider in temporarily disabled. Probably due to the provider being down.
AUTHENTICATION_ERROR | When an error occured due to authentication of the end-user. Can either be temporary or triggered by user (i.e. cancelling authentication). Further information will be given by the `status` and `statusPayload` of the `Credentials` object found in the `data` parameter.
SIGN_ERROR | When an error occured when signing a SignableOperation. Can either be temporary or triggered by user (i.e. cancelling signing). Further information will be given by the `status` and `statusMessage` of the `SignableOperation` object found in the `data` parameter.
UNAUTHORIZED | When starting with product `sign-transfer` but session from authentication is lost.
SAFARI_PRIVATE_MODE | Same as UNAUTHORIZED, but will always happen when running Safari in private mode.
