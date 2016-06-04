---
title: Tink API Reference

language_tabs:
  - json: Examples

includes:
  - start-general
  - introduction
  - message-formats
  - versioning
  - periods
  - categories
  - user
  - account
  - transaction
  - statistics
  - activity
  - start-reference

search: true
---






# Account Service

An account could either be a debit account, a credit card, a loan or mortgage.

## List accounts

Returns an object with a list of the authenticated user's accounts.

`GET /accounts/list`

> Response Example

```json
{
  "accounts": [
    {
      "accountNumber": "1234-123456789",
      "balance": 34567.5,
      "credentialsId": "6e68cc6287704273984567b3300c5822",
      "excluded": false,
      "favored": false,
      "id": "a6bb87e57a8c4dd4874b241471a2b9e8",
      "name": "Privatkonto",
      "ownership": 0.5,
      "type": "string"
    }
  ]
}
```


### Response: AccountListResponse

Parameter | Type | Description
--------- | ---- | -----------
accounts | array[Account] | A list of accounts


## Update an Account

Updates certain user modifiable properties of an account. Please refer to the body schema to see which properties are modifiable by the user.

`PUT /accounts/{id}`

> Request Example

```json
{
  "accountNumber": "1234-123456789",
  "balance": 34567.5,
  "credentialsId": "6e68cc6287704273984567b3300c5822",
  "excluded": false,
  "favored": false,
  "id": "a6bb87e57a8c4dd4874b241471a2b9e8",
  "name": "Privatkonto",
  "ownership": 0.5,
  "type": "string"
}
```


### Parameters

Parameter | Description
--------- | -----------
id | The id of the account


### Body: Account

The updated account object

Parameter | Type | Description
--------- | ---- | -----------
accountNumber | string | The account number of the account.
balance | number | The current balance of the account.
credentialsId | string | The internal identifier of the credentials that the account belongs to.
excluded | boolean | Indicates if the user has excluded the account. This can be modified by the user.
favored | boolean | Indicates if the user has favored the account. This can be modified by the user.
id | string | The internal identifier of account.
name | string | The display name of the account. This can be modified by the user.
ownership | number | The ownership ratio indicating how much of the account is owned by the user. This is used to determine how much of transactions belonging to this account should be attributed to the user when statistics are calculated. This can be modified by the user.
type | string | The type of the account. This can be modified by the user.. Values: <code style="white-space: nowrap;">CHECKING</code>, <code style="white-space: nowrap;">SAVINGS</code>, <code style="white-space: nowrap;">INVESTMENT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">LOAN</code>


> Response Example

```json
{
  "accountNumber": "1234-123456789",
  "balance": 34567.5,
  "credentialsId": "6e68cc6287704273984567b3300c5822",
  "excluded": false,
  "favored": false,
  "id": "a6bb87e57a8c4dd4874b241471a2b9e8",
  "name": "Privatkonto",
  "ownership": 0.5,
  "type": "string"
}
```


### Response: Account

Parameter | Type | Description
--------- | ---- | -----------
accountNumber | string | The account number of the account.
balance | number | The current balance of the account.
credentialsId | string | The internal identifier of the credentials that the account belongs to.
excluded | boolean | Indicates if the user has excluded the account. This can be modified by the user.
favored | boolean | Indicates if the user has favored the account. This can be modified by the user.
id | string | The internal identifier of account.
name | string | The display name of the account. This can be modified by the user.
ownership | number | The ownership ratio indicating how much of the account is owned by the user. This is used to determine how much of transactions belonging to this account should be attributed to the user when statistics are calculated. This can be modified by the user.
type | string | The type of the account. This can be modified by the user.. Values: <code style="white-space: nowrap;">CHECKING</code>, <code style="white-space: nowrap;">SAVINGS</code>, <code style="white-space: nowrap;">INVESTMENT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">LOAN</code>


# Activity Service

Activities are generated after statistics has been generated. The activities resides in a sorted list. Sort order is based on relevance.

## List activities

Returns all activities within the range of [offset, offset+limit].

`GET /activities`

### Query Parameters

Parameter | Description
--------- | -----------
offset | Offset in the sorted list of activities
limit | Number of activities to fetch


> Response Example

```json
{
  "content": "",
  "date": "1455740874875",
  "importance": 0,
  "key": "string",
  "message": "string",
  "title": "string",
  "type": "string"
}
```


### Response: Activity

Parameter | Type | Description
--------- | ---- | -----------
content | object | Serialized type dependent object.
date | string | Date of the activity.
importance | number | Importance compared to other activities 1-100 where 100 is of most importance.
key | string | Persistent key per type and content.
message | string | The activty message.
title | string | The activty title.
type | string | The activty type.


