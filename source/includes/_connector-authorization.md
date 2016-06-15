## Authorization

Communication to the ingest endpoints requires a authorization token to be sent in the HTTP header. Certificate pinning is advised, to validate the authenticity of the target host.

The authorization token is submitted according to the standard authorization scheme (in the <code>Authorization</code> field) with token as authorization mechanism.

The token is supplied by Tink, and may be regularly updated. When updated, there will be a grace period during which several tokens are enabled simultaneously to guarantee a seamless transition to the new token.
<code>Authorization: Token 88eb60f24418495ab0a172b89e631fa6</code>
