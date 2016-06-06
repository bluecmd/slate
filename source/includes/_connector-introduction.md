## Introduction

This document gives an overview of the layout and specification of the Connector located in the Tink cluster to get data from customers core systems.

The connector domain model consists of basically three levels:

<code>User</code>
The top domain object, holding information about the authenticated user.

<code>Account</code>
A user can have one or several accounts. An account could be a savings account, checking account, credit card, mortgage or car loan. An account holds information like: balance, name and number.

<code>Transaction</code>
An account can have one or several transactions. A transaction holds information like: amount, date and description.
