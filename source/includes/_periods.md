# Periods

A lot of the data served by the Tink API derived from the either transactional or otherwise date-based information, is in various forms periodized into pre-computed date-based buckets for easy access. Statistics are computed for <code>YEARLY, MONTHLY</code> and <code>MONTHLY_ADJUSTED</code> buckets, which represents different time periods.

As exemplified to the right, most of this is self explanatory, except for <code>MONTHLY_ADJUSTED</code>. The <code>MOHTLY_ADJUSTED</code> buckets adjust for the fact that in many markets, people relate to their financials based on when they receive their salary. Using Sweden as an example, salary is received on the 25th of each month, and using <code>MONTHLY_ADJUSTED</code> each month in Tink includes transactional data from an adjecant calendar month, covering the entire salary cycle.

The <code>MONTHLY_ADJUSTED</code> buckets also account for the fact that salaries are not expidited on non-business days, so if the 25th of a specific month happens to be a Saturday, the period is adjusted to start of on Friday the 24th of the same month instead.

### Example

Resolution | Period | Start date | End date
---------- | ------ | ---------- | --------
<code>YEARLY</code> | <code>2015</code> | 2015-01-01 | 2015-12-31
<code>MONTHLY</code> | <code>2015-04</code> | 2015-04-01 | 2015-04-31
<code>MONTHLY_ADJUSTED</code> | <code>2015-04</code> | 2015-03-25 | 2015-04-24
