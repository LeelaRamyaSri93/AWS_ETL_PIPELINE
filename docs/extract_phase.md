# 📥 Extract Phase – Data Ingestion

## 🔍 Why This Phase?

The extract phase initiates the ETL pipeline by ingesting raw data into the cloud. It replaces manual file handling with automated, event-driven ingestion using Amazon S3. This phase ensures that every new CSV upload triggers the transformation workflow without human intervention.

---

## 🧰 Tools & Services Used

| Tool/Service         | Purpose                                      |
|----------------------|----------------------------------------------|
| AWS Billing Alerts   | Monitor free-tier usage and prevent overages |
| IAM (etl-user)       | Secure access to AWS resources               |
| Amazon S3            | Store raw and processed data files           |
| AWS CLI              | Manage AWS services from terminal  & UI      |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Set Up AWS Environment

- Verified AWS account and activated **Billing Alerts**  
  - Budget: $0.01  
  - Region: `us-east-1`  
  - Email notifications enabled  

- Created IAM user: `etl-user`  
  - Enabled programmatic and console access  
  - Attached `AdministratorAccess`   
  - Downloaded credentials securely  

- Installed and configured **AWS CLI**  
  - Installed via:
    ```bash
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    ```
  - Configured with:
    ```bash
    aws configure
    ```
    - Access Key ID: from credentials CSV  
    - Secret Access Key: from credentials CSV  
    - Region: `us-east-1`  
    - Output format: `json`  

- Verified CLI setup  
  - Checked versions:
    ```bash
    aws --version
    python3 --version
    git --version
    ```

- Configured Git:
    ```bash
    git config --global user.name "LeelaRamyaSri93"
    git config --global user.email "ramyasrikaruturi93@gmail.com"
    ```

- Created local project folder:
    ```bash
    mkdir ~/aws-etl-pipeline
    cd ~/aws-etl-pipeline
    ```

- Initialized Git repository and connected to GitHub:
    ```bash
    git init
    git remote add origin https://github.com/LeelaRamyaSri93/AWS_ETL_Pipeline.git
    ```

- Created and updated:
  - `README.md` → for project overview and progress tracking  
  - `.gitignore` → to exclude sensitive files  

---

### ✅ Step 2: Configure Amazon S3 for Data Ingestion

- Created S3 bucket: `aws-etl-pipeline`  
  - Region: `us-east-1`  
  - Blocked public access (default)
  - Enabled versioning  
  - Enabled SSE-S3 encryption  

- Created folders inside the bucket:  
  - `raw-data/` → for incoming CSV files  
  - `processed-data/` → for Lambda outputs and backups  

- Uploaded sample CSV: `drug_labels.csv` to `raw-data/`  

- Created **Event Notification**:  
  - Name: `raw-upload-trigger`  
  - Trigger: On object creation in `raw-data/`  
  - Destination: AWS Lambda (configured in next phase)  

---

### 🔐 Security Configuration

- Created basic bucket policy to allow access for `etl-user`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::************:user/etl-user"
      },
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::aws-etl-pipeline/*"
    }
  ]
}

