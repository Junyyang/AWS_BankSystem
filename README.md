# AWS_BankSystem
---
## Access pattern for admin and users to manage DynamoDB.

Access for admin:
- Create table(Creat GSI)
- Create item
- Read all items
- Read items sorted by a GSI "IndexName"
- Update item
- Delete table
- Delete item

Access for user:
- Create item
- Read item
- Update item
- Delete item

Inputs from APIs RESTful method are specified in the code.
---
## Problems remains to be solved
- If the attribute upload from API is vacant, how to deal with it.
 - assigned with None?
- How to load the profile picture? S3 Bucket?