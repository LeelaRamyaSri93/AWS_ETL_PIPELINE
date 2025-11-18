# ☁️ AWS ETL Pipeline: Serverless Data Processing with S3, Lambda, and RDS

---

## 🧩 Problem Statement

In my earlier project, I built a Linux-based ETL pipeline using shell scripting, Python, and PostgreSQL. While effective for learning, it relied on manual execution, local dependencies, and lacked scalability. To overcome these limitations, I transitioned to a **cloud-native ETL pipeline** that automates data ingestion, transformation, and storage using AWS services.

This project reflects that evolution from traditional scripting to **event-driven, serverless architecture**.

---

## 🚀 Solution Overview

Cloud-native ETL pipelines offer:

- **Scalability**: Handle growing data volumes without manual intervention  
- **Automation**: Triggered by events or schedules, reducing human effort  
- **Security**: IAM roles and Secrets Manager protect sensitive operations  
- **Observability**: CloudWatch tracks performance and errors in real time  

### 🧠 What is ETL?

**ETL (Extract, Transform, Load)** is a foundational data engineering process:

- **Extract**: Pull raw data from a source (e.g., CSV, APIs)  
- **Transform**: Clean, format, and validate data  
- **Load**: Insert structured data into a target system (e.g., database)  

This project applies ETL to a dataset of drug information, using AWS services to automate each phase.

---

## 📁 Project Structure
aws-etl-pipeline/ 
├── README.md 
├── architecture-diagram.png 
├── lambda/ 
│   └── transform_function.py 
├── docs/ 
│   └── pipeline_steps.md 
│   └── troubleshooting.md 
├── assets/ 
│   └── screenshots/


---

## 🛠️ Tech Stack

| Tool/Service             | Purpose                          |
|--------------------------|----------------------------------|
| Amazon S3                | Raw data storage                 |
| AWS Lambda (Python)      | Data transformation              |
| Amazon RDS (PostgreSQL)  | Structured data storage          |
| IAM                      | Access control                   |
| AWS Secrets Manager      | Credential management            |
| Amazon EventBridge       | Scheduling and orchestration     |
| AWS CloudWatch           | Monitoring and logging           |
| Python (pandas, psycopg2)| Data manipulation and DB access  |

---

## 📚 Documentation

Detailed guides available in the `docs/` folder:

- `pipeline_steps.md`: Step-by-step explanation of each ETL phase  
- `troubleshooting.md`: Common issues and how they were resolved  

---

## 🖼️ Visual Reference

![Architecture Diagram](architecture-diagram.png)

Additional screenshots available in `assets/screenshots/`.

---