# Category Service

List of categories with parent/child relationships using their id and parent fields.

## List categories

Returns all categories

`GET /categories`

> Response Example

```json
{
  "code": "expenses:food.restaurants",
  "defaultChild": false,
  "id": "7e88d58188ee49749adca59e152324b6",
  "parent": "067fa4c769774ae980435c76be328c0b",
  "primaryName": "Food & Drinks",
  "searchTerms": "food,lunch,snacks",
  "secondaryName": "Restaurants",
  "sortOrder": "45",
  "type": "EXPENSES",
  "typeName": "Expenses"
}
```


### Response: Category

Parameter | Type | Description
--------- | ---- | -----------
code | string | Machine readable category code.
defaultChild | boolean | Indicates if this is the default child to be used when categorizing to a primary level category.
id | string | The internal identifier of the category, referenced by e.g. a transaction.
parent | string | The parent internal identifier of this category, or null.
primaryName | string | The primary name of this category.
searchTerms | string | Used by search engine to find transaction with this category.
secondaryName | string | The secondary name of this category.
sortOrder | integer | Sort order for nicer display for the user.
type | string | Type of the category.. Values: <code style="white-space: nowrap;">INCOME</code>, <code style="white-space: nowrap;">EXPENSES</code>, <code style="white-space: nowrap;">TRANSFERS</code>
typeName | string | Type name of the category.


# Device Service

This service handles Devices and their APN and GCM notification tokens.

## List all registered devices

Lists all registered devices.

`GET /devices`

> Response Example

```json
{
  "devices": [
    {
      "appId": "se.seb.privatkund",
      "deviceToken": "string",
      "notificationToken": "LRJ2bFzHA1jUIkwayDqxteNsWY3udejkEe9UwRMt12E_R5i...",
      "os": "ANDROID",
      "userAgent": "Tink Mobile/1.7.8 (Android; 4.4.2, LGE Nexus 4)"
    }
  ]
}
```


### Response: DeviceListResponse

Parameter | Type | Description
--------- | ---- | -----------
devices | array[Device] | 


## Deregister a device

Deregisters the device. Does not require an authenticated user.

`DELETE /devices/{deviceToken}`

### Parameters

Parameter | Description
--------- | -----------
deviceToken | The (persistent) deviceToken


## Register a device

Registers a device for the authenticated user. If the same notificationToken would exist on some another user, it will be removed from that user. If the deviceToken is registered already with a different push token, it will be updated to the latest one.

`PUT /devices/{deviceToken}`

> Request Example

```json
{
  "appId": "se.seb.privatkund",
  "deviceToken": "string",
  "notificationToken": "LRJ2bFzHA1jUIkwayDqxteNsWY3udejkEe9UwRMt12E_R5i...",
  "os": "ANDROID",
  "userAgent": "Tink Mobile/1.7.8 (Android; 4.4.2, LGE Nexus 4)"
}
```


### Parameters

Parameter | Description
--------- | -----------
deviceToken | The (persistent) deviceToken


### Body: Device

The token and some meta data around it

Parameter | Type | Description
--------- | ---- | -----------
appId | string | The app id of the app that registers the device
deviceToken | string | A device token, should be unique per device and app
notificationToken | string | The APN or GCM token
os | string | The operating system of the device. Values: <code style="white-space: nowrap;">ANDROID</code>, <code style="white-space: nowrap;">IOS</code>
userAgent | string | The User-Agent of the device


# Search Service

Service for searching and fetching transactions and their corresponding statistics.

## Query transactions

Returns a response containing transaction and their corresponding statistics matching the query.

`POST /search`

> Request Example

```json
{
  "endDate": "1455740874875",
  "includeUpcoming": false,
  "limit": "20",
  "offset": "20",
  "order": "ASC",
  "queryString": "Food this week",
  "sort": "DATE",
  "startDate": "1455740874875"
}
```


### Body: SearchQuery

The search query.

Parameter | Type | Description
--------- | ---- | -----------
endDate | string | The end date of the result.
includeUpcoming | boolean | Indicates if result should include upcoming transactions.
limit | integer | The limit for the result, used for paging.
offset | integer | The offset for the result, used for paging.
order | string | The order of the result.. Values: <code style="white-space: nowrap;">ASC</code>, <code style="white-space: nowrap;">DESC</code>
queryString | string | The string query.
sort | string | The sort order of the result.. Values: <code style="white-space: nowrap;">SCORE</code>, <code style="white-space: nowrap;">DATE</code>, <code style="white-space: nowrap;">ACCOUNT</code>, <code style="white-space: nowrap;">DESCRIPTION</code>, <code style="white-space: nowrap;">AMOUNT</code>, <code style="white-space: nowrap;">CATEGORY</code>
startDate | string | The start date of the result.


