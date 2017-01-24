## Initiate an authorization

If using the tink-link Javascript library is not appropriate for any reason, you can let Tink users authorize access to their data using the standard OAuth2 redirect mechanism.

The first step to get authorization to access user data is to initiate an OAuth2 authorization process by redirecting the user to Tink, and construct the authorization URL with the correct parameters and scopes. The parameters for the authorization redirect should include the following.

Parameter | Description
--------- | -----------
client_id | The client ID you received from Tink, identifying the 3rd party API consumer
redirect_uri | The URI that the user should be redirected to upon successful authorization
scope | List of security scopes requested, must be a subset of the client's permitted scopes

These parameters should be URL encoded and added as query parameters to the authorizarion URI which the user is redirected to:

`http://www.tink.se/link/0.2/oauth/auto-authorize.html`

<!--When the user is redirected to Tink, she is first asked to authenticate herself using her regular Tink credentials. If the user has any applicable services enabled that required device pinning, an extra 2-factor authentication step can be present, requiring the user to authenticate once per device using Mobilt BankID.

Once authenticated, the user will be presented with a screen that asks her to confirm the authorization process. This view highlights the specific security scopes requested by the 3rd-party API consumer so that the user is in full control and aweness of what types of data is being shared.-->

If the user accepts the authorization, an authorization code is generated and the user is redirected to the redirect URI requested with the authorization code appended as an URL encoded query parameter.

`https://example.com/redirect?code=6915ab99857fec1e6f2f6c078`

If the user does not approve the authorization, the user is redirected to the same redirect URI, but without any authorization code query parameters.