Its a small project 
**1. Whenever it detect any file in the GCS it should keep that in respective folder and it should collect the logs of the Cloud Function in BQ**

step 1: Set Up Google Cloud Storage (GCS)
Create a GCS Bucket:
Go to the Google Cloud Console.
Navigate to "Cloud Storage" and create a new bucket.
Step 2: Set Up a Cloud Function
Create a Cloud Function:

Navigate to "Cloud Functions" in the Google Cloud Console.
Click "Create Function".
Configure the basic settings such as name, region, and memory allocation.
Set the Trigger:

Choose "Cloud Storage" as the trigger.
Select the bucket you created.
Choose "Finalized" for the event type to trigger the function when a file is uploaded.

step: 3 is the code

Deploy the Cloud Function:
Click "Deploy" to deploy the function.
Step 3: Test the Function
Upload Files:
Upload different types of files (images, documents, audio) to the GCS bucket.
The Cloud Function should automatically organize these files into respective folders (images/, documents/, audio/, others/).
Final Steps
Step 4: Set Up BigQuery
Create a BigQuery Dataset and Table:
Go to the BigQuery section in the Google Cloud Console.
Create a new dataset.
Create a new table within the dataset with the following schema:
original_file_name (STRING)
new_file_name (STRING)
timestamp (TIMESTAMP)
Step 5: Test the Function
Upload Files:
Upload different types of files (images, documents, audio) to the GCS bucket.
The Cloud Function should automatically organize these files into respective folders (images/, documents/, audio/, others/).
Final Steps
Verify File Organization:

Check the bucket to ensure files are moved to the correct folders.
Verify Logs in BigQuery:

Check the BigQuery table to see the logs of the file operations.
Monitor and Logs:

Monitor the function's execution and view logs in the Google Cloud Console under "Cloud Functions" and "Logs".
This setup ensures that whenever a new file is uploaded to the GCS bucket, the Cloud Function is triggered, and the file is moved to the appropriate folder based on its type. Additionally, the file operations are logged in BigQuery for further analysis and tracking.