> Response Example

```json
{
  "count": "110",
  "net": 1288.45,
  "periodAmounts": [
    {
      "key": "string",
      "value": 0
    }
  ],
  "query": {
    "endDate": "1455740874875",
    "includeUpcoming": false,
    "limit": "20",
    "offset": "20",
    "order": "ASC",
    "queryString": "Food this week",
    "sort": "DATE",
    "startDate": "1455740874875"
  },
  "results": [
    {
      "transaction": {
        "accountId": "3fe2d96efacd4dc5994404a950f238a9",
        "amount": 34.5,
        "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
        "categoryType": "EXPENSES",
        "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
        "date": "1455740874875",
        "description": "Stadium Sergelg Stockholm",
        "id": "79c6c9c27d6e42489e888e08d27205a1",
        "lastModified": "1455740874875",
        "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
        "notes": "wedding",
        "originalAmount": 34.5,
        "originalDate": "1455740874875",
        "originalDescription": "Stadium Sergelg Stockholm",
        "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
        "pending": false,
        "timestamp": "1464543093494",
        "type": "CREDIT_CARD",
        "upcoming": true,
        "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
      },
      "type": "TRANSACTION"
    }
  ]
}
```


### Response: SearchResponse

Parameter | Type | Description
--------- | ---- | -----------
count | integer | Number of results returned.
net | number | The transaction amount net of the result.
periodAmounts | array[StringDoublePair] | Key value object holding periods and statistics values for result with the period specified in query.
query | SearchQuery | The query executed.
results | array[SearchResult] | The search result.


# Statistics Service

## Query for Statistics

Returns statistics matching the query

`POST /statistics/query`

> Request Example

```json
{
  "description": "fe9e199c2ca94c12baf1f3eb4a4122de",
  "padResultUntilToday": true,
  "periods": [
    "2014-02-11",
    "2014-02-12"
  ],
  "resolution": "DAILY",
  "types": [
    "expenses-by-account"
  ]
}
```


### Body: StatisticQuery

The query object

Parameter | Type | Description
--------- | ---- | -----------
description | string | Identifier of the data the statistic represents.
padResultUntilToday | boolean | Indicates if the result should be flat filled until the period of today.
periods | array[string] | Time periods for the statistics: year, month, week or day. Format: '2014', '2014-02', 2014:45 or '2014-02-12'
resolution | string | Resolution for the statistics.. Values: <code style="white-space: nowrap;">DAILY</code>, <code style="white-space: nowrap;">MONTHLY</code>, <code style="white-space: nowrap;">MONTHLY_ADJUSTED</code>, <code style="white-space: nowrap;">YEARLY</code>, <code style="white-space: nowrap;">ALL</code>, <code style="white-space: nowrap;">WEEKLY</code>
types | array[string] | A list of types of statistics. See Statistics for type information.


> Response Example

```json
{
  "description": "fe9e199c2ca94c12baf1f3eb4a4122de",
  "payload": "690667930d7e4f2ba0d9aa5f7d2a1941",
  "period": "2014-12-15",
  "resolution": "DAILY",
  "type": "expenses-by-account",
  "userId": "d9f134ee2eb44846a4e02990ecc8d32e",
  "value": 1298.5
}
```


### Response: Statistic

Parameter | Type | Description
--------- | ---- | -----------
description | string | Identifier of the data the statistic represents.
payload | string | Secondary identifier of the data the statistic represent
period | string | The statistic's period, depends on it's resolution. On of: year, month, week or day. Format: '2014', '2014-02', 2014:45 or '2014-02-12'
resolution | string | Resolution for the statistics.. Values: <code style="white-space: nowrap;">DAILY</code>, <code style="white-space: nowrap;">MONTHLY</code>, <code style="white-space: nowrap;">MONTHLY_ADJUSTED</code>, <code style="white-space: nowrap;">YEARLY</code>, <code style="white-space: nowrap;">ALL</code>, <code style="white-space: nowrap;">WEEKLY</code>
type | string | The statistic's type.
userId | string | The internal identifier of the user that the statistics belongs to.
value | number | The value of the statistics for this type, period, and description.


# Transaction Service

Transactions Service

## Get one transaction

Returns a transaction matching the requested id

`GET /transactions/{id}`

### Parameters

Parameter | Description
--------- | -----------
id | The id of the transaction


> Response Example

