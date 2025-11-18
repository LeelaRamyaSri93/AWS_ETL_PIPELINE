# 🔁 Orchestration Phase – Automating Pipeline Execution with EventBridge

## 🔍 Why This Phase?

This phase automates the ETL pipeline using AWS EventBridge. It ensures that every new CSV upload to S3 triggers the Lambda transformation and load logic without manual intervention.

---

## 🧰 Tools & Services Used

| Tool/Service       | Purpose                                         |
|--------------------|-------------------------------------------------|
| Amazon S3          | Event source for new uploads                    |
| AWS Lambda         | Target for transformation and load              |
| EventBridge        | Event routing and automation                    |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Create S3 Event Notification

- Bucket: `aws-etl-pipeline`  
- Folder: `raw-data/`  
- Trigger: On object creation  
- Destination: Lambda function

### ✅ Step 2: Configure EventBridge (Optional)

- EventBridge rule to monitor S3 events  
- Can be extended to trigger alerts or workflows

---

## 🔐 Security 

- Event-driven architecture reduces manual access  
- IAM roles restrict event permissions  
- Logs captured in CloudWatch
