 # Step 3: RDS Database Setup
   - Launched PostgreSQL instance: database-1 (db.t4.micro, us-east-1).
   - Master username: admin_ETL
   - Endpoint: <database-1.*****************.us-east-1.rds.amazonaws.com>:5432
   - Created database: drugdb
   - Run schema: CREATE TABLE drugs (drug_name, side_effects, etc.)
   - Tested via pgAdmin: Connected, inserted sample row ('Aspirin'), queried successfully.
   - Security: Inbound rule updated to my IP; public access enabled.

