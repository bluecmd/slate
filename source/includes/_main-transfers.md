## Transfers

The Tink API makes it possible to make transfers. Tink has defined a transfer as moving money from one account to any destination, no matter if the destination is another bank account or a PG/BG-recipient. 

When making a transfer, the client sends in an object, a <code>Transfer</code>, that defines from where, to where and how much that will be transferred. The source account must of course belong to the authenticated user. It's the destination that decides whether to make a bank transfer or a payment. For instance if the destination is a BG-recipient, then the transfer will become a payment, whereas if the destination is a swedish account number, the transfer will be become a bank transfer.

Source and Destination accounts or PG/BG-recipients are sent on a special URI format. 

### Example

Source type | Defined by | URI format | Example
-------------- | ------ | ---------- | --------
Bank Account   | 9999 - 123456789 | se://{clearingnumber}{accountnumber} | se://9999123456789
Tink <code>Account</code>   | a4692fae219d4f7892262f269a6002f6 | tink://{account#id} | tink://a4692fae219d4f7892262f269a6002f6

Destination type | Defined by | URI format | Example
-------------- | ------ | ---------- | --------
Bank Account   | 9999 - 123456789 | se://{clearingnumber}{accountnumber} | se://9999123456789
PG Recipient   | 90 2003-3 | se-pg://{pg-recipient} | se-pg://9020033
BG Recipient   | 902-0033 | se-bg://{bg-recipient} | se-bg://9020033