```json
{
  "accountId": "3fe2d96efacd4dc5994404a950f238a9",
  "amount": 34.5,
  "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
  "categoryType": "EXPENSES",
  "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
  "date": "1455740874875",
  "description": "Stadium Sergelg Stockholm",
  "id": "79c6c9c27d6e42489e888e08d27205a1",
  "lastModified": "1455740874875",
  "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
  "notes": "wedding",
  "originalAmount": 34.5,
  "originalDate": "1455740874875",
  "originalDescription": "Stadium Sergelg Stockholm",
  "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
  "pending": false,
  "timestamp": "1464543093494",
  "type": "CREDIT_CARD",
  "upcoming": true,
  "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
}
```


### Response: Transaction

Parameter | Type | Description
--------- | ---- | -----------
accountId | string | The internal identifier of the account that the transaction belongs to.
amount | number | The amount of the transaction. This can be modified by the user.
categoryId | string | The category of the transaction. This can be modified by the user.
categoryType | string | The category type of the transaction.. Values: <code style="white-space: nowrap;">INCOME</code>, <code style="white-space: nowrap;">EXPENSES</code>, <code style="white-space: nowrap;">TRANSFERS</code>
credentialsId | string | The internal identifier of the credentials that the transaction belongs to.
date | string | The date the transaction was executed. This can be modified by the user.
description | string | The description of the transaction. This can be modified by the user.
id | string | The internal identifier of the transaction.
lastModified | string | The date the transaction was last modified by the user.
merchantId | string | The internal identifier of the merchant that the transaction belongs to. If available.
notes | string | A note specified by the user. This can be modified by the user.
originalAmount | number | The original amount that was received from the provider, before the user changed it.
originalDate | string | The original date that was received from the provider, before the user changed it.
originalDescription | string | The original description that was received from the provider, before the user changed it.
payload | object | Meta data about the transaction, in key value format with Strings.
pending | boolean | Indicates if this transaction has been settled or is still pending.
timestamp | integer | The timestamp of when the transaction was first saved to database.
type | string | The type of the transaction.. Values: <code style="white-space: nowrap;">DEFAULT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">TRANSFER</code>, <code style="white-space: nowrap;">PAYMENT</code>, <code style="white-space: nowrap;">WITHDRAWAL</code>
upcoming | boolean | Indicates if this is an upcoming transaction not booked yet.
userId | string | The internal identifier of the user that the transaction belongs to.


## Update a transaction

Updates certain user modifiable properties of a transaction

`PUT /transactions/{id}`

> Request Example

```json
{
  "accountId": "3fe2d96efacd4dc5994404a950f238a9",
  "amount": 34.5,
  "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
  "categoryType": "EXPENSES",
  "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
  "date": "1455740874875",
  "description": "Stadium Sergelg Stockholm",
  "id": "79c6c9c27d6e42489e888e08d27205a1",
  "lastModified": "1455740874875",
  "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
  "notes": "wedding",
  "originalAmount": 34.5,
  "originalDate": "1455740874875",
  "originalDescription": "Stadium Sergelg Stockholm",
  "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
  "pending": false,
  "timestamp": "1464543093494",
  "type": "CREDIT_CARD",
  "upcoming": true,
  "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
}
```


### Parameters

Parameter | Description
--------- | -----------
id | The id of the transaction


### Body: Transaction

The transaction to be updated

Parameter | Type | Description
--------- | ---- | -----------
accountId | string | The internal identifier of the account that the transaction belongs to.
amount | number | The amount of the transaction. This can be modified by the user.
categoryId | string | The category of the transaction. This can be modified by the user.
categoryType | string | The category type of the transaction.. Values: <code style="white-space: nowrap;">INCOME</code>, <code style="white-space: nowrap;">EXPENSES</code>, <code style="white-space: nowrap;">TRANSFERS</code>
credentialsId | string | The internal identifier of the credentials that the transaction belongs to.
date | string | The date the transaction was executed. This can be modified by the user.
description | string | The description of the transaction. This can be modified by the user.
id | string | The internal identifier of the transaction.
lastModified | string | The date the transaction was last modified by the user.
merchantId | string | The internal identifier of the merchant that the transaction belongs to. If available.
notes | string | A note specified by the user. This can be modified by the user.
originalAmount | number | The original amount that was received from the provider, before the user changed it.
originalDate | string | The original date that was received from the provider, before the user changed it.
originalDescription | string | The original description that was received from the provider, before the user changed it.
payload | object | Meta data about the transaction, in key value format with Strings.
pending | boolean | Indicates if this transaction has been settled or is still pending.
timestamp | integer | The timestamp of when the transaction was first saved to database.
type | string | The type of the transaction.. Values: <code style="white-space: nowrap;">DEFAULT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">TRANSFER</code>, <code style="white-space: nowrap;">PAYMENT</code>, <code style="white-space: nowrap;">WITHDRAWAL</code>
upcoming | boolean | Indicates if this is an upcoming transaction not booked yet.
userId | string | The internal identifier of the user that the transaction belongs to.


