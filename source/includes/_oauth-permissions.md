## Permissions

Access to user-data is controlled using so called OAuth2 security scopes or permissions. Each 3rd-party API consumer is provisioned using a set of permissions which control the maximum permitted data access for the consumer, and for each end-user authorization process, a subset of those permissions can be requested for the user to authorize.

This setup provides a way for 3rd-party services to selectively request the right set of permissions from the user depending on the use-case for the data. If a 3rd-party API consumer has access to a broad set of permissions, it's highly recommended to be prudent in which permissions you actually request from the end-user.


Scope | Description
--------- | ---- | -----------
`user:read` | Access to user profile data such as e-mail, date of birth, etc.
`accounts:read` | Access to all the user's account information, including balances.
`accounts:write` | Ability to modify the user's accounts, for example renaming or excluding an account.
`transaction:read` | Access to all the user's transactional data
`transaction:write` | Ability to modify the user's transactions, for example recategorizing transactions.
`statistics:read` | Access to all the user's statistics, can include filters on statistic.type.
`user:web_hooks` | Access to list and create WebHooks

Other non-public security scopes are available for specific partners.