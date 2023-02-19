# AWS_BankSystem
---
## Lambda functions for admin and users to manage DynamoDB.

Options for admin:
- Create table
- Create item
- Read all items by .scan()
- Read items sorted by a specific attribute by GSI and .query()
- Update item
- Delete table
- Delete item

Options for user:
- Create item
- Read item
- Update item
- Delete item

Inputs from APIs RESTful method are specified in the code.
  
---
## Problems remains to be solved
- It costs a lot of time for DynamoDB to be ready for the next usage when creating GSI. Normally it is much more than the time limit set for Lambda function. 
- Not sure whether it is appropriate to set up the static sort key to read out all the items in table.
