# 📈 Monitoring Phase – CloudWatch Setup for Logging, Metrics, and Alerts

## 🔍 Why This Phase?

Monitoring ensures visibility into pipeline health, failures, and performance. AWS CloudWatch captures logs, metrics, and alerts across Lambda and RDS.

---

## 🧰 Tools & Services Used

| Tool/Service       | Purpose                                         |
|--------------------|-------------------------------------------------|
| AWS CloudWatch     | Logs, metrics, and alerts                       |
| AWS Lambda         | Auto-logs execution results                     |
| Amazon RDS         | Logs queries and errors                         |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Enable CloudWatch Logging

- Lambda logs visible in CloudWatch > Log Groups  
- RDS logs under CloudWatch > Logs & Events

### ✅ Step 2: Set Billing Alerts

- AWS Billing > Budgets  
  - Budget: $0.01 
  - Email alerts enabled

### ✅ Step 3: Future Enhancements

- Add CloudWatch Alarms for:
  - Lambda errors  
  - RDS CPU/memory thresholds  
  - S3 object count spikes

---

## 🔐 Security

- Logs are encrypted at rest  
- Access restricted via IAM policies  
- Alerts sent only to verified email