> Response Example

```json
{
  "accountId": "3fe2d96efacd4dc5994404a950f238a9",
  "amount": 34.5,
  "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
  "categoryType": "EXPENSES",
  "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
  "date": "1455740874875",
  "description": "Stadium Sergelg Stockholm",
  "id": "79c6c9c27d6e42489e888e08d27205a1",
  "lastModified": "1455740874875",
  "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
  "notes": "wedding",
  "originalAmount": 34.5,
  "originalDate": "1455740874875",
  "originalDescription": "Stadium Sergelg Stockholm",
  "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
  "pending": false,
  "timestamp": "1464543093494",
  "type": "CREDIT_CARD",
  "upcoming": true,
  "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
}
```


### Response: Transaction

Parameter | Type | Description
--------- | ---- | -----------
accountId | string | The internal identifier of the account that the transaction belongs to.
amount | number | The amount of the transaction. This can be modified by the user.
categoryId | string | The category of the transaction. This can be modified by the user.
categoryType | string | The category type of the transaction.. Values: <code style="white-space: nowrap;">INCOME</code>, <code style="white-space: nowrap;">EXPENSES</code>, <code style="white-space: nowrap;">TRANSFERS</code>
credentialsId | string | The internal identifier of the credentials that the transaction belongs to.
date | string | The date the transaction was executed. This can be modified by the user.
description | string | The description of the transaction. This can be modified by the user.
id | string | The internal identifier of the transaction.
lastModified | string | The date the transaction was last modified by the user.
merchantId | string | The internal identifier of the merchant that the transaction belongs to. If available.
notes | string | A note specified by the user. This can be modified by the user.
originalAmount | number | The original amount that was received from the provider, before the user changed it.
originalDate | string | The original date that was received from the provider, before the user changed it.
originalDescription | string | The original description that was received from the provider, before the user changed it.
payload | object | Meta data about the transaction, in key value format with Strings.
pending | boolean | Indicates if this transaction has been settled or is still pending.
timestamp | integer | The timestamp of when the transaction was first saved to database.
type | string | The type of the transaction.. Values: <code style="white-space: nowrap;">DEFAULT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">TRANSFER</code>, <code style="white-space: nowrap;">PAYMENT</code>, <code style="white-space: nowrap;">WITHDRAWAL</code>
upcoming | boolean | Indicates if this is an upcoming transaction not booked yet.
userId | string | The internal identifier of the user that the transaction belongs to.


## Update a list of transactions

Updates certain user modifiable properties of a list of transactions

`PUT /transactions`

> Request Example

```json
{
  "accountId": "3fe2d96efacd4dc5994404a950f238a9",
  "amount": 34.5,
  "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
  "categoryType": "EXPENSES",
  "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
  "date": "1455740874875",
  "description": "Stadium Sergelg Stockholm",
  "id": "79c6c9c27d6e42489e888e08d27205a1",
  "lastModified": "1455740874875",
  "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
  "notes": "wedding",
  "originalAmount": 34.5,
  "originalDate": "1455740874875",
  "originalDescription": "Stadium Sergelg Stockholm",
  "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
  "pending": false,
  "timestamp": "1464543093494",
  "type": "CREDIT_CARD",
  "upcoming": true,
  "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
}
```


### Body: Transaction

The transactions to be updated

Parameter | Type | Description
--------- | ---- | -----------
accountId | string | The internal identifier of the account that the transaction belongs to.
amount | number | The amount of the transaction. This can be modified by the user.
categoryId | string | The category of the transaction. This can be modified by the user.
categoryType | string | The category type of the transaction.. Values: <code style="white-space: nowrap;">INCOME</code>, <code style="white-space: nowrap;">EXPENSES</code>, <code style="white-space: nowrap;">TRANSFERS</code>
credentialsId | string | The internal identifier of the credentials that the transaction belongs to.
date | string | The date the transaction was executed. This can be modified by the user.
description | string | The description of the transaction. This can be modified by the user.
id | string | The internal identifier of the transaction.
lastModified | string | The date the transaction was last modified by the user.
merchantId | string | The internal identifier of the merchant that the transaction belongs to. If available.
notes | string | A note specified by the user. This can be modified by the user.
originalAmount | number | The original amount that was received from the provider, before the user changed it.
originalDate | string | The original date that was received from the provider, before the user changed it.
originalDescription | string | The original description that was received from the provider, before the user changed it.
payload | object | Meta data about the transaction, in key value format with Strings.
pending | boolean | Indicates if this transaction has been settled or is still pending.
timestamp | integer | The timestamp of when the transaction was first saved to database.
type | string | The type of the transaction.. Values: <code style="white-space: nowrap;">DEFAULT</code>, <code style="white-space: nowrap;">CREDIT_CARD</code>, <code style="white-space: nowrap;">TRANSFER</code>, <code style="white-space: nowrap;">PAYMENT</code>, <code style="white-space: nowrap;">WITHDRAWAL</code>
upcoming | boolean | Indicates if this is an upcoming transaction not booked yet.
userId | string | The internal identifier of the user that the transaction belongs to.


