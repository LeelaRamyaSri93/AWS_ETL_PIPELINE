import json
import boto3
import pandas as pd
from io import StringIO  # For reading CSV from S3 as string

s3 = boto3.client('s3')

def lambda_handler(event, context):
    if 'Records' in event:  # From S3 trigger
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
    else:  
        bucket = 'aws-etl-pipeline-bucket-2025' 
        key = 'raw_data/realistic_drug_labels_side_effects.csv'  

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        raw_data = response['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(raw_data))

        # Transform: Exact logic
        df['side_effect_severity'] = df['side_effect_severity'].str.lower().str.strip()
        df['indications'] = df['indications'].apply(lambda x: ', '.join([i.strip() for i in str(x).split(',')]))
        df['side_effects'] = df['side_effects'].apply(lambda x: ','.join([i.strip() for i in str(x).split(',')]))
        df['drug_class'] = df['drug_class'].str.strip()
        df['approval_status'] = df['approval_status'].str.strip()

        # Save transformed CSV to S3 
        transformed_key = 'processed_data/transformed_drugs.csv'  
        csv_buffer = df.to_csv(index=False)
        s3.put_object(Bucket=bucket, Key=transformed_key, Body=csv_buffer)

        return {
            'statusCode': 200,
            'body': json.dumps(f'Transform complete: {len(df)} rows processed. Output saved to {transformed_key}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }


    # Load into RDS PostgreSQL
    try:
        conn = psycopg2.connect(
            host=os.environ['RDS_HOST'],
            port=os.environ['RDS_PORT'],
            dbname=os.environ['RDS_DBNAME'],
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD']
        )
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO drugs (drug_name, indications, side_effects, side_effect_severity, drug_class, approval_status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                row['drug_name'],
                row['indications'],
                row['side_effects'],
                row['side_effect_severity'],
                row['drug_class'],
                row['approval_status']
            ))

        conn.commit()
        cursor.close()
        conn.close()
        return {
            'statusCode': 200,
            'body': f"{len(df)} rows transformed and loaded successfully."
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error loading data: {str(e)}"
        }
