## Categories

The categories that are available for the user to categorize her transactions with, while structurally being a category tree, are available as a flat list of categories with parent/child relationships using their <code>id</code> and <code>parent</code> fields.

Category information is used for the pre-computed statistics, making aggregated spending and income data available for all the different nodes in the category tree. However, a transaction itself, can only be assigned to a leaf category.

Both the <code>INCOME</code> and <code>EXPENSES</code> categories represents user's regular income and spending, while the <code>TRANSFER</code> categories are special in the sense that they represent transfers between accounts (potentially across banks), such as regular bank transfers, credit-card payments, mortgage amortizations and other transactions that should not add to the user's actual spending.
