## Statistics

By querying the statistics endpoint, an API consumer can select the specific types of data to access. The query should be posted in the request body and you can specify any of the properties available to filter the result set. Defining multiple properties will yield an <code>AND</code> operation, and specifying multiple values of a property will yield an <code>OR</code> operation.

### Statistics types

Type | <code>description</code> value
---- | -----------------
<code>expenses-by-category</code> | Primary identifier of a <code>category</code>
<code>expenses-by-account</code> | Primary identifier of an <code>account</code>
<code>income-by-category</code> | Primary identifier of a <code>category</code>
<code>income-by-account</code> | Primary identifier of an <code>account</code>
<code>balances-by-account</code> | Primary identifier of an <code>account</code>
<code>left-to-spend</code> | None
<code>left-to-spend-average</code> | None
