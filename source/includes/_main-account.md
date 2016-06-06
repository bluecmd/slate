## Account
  
When a <code>credentials</code> connection is successfully established, all supported accounts from the financial institution are aggregated and made available in the Tink API. An <code>account</code> can represent everything from the user's regular checking account to an investment account with their broker, or their home mortgage as a credit acccount.

Tink does what it can to try to determine the real type of account, but always defaults to marking the account as a regular <code>CHECKING</code>-account if we can't figure it out.

The <code>ownership</code> property adheres from the case where a user has selected that she's sharing the account with someone else. The effect of the ratio is that both the balance of the account, as well as any transactions stemming from the account, are only partly contributing towards the user's spending and total net-worth when the aggregated <code>statistics</code> are calculated.

The <code>balance</code> property of an account tries to provide a unified concept of balance across the different account types, which the intention to represent the user's current standing with the financial institution, and not the disposable amount. As an example, on a <code>CHECKING</code> account, the balance represent the actual amount of cash in the account. In the case of a <code>CREDIT_CARD</code> account, the balance is the outstanding balance on the account, and does not include any available credit or purchasing power the user has with the credit provider.
    
Also worth mentioning, the <code>balance</code> property represents the current balance of the account when the <code>credentials</code> was last updated successfully. Historical account balance information is available through the statistics interface, with a type of <code>balances-by-account</code> and the <code>id</code> of the account as the <code>description</code> of the statistics objects.