## Get categorization clusters

Returns an object holding clusters of transactions to be categorized and possible categorization level improvement

`GET /transactions/suggest`

### Query Parameters

Parameter | Description
--------- | -----------
numberOfClusters | Max number of clusters returned
evaluateEverything | 


> Response Example

```json
{
  "categorizationImprovement": 0.01,
  "categorizationLevel": 0.93,
  "clusters": [
    {
      "categorizationImprovement": 0.003,
      "description": "McDonalds Stock",
      "transactions": [
        {
          "accountId": "3fe2d96efacd4dc5994404a950f238a9",
          "amount": 34.5,
          "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
          "categoryType": "EXPENSES",
          "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
          "date": "1455740874875",
          "description": "Stadium Sergelg Stockholm",
          "id": "79c6c9c27d6e42489e888e08d27205a1",
          "lastModified": "1455740874875",
          "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
          "notes": "wedding",
          "originalAmount": 34.5,
          "originalDate": "1455740874875",
          "originalDescription": "Stadium Sergelg Stockholm",
          "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
          "pending": false,
          "timestamp": "1464543093494",
          "type": "CREDIT_CARD",
          "upcoming": true,
          "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
        }
      ]
    }
  ]
}
```


### Response: SuggestTransactionsResponse

Parameter | Type | Description
--------- | ---- | -----------
categorizationImprovement | number | The categorization improvement achieve if all clusters are categorized.
categorizationLevel | number | The current categorization level before categorization.
clusters | array[TransactionCluster] | Clusters to categorize.


## Change category of transactions

Changes category of the supplied list of transactions to the supplied category

`POST /transactions/categorize`

> Request Example

```json
{
  "categoryId": "2d3bd65493b549e1927d97a2d0683ab9",
  "transactionIds": [
    "92e9e178cc22437281084c572ada8d7d",
    "a40db0b79bf94d2a9340cbc35d8b8020"
  ]
}
```


### Body: CategorizeTransactionsRequest

List of objects holding new category and the transactions to be categorized

Parameter | Type | Description
--------- | ---- | -----------
categoryId | string | The internal identifier of the category that the list of transactions is categorized to.
transactionIds | array[string] | A list of internal identifiers of the transactions categorized.


## Get similar transactions

Returns an object holding a list of transactions similar to the supplied transaction based on description and a list of statistics summarizing these transactions

`GET /transactions/{id}/similar`

### Parameters

Parameter | Description
--------- | -----------
id | The id of the transaction


### Query Parameters

Parameter | Description
--------- | -----------
categoryId | Returns similar of the this cateogry
includeSelf | Include the supplied transaction in response


> Response Example

```json
{
  "statistics": [
    {
      "description": "fe9e199c2ca94c12baf1f3eb4a4122de",
      "payload": "690667930d7e4f2ba0d9aa5f7d2a1941",
      "period": "2014-12-15",
      "resolution": "DAILY",
      "type": "expenses-by-account",
      "userId": "d9f134ee2eb44846a4e02990ecc8d32e",
      "value": 1298.5
    }
  ],
  "transactions": [
    {
      "accountId": "3fe2d96efacd4dc5994404a950f238a9",
      "amount": 34.5,
      "categoryId": "0e1bade6a7e3459eb794f27b7ba4cea0",
      "categoryType": "EXPENSES",
      "credentialsId": "65bc7a41a66e4ad1aad199bbfb3c5098",
      "date": "1455740874875",
      "description": "Stadium Sergelg Stockholm",
      "id": "79c6c9c27d6e42489e888e08d27205a1",
      "lastModified": "1455740874875",
      "merchantId": "ba3f9312fa7d442abde61ca419877fbf",
      "notes": "wedding",
      "originalAmount": 34.5,
      "originalDate": "1455740874875",
      "originalDescription": "Stadium Sergelg Stockholm",
      "payload": "{TRANSFER_ACCOUNT:'40dc04e5353547378c84f34ffc88f853'}",
      "pending": false,
      "timestamp": "1464543093494",
      "type": "CREDIT_CARD",
      "upcoming": true,
      "userId": "d9f134ee2eb44846a4e02990ecc8d32e"
    }
  ]
}
```


