## Transactions

The customer backend pushes all transactions (and transaction updates/deletes) to this endpoint.

Transactions are sent by account in a list. The request has a status that indicates if this is historical or real time transactions.

For accounts that don’t contain any transactions, an empty page should be sent.

When a transaction is updated on the customer side (normally that it changes state from being reserved to being booked) it is also sent here. This means that the record representing the booked transaction needs to have the same transaction id as the original entry.
