from flask import Flask, render_template, request, jsonify
import boto3
import csv
from io import StringIO
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuration
S3_BUCKET = 'your-s3-bucket-name'
CSV_FILE = 'documents.csv'
s3_client = boto3.client('s3')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload_files', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')
    response_message = []
    for file in files:
        filename = file.filename
        file_content = file.read()

        # Check if document exists in CSV
        try:
            csv_content = s3_client.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)['Body'].read().decode('utf-8')
            csv_reader = list(csv.DictReader(StringIO(csv_content)))
        except Exception as e:
            csv_reader = []

        document_exists = any(row['Document Name'] == filename for row in csv_reader)

        if document_exists:
            return jsonify({'message': f'{filename} already exists. Do you want to update it?', 'status': 'exists'}), 409

        # Upload file to S3
        s3_client.put_object(Bucket=S3_BUCKET, Key=f'documents/{filename}', Body=file_content)

        # Add new entry to CSV
        csv_reader.append({
            'Document Name': filename,
            'Date Uploaded': datetime.now().strftime('%Y-%m-%d'),
            'Last Updated': datetime.now().strftime('%Y-%m-%d'),
            'Owner': 'User'
        })

        # Write updated CSV back to S3
        csv_content = StringIO()
        csv_writer = csv.DictWriter(csv_content, fieldnames=['Document Name', 'Date Uploaded', 'Last Updated', 'Owner'])
        csv_writer.writeheader()
        csv_writer.writerows(csv_reader)
        s3_client.put_object(Bucket=S3_BUCKET, Key=CSV_FILE, Body=csv_content.getvalue())
        response_message.append(f'{filename} uploaded successfully.')

    return jsonify({'message': ' '.join(response_message), 'status': 'success'})

@app.route('/update_file', methods=['POST'])
def update_file():
    file = request.files['file']
    filename = file.filename
    file_content = file.read()

    # Upload file to S3
    s3_client.put_object(Bucket=S3_BUCKET, Key=f'documents/{filename}', Body=file_content)

    # Update entry in CSV
    csv_content = s3_client.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)['Body'].read().decode('utf-8')
    csv_reader = list(csv.DictReader(StringIO(csv_content)))

    for row in csv_reader:
        if row['Document Name'] == filename:
            row['Last Updated'] = datetime.now().strftime('%Y-%m-%d')
            break

    # Write updated CSV back to S3
    csv_content = StringIO()
    csv_writer = csv.DictWriter(csv_content, fieldnames=['Document Name', 'Date Uploaded', 'Last Updated', 'Owner'])
   