### Response: SimilarTransactionsResponse

Parameter | Type | Description
--------- | ---- | -----------
statistics | array[Statistic] | Statistics of type 'income-and-expenses-and-transfers' for the similar transactions.
transactions | array[Transaction] | List of similar transactions.


# User Service

User Service handles operations regarding the User

## Get the user

Returns the user object. Note that the password field is not stored in clear text nor populated when getting the user. It's only used for setting the password when registering a new user.

`GET /user`

> Response Example

```json
{
  "created": "string",
  "flags": [
    "string",
    "string"
  ],
  "id": "6e68cc6287704273984567b3300c5822",
  "password": "string",
  "profile": {
    "currency": "SEK",
    "locale": "sv_SE",
    "market": "SE",
    "notificationSettings": {
      "balance": false,
      "budget": false,
      "doubleCharge": false,
      "income": false,
      "largeExpense": false,
      "summaryMonthly": false,
      "summaryWeekly": false,
      "transaction": false,
      "unusualAccount": false,
      "unusualCategory": false
    },
    "periodAdjustedDay": "25",
    "periodMode": "MONTHLY_ADJUSTED",
    "timeZone": "Europe/Stockholm"
  },
  "username": "nisse@manpower.se"
}
```


### Response: User

Parameter | Type | Description
--------- | ---- | -----------
created | string | The date when the user was created.
flags | array[string] | The user-specific feature flags assigned to the user.
id | string | The internal identifier of the user.
password | string | The password of the user (only included at registration).
profile | UserProfile | The configurable profile of the user
username | string | The username (usually email) of the user.


## Update the user

Updates certain user modifiable properties of a user. Please refer to the body schema to see which properties are modifiable by the user.

`PUT /user`

> Request Example

```json
{
  "created": "string",
  "flags": [
    "string",
    "string"
  ],
  "id": "6e68cc6287704273984567b3300c5822",
  "password": "string",
  "profile": {
    "currency": "SEK",
    "locale": "sv_SE",
    "market": "SE",
    "notificationSettings": {
      "balance": false,
      "budget": false,
      "doubleCharge": false,
      "income": false,
      "largeExpense": false,
      "summaryMonthly": false,
      "summaryWeekly": false,
      "transaction": false,
      "unusualAccount": false,
      "unusualCategory": false
    },
    "periodAdjustedDay": "25",
    "periodMode": "MONTHLY_ADJUSTED",
    "timeZone": "Europe/Stockholm"
  },
  "username": "nisse@manpower.se"
}
```


### Body: User

The updated user object

Parameter | Type | Description
--------- | ---- | -----------
created | string | The date when the user was created.
flags | array[string] | The user-specific feature flags assigned to the user.
id | string | The internal identifier of the user.
password | string | The password of the user (only included at registration).
profile | UserProfile | The configurable profile of the user
username | string | The username (usually email) of the user.


> Response Example

```json
{
  "created": "string",
  "flags": [
    "string",
    "string"
  ],
  "id": "6e68cc6287704273984567b3300c5822",
  "password": "string",
  "profile": {
    "currency": "SEK",
    "locale": "sv_SE",
    "market": "SE",
    "notificationSettings": {
      "balance": false,
      "budget": false,
      "doubleCharge": false,
      "income": false,
      "largeExpense": false,
      "summaryMonthly": false,
      "summaryWeekly": false,
      "transaction": false,
      "unusualAccount": false,
      "unusualCategory": false
    },
    "periodAdjustedDay": "25",
    "periodMode": "MONTHLY_ADJUSTED",
    "timeZone": "Europe/Stockholm"
  },
  "username": "nisse@manpower.se"
}
```


### Response: User

Parameter | Type | Description
--------- | ---- | -----------
created | string | The date when the user was created.
flags | array[string] | The user-specific feature flags assigned to the user.
id | string | The internal identifier of the user.
password | string | The password of the user (only included at registration).
profile | UserProfile | The configurable profile of the user
username | string | The username (usually email) of the user.


## Get the user profile

Returns the user profile.

`GET /user/profile`

> Response Example

