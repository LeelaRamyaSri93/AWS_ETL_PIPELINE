# Step 2: Configure S3 Storage
- Created bucket: aws-etl-pipeline-bucket-2025 (us-east-1, versioning enabled).
- Folders: raw-data/, processed-data/.
- Uploaded sample CSV: realistic_drug_labels_side_effects.csv to raw-data/.
- Tested via CLI: aws s3 ls and cp commands.
- Bucket policy: Default private.

