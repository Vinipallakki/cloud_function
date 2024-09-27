import os
import logging
from google.cloud import storage, bigquery

# Set up logging
logging.basicConfig(level=logging.INFO)

def organize_files(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This function organizes files into folders based on their type.
       It also logs the file operations to BigQuery.
    """
    file_name = data['name']
    bucket_name = data['bucket']

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Determine the folder based on file type
    _, file_extension = os.path.splitext(file_name)
    if file_extension in ['.jpg', '.jpeg', '.png']:
        folder = 'images/'
    elif file_extension in ['.txt', '.pdf', '.docx']:
        folder = 'documents/'
    elif file_extension in ['.mp3', '.wav']:
        folder = 'audio/'
    else:
        folder = 'others/'

    # Construct the new file path
    new_file_name = folder + os.path.basename(file_name)
    new_blob = bucket.blob(new_file_name)

    # Copy the file to the new location
    new_blob.rewrite(blob)

    # Delete the old file
    blob.delete()

    # Log the operation to BigQuery
    log_to_bigquery(file_name, new_file_name)

    logging.info(f"File {file_name} moved to {new_file_name}.")

def log_to_bigquery(original_file_name, new_file_name):
    """Log the file operation to BigQuery."""
    client = bigquery.Client()
    table_id = "your-project.your_dataset.your_table"  # Replace with your project, dataset, and table ID

    rows_to_insert = [
        {
            "original_file_name": original_file_name,
            "new_file_name": new_file_name,
            "timestamp": bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
        }
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        logging.info("New rows have been added.")
    else:
        logging.error(f"Encountered errors while inserting rows: {errors}")
