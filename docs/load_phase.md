# 🛬 Load Phase – Secure Insertion of Structured Data into RDS Using psycopg2

## 🔍 Why This Phase?

This phase inserts cleaned data into Amazon RDS using psycopg2. It connects Lambda to PostgreSQL securely via environment variables and layers, completing the ETL pipeline.

---

## 🧰 Tools & Services Used

| Tool/Service       | Purpose                                         |
|--------------------|-------------------------------------------------|
| AWS Lambda         | Executes load logic                             |
| Amazon RDS         | Stores structured data                          |
| psycopg2           | Python PostgreSQL driver                        |
| Environment Vars   | Securely pass DB credentials                    |

---

## 🛠️ Implementation Steps

### ✅ Step 1: Set Environment Variables

- Lambda Console > Configuration > Environment Variables  
  - RDS_HOST, RDS_PORT, RDS_DBNAME, RDS_USERNAME, RDS_PASSWORD

### ✅ Step 2: Add psycopg2 Layer

- Used AWS official layer  
- Encountered import errors (`libpq.so.5` missing)

### ✅ Step 3: Build Custom Layer

- Docker build with `libpq.so.5` bundled  
- Created and attached custom layer: `psycopg2-313-custom`

### ✅ Step 4: Final Test

- Lambda reads from `processed-data/`  
- Inserts into `drugdb.drugs`  
- Verified via pgAdmin

---

## 🔐 Security 

- Credentials via env vars  
- RDS access restricted to IP/32  
- psycopg2 layer hardened for compatibility
