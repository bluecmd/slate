## Web Hooks

```
+-----------------+   +-----------+                         +-------+
|    Consumer     |   | Consumer  |                         | Tink  |
| WebHookService  |   |           |                         |       |
+-----------------+   +-----------+                         +-------+
         |                  |                                   |
         |                  | POST /hooks (body: OAuth2Webhook) |
         |                  |---------------------------------->|
         |                  |                                   |
         |                  |                                   |
         |                  |                                   |
         |                  | POST /transfer (body: Transfer)   |
         |                  |---------------------------------->+
         |                  |                                  / \
         |                  |  Newly created SignableOperation \ /
         |                  |<----------------------------------+
         |                  |                                   |
         |                  |                                   |
         |                  |                                   | +---------------------+
         |                  |                                   |-| User signs transfer |
         |                  |                                   | +---------------------+
         |                  |                                   |
         |                  |                                   |
         |            POST {webhook-url} (body: WebHookRequest) |
         |<-----------------------------------------------------|
```

If you want updates to certain events pushed back to your servers that can be acheived using web hooks. The consumer client will need a special OAuth2 Client scope for creating web hooks for the end user. The web hook flow can be seen in the sequence diagram here on the right. The request made back to the consumer's web hook service (the given URL) will be a POST request with a `WebHookRequest` object as the body.

> POST /hooks body: OAuth2Webhook

```json
{
    "secret": "{SOME_USER_SPECIFIC_SECRET}",
    "url": "https://www.consumer.com/webhook-receiver/",
    "events": [
        "signable-operation:update"
    ]
}
```

### Request body: WebHookRequest

Parameter | Type | Description
--------- | ---- | -----------
event | String | The triggered event.
content | Object | The content depends on the event. For instance, for a Signable operation event the content object will be a SignableOperation.
webHook | OAuth2WebHook | The web hook that was created by the consumer. This objects contains the secret for the consumer to compare. See Web Hook Service for more information.

> POST {webhook-url}: WebHookRequest

```json
{
    "event": "signable-operation:update",
    "content": {
        "created": 1471349422000,
        "credentialsId": "342220f1e0484c0481b2b468d7fbcfc4",
        "id": "a4516bda6ff545e0aa24e54b859579e0",
        "status": "EXECUTED",
        "statusMessage": "The transfer has been sent to your bank.",
        "type": "TRANSFER",
        "underlyingId": "1e09bab571d84b1cbe8d49c0be9c030f",
        "updated": 1471349422000,
        "userId": "2f37e3ff1e5342b39c41bee3ee73cf8e"
    },
    "webHook": {
        "secret": "{SOME_USER_SPECIFIC_SECRET}",
        "url": "https://www.consumer.com/webhook-receiver/",
        "events": [
            "signable-operation:update"
        ]
    }
}
```

### Restrictions
The service receiving the web hooks must be served over `https`, and the Tink client will not follow redirects. Furthermore, the domain of the URL needs to be preset in Tink's backend. It is not possible to automatically set this domain so the consumer needs to contact their Tink contact for this to be set. A consumer can have multiple "authorized" domains preset. These restrictions are done for security reasons.

### Events
Event name | Description
---------- | ----------- 
signable-operation:update | This event is fired upon an update of the SignableOperation.