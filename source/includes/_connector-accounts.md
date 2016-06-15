## Accounts

The accounts endpoint enables the customer to create, update and delete accounts.

By sending a user token for an activated user, together with a list of account entries, these will be created accordingly (depending on whether they already exist or not).

Before sending transactions to Tink, the customer’s account needs to be created. When enrolling a new customer, all accounts for the customer should be sent in one batch. A successful call to create accounts means that Tink is ready to receive transactions.

**Please note:** The customer’s accounts must not be subscribed for real-time transactions on the customer side before a successful response has been received from a call to this endpoint with the corresponding account.
