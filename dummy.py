from flask import Flask, render_template, request, jsonify
import boto3
import csv
import os
from io import StringIO

app = Flask(__name__)

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
        # Upload file to S3
        s3_client.put_object(Bucket=S3_BUCKET, Key=f'documents/{filename}', Body=file_content)

        # Check if document exists in CSV
        csv_content = s3_client.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)['Body'].read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(csv_content))
        document_exists = False
        for row in csv_reader:
            if row['Document Name'] == filename:
                document_exists = True
                break

        if document_exists:
            response_message.append(f'{filename} already exists. Do you want to update it?')
            # Logic to handle document update
        else:
            # Add new entry to CSV
            csv_content = StringIO()
            csv_writer = csv.DictWriter(csv_content, fieldnames=['Document Name', 'Date Uploaded', 'Last Updated', 'Owner'])
            csv_writer.writeheader()
            csv_writer.writerows(csv_reader)
            csv_writer.writerow({'Document Name': filename, 'Date Uploaded': '2023-01-01', 'Last Updated': '2023-01-01', 'Owner': 'User'})
            s3_client.put_object(Bucket=S3_BUCKET, Key=CSV_FILE, Body=csv_content.getvalue())
            response_message.append(f'{filename} uploaded successfully.')

    return jsonify({'message': ' '.join(response_message)})

@app.route('/api/documents')
def get_documents():
    csv_content = s3_client.get_object(Bucket=S3_BUCKET, Key=CSV_FILE)['Body'].read().decode('utf-8')
    csv_reader = csv.DictReader(StringIO(csv_content))
    documents = [row for row in csv_reader]
    return jsonify(documents)

if __name__ == '__main__':
    app.run(debug=True)
