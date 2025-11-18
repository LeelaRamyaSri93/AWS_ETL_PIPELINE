
# 📊 Transform Phase – Data Cleaning Logic Using Lambda and pandas

## 🔍 Why This Phase?

This phase automates data preprocessing using AWS Lambda and pandas. It reads raw CSVs from S3, applies cleaning logic (e.g., deduplication, missing value handling), and writes the transformed output back to S3. This replaces manual scripts with scalable, serverless transformation.

---

## 🧰 Tools & Services Used

| Tool/Service       | Purpose                                                  |
|--------------------|----------------------------------------------------------|
| AWS Lambda         | Executes transformation logic                            |
| Amazon S3          | Stores raw and processed data                            |
| pandas (Python)    | Cleans and structures CSV data                           |
| IAM Role           | Grants Lambda access to S3                               |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Prepare Lambda Code

- Created `lambda_function.py` with:
  - Read from `raw-data/`
  - Drop duplicates
  - Fill missing values
  - Save to `processed-data/`

### ✅ Step 2: Deploy Lambda

- AWS Console > Lambda > Create Function  
  - Name: `etl-transform-function`  
  - Runtime: Python 3.12  
  - Role: New role with basic permissions  
  - Pasted code and deployed

### ✅ Step 3: Grant S3 Access

- IAM Console > Role: `lambda-etl-role`  
  - Attached `AmazonS3FullAccess` (temporary)

### ✅ Step 4: Test

- Created test event `{}`  
- Output: `1436 rows processed` to `processed-data/`

---

## 🔐 Security 

- Role-based access to S3  
- No hardcoded credentials  
- Will be refined in Security Phase
