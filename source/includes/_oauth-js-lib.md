## Javascript Library: Link

```html
<script type="text/javascript" src="https://www.tink.se/link/0.2/tink-link-0.2.0-min.js"></script>
...
<body>
  <div id="tink-area"></div>
  ...

  <script>
    var container = document.getElementById('tink-area');

    tink.start(container, {
      product: tink.Product.AUTO_AUTHORIZE,
      clientId: '{YOUR_CLIENT_ID}',
      oauth: {
        redirectUri: 'https://www.example.com/redirect',
        scopes: [
          tink.Scope.ACCOUNTS_READ,
          tink.Scope.USER_READ
        ],
      },
      input: {
        providerName: {provider-name},
        username: 'yyyymmddnnnn'
      },
      success: function(type, token) {
        // The token of type 'code' together with your client's secret
        // will be exchangable for an access_token 
      }
    });
  </script>
</body>
```

For web developers we've done it easy. Just include the Javascript library tink-link on your site and start it up with your OAuth2 parameters. The library takes care of the rest. It's even possible to authorize non-tink users and get hold of their data. Without them having to sign up as a Tink user first.

A fully functional demo in production environment: [https://link-example.appspot.com/account-checker/](https://link-example.appspot.com/account-checker/)

Start up tink-link by giving a DOM element and the options parameter to the start method: `tink.start(element, options);`

