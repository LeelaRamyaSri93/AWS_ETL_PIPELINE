# Step 5: AWS Lambda Transformation (Complete)
- Function: etl-transform-function (Python 3.13).
- Layer: AWSSDKPandas-Python312 (for pandas/numpy).
- Code: Pasted custom lambda_function.py with exact transform.py logic (string lower/strip/join).
- IAM: AmazonS3FullAccess attached.
- Test: Manual {} event success; processed 1436 rows from raw-data/extracted_drugs.csv.
- Output: transformed_drugs.csv created in processed-data/ (verified: cleaned columns like lowercase severity, joined side_effects).
- Billing: $0 (free tier invocation).

