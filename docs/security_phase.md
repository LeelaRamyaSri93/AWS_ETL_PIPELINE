# 🔐 Security Phase – IAM Roles and Secrets Manager for Controlled Access

## 🔍 Why This Phase?

Security ensures that credentials and access are tightly controlled. This phase replaces plaintext secrets with Secrets Manager and scopes IAM roles to least privilege.

---

## 🧰 Tools & Services Used

| Tool/Service         | Purpose                                         |
|----------------------|-------------------------------------------------|
| AWS Secrets Manager  | Store RDS credentials securely                  |
| IAM Policies         | Enforce least-privilege access                  |
| Security Groups      | Restrict RDS access to specific IPs             |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Store Secrets

- Created secret: `rds-credentials`  
  - Includes host, port, dbname, username, password

### ✅ Step 2: Restrict RDS Access

- Security Group inbound rule: `ip/32`  
- Public access enabled only for dev

### ✅ Step 3: Harden IAM Roles

- replaced `AmazonS3FullAccess` with scoped policy:
  ```json
  {
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": [
      "arn:aws:s3:::aws-etl-pipeline/raw-data/*",
      "arn:aws:s3:::aws-etl-pipeline/processed-data/*"
    ]
  }
