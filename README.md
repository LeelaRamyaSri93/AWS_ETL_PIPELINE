# ☁️ AWS ETL Pipeline: Serverless Data Processing with S3, Lambda, and RDS



## 🧩 Problem Statement

In my earlier project, I built a Linux-based ETL pipeline using shell scripting, Python, and PostgreSQL. While effective for learning, it relied on manual execution, local dependencies, and lacked scalability. To overcome these limitations, I transitioned to a **cloud-native ETL pipeline** that automates data ingestion, transformation, and storage using AWS services.

This project reflects that evolution from traditional scripting to **event-driven, serverless architecture**.

---

## 🚀 Solution Overview

### 🧠 What is ETL?

**ETL (Extract, Transform, Load)** is a foundational data engineering process:

- **Extract**: Pull raw data from a source (e.g., CSV, APIs)  
- **Transform**: Clean, format, and validate data  
- **Load**: Insert structured data into a target system (e.g., database)  

Cloud-native ETL pipelines offer:

- **Scalability**: Handle growing data volumes without manual intervention  
- **Automation**: Triggered by events or schedules, reducing human effort  
- **Security**: IAM roles and Secrets Manager protect sensitive operations  
- **Observability**: CloudWatch tracks performance and errors in real time  

This project applies ETL to a dataset of drug information, using AWS services to automate each phase.

---

## 📁 Project Structure

- `scripts/`
- `lambda/`: Contains the Python transformation logic executed by AWS Lambda
- `docs/`: Phase-wise documentation with implementation details, service usage, and reasoning
- `assets/screenshots/`: Visual references of AWS services (S3, Lambda logs, RDS schema, etc.)
- `architecture-diagram.jpeg`: End-to-end architecture of the AWS ETL pipeline
- `README.md`: Project overview, workflow, and setup instructions  

---

## 🛠️ Tech Stack

- AWS (S3, Lambda, RDS, EventBridge, CloudWatch, IAM, Secrets Manager)
- Python (`pandas`, `psycopg2`)
- PostgreSQL
- Cloud-native architecture
- Serverless orchestration

---

## 🚀 ETL Workflow Overview

| Phase         | Service(s) Used                            | Output/Action                                      |
|---------------|--------------------------------------------|----------------------------------------------------|
| Extract       | Amazon S3                                  | `drugs_data.csv` uploaded to S3 bucket             |
| Transform     | AWS Lambda (Python + pandas)               | Cleaned and structured data in-memory              |
| Load          | Amazon RDS (PostgreSQL) + psycopg2         | Data inserted into `drugs` table                   |
| Orchestration | Amazon EventBridge                         | Lambda triggered on S3 upload or scheduled daily   |
| Security      | IAM + AWS Secrets Manager                  | Controlled access and secure DB credentials        |
| Monitoring    | AWS CloudWatch                             | Logs, metrics, and alerts for Lambda execution     |

---

## 📚 Documentation

Detailed guides available in the `docs/` folder:

- [Extract Phase](docs/extract_phase.md): Why data ingestion is critical and how S3 triggers the pipeline  
- [Transform Phase](docs/transform_phase.md): Data cleaning logic using Lambda and pandas  
- [Load Phase](docs/load_phase.md): Secure insertion of structured data into RDS using psycopg2  
- [Orchestration](docs/orchestration.md): Automating pipeline execution with EventBridge  
- [Security](docs/security.md): IAM roles and Secrets Manager for controlled access  
- [Monitoring](docs/monitoring.md): CloudWatch setup for logging, metrics, and alerts  

---

## 🖼️ Visual Reference

![Architecture Diagram](architecture-diagram.jpeg)

Additional screenshots available in `assets/screenshots/`.

---