```json
{
  "currency": "SEK",
  "locale": "sv_SE",
  "market": "SE",
  "notificationSettings": {
    "balance": false,
    "budget": false,
    "doubleCharge": false,
    "income": false,
    "largeExpense": false,
    "summaryMonthly": false,
    "summaryWeekly": false,
    "transaction": false,
    "unusualAccount": false,
    "unusualCategory": false
  },
  "periodAdjustedDay": "25",
  "periodMode": "MONTHLY_ADJUSTED",
  "timeZone": "Europe/Stockholm"
}
```


### Response: UserProfile

Parameter | Type | Description
--------- | ---- | -----------
currency | string | The configured ISO 4217 currency code of the user. This can be modified by the user.
locale | string | The configured locale of the user. This can be modified by the user.
market | string | The primary market/country of the user.
notificationSettings | NotificationSettings | The configured notification settings of the user. This can be modified by the user.
periodAdjustedDay | integer | The configured day of the month to break the adjusted period on. This can be modified by the user.
periodMode | string | The configured monthly period mode of the user. This can be modified by the user.. Values: <code style="white-space: nowrap;">MONTHLY</code>, <code style="white-space: nowrap;">MONTHLY_ADJUSTED</code>
timeZone | string | The configured time zone of the user. This can be modified by the user.


## Update the user profile

Updates certain user modifiable properties of a user's profile. Please refer to the body schema to see which properties are modifiable by the user.

`PUT /user/profile`

> Request Example

```json
{
  "currency": "SEK",
  "locale": "sv_SE",
  "market": "SE",
  "notificationSettings": {
    "balance": false,
    "budget": false,
    "doubleCharge": false,
    "income": false,
    "largeExpense": false,
    "summaryMonthly": false,
    "summaryWeekly": false,
    "transaction": false,
    "unusualAccount": false,
    "unusualCategory": false
  },
  "periodAdjustedDay": "25",
  "periodMode": "MONTHLY_ADJUSTED",
  "timeZone": "Europe/Stockholm"
}
```


### Body: UserProfile

The updated user profile object

Parameter | Type | Description
--------- | ---- | -----------
currency | string | The configured ISO 4217 currency code of the user. This can be modified by the user.
locale | string | The configured locale of the user. This can be modified by the user.
market | string | The primary market/country of the user.
notificationSettings | NotificationSettings | The configured notification settings of the user. This can be modified by the user.
periodAdjustedDay | integer | The configured day of the month to break the adjusted period on. This can be modified by the user.
periodMode | string | The configured monthly period mode of the user. This can be modified by the user.. Values: <code style="white-space: nowrap;">MONTHLY</code>, <code style="white-space: nowrap;">MONTHLY_ADJUSTED</code>
timeZone | string | The configured time zone of the user. This can be modified by the user.


> Response Example

```json
{
  "currency": "SEK",
  "locale": "sv_SE",
  "market": "SE",
  "notificationSettings": {
    "balance": false,
    "budget": false,
    "doubleCharge": false,
    "income": false,
    "largeExpense": false,
    "summaryMonthly": false,
    "summaryWeekly": false,
    "transaction": false,
    "unusualAccount": false,
    "unusualCategory": false
  },
  "periodAdjustedDay": "25",
  "periodMode": "MONTHLY_ADJUSTED",
  "timeZone": "Europe/Stockholm"
}
```


### Response: UserProfile

Parameter | Type | Description
--------- | ---- | -----------
currency | string | The configured ISO 4217 currency code of the user. This can be modified by the user.
locale | string | The configured locale of the user. This can be modified by the user.
market | string | The primary market/country of the user.
notificationSettings | NotificationSettings | The configured notification settings of the user. This can be modified by the user.
periodAdjustedDay | integer | The configured day of the month to break the adjusted period on. This can be modified by the user.
periodMode | string | The configured monthly period mode of the user. This can be modified by the user.. Values: <code style="white-space: nowrap;">MONTHLY</code>, <code style="white-space: nowrap;">MONTHLY_ADJUSTED</code>
timeZone | string | The configured time zone of the user. This can be modified by the user.


## List markets

Returns an object with a list of all available markets in which a user could register with.

`GET /user/markets/list`

### Query Parameters

Parameter | Description
--------- | -----------
desired | The ISO 3166-1 alpha-2 country code of the desired market


> Response Example

```json
{
  "markets": [
    {
      "code": "SE",
      "currencies": [
        {
          "code": "SEK",
          "factor": 10,
          "prefixed": false,
          "symbol": "kr"
        }
      ],
      "defaultCurrency": "SEK",
      "defaultLocale": "sv_SE",
      "defaultTimeZone": "Europe/Stockholm",
      "description": "Sweden",
      "status": false
    }
  ]
}
```


### Response: MarketListResponse

Parameter | Type | Description
--------- | ---- | -----------
markets | array[Market] | 


