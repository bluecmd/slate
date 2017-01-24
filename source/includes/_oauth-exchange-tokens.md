## Exchange access tokens

```bash
$ curl -X POST 'https://www.tink.se/api/v1/oauth/token' \
          -d 'code=6915ab99857fec1e6f2f6c078& \
              client_id=63e53e0cf75e4b9381a4b37962fc0c9a& \
              client_secret=4c3b94d6b14348d5ad8994a3a04e36c8& \
              redirect_uri=https://example.com/oauth/callback& \
              grant_type=authorization_code'
        {
          "access_token": "78b0525677c7414e8b202c48be57f3da",
          "token_type": "bearer",
          "expires_in": 7200,
          "refresh_token": "33f10ce3cb1941b8a274af53da03f361",
          "scope": "transactions:read,accounts:read"
        }
```


Once you have received the authorization code in the redirect URI, you can use that code to exchange it for an access code. This must be done using the client secret, which you received with your client id.

As hinted by the expiry time of the access token, access tokens can expire after a set amount of time and will then need to be refreshed by the 3rd-party API consumer for continued access. This is done with the refresh token in a standard OAuth2 fashion using the same endpoint as used when exchanging the authorization code for an access token. More detailed information about the refresh of access tokens can be found at Google.