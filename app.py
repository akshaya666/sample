import os
import pandas as pd
import boto3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from io import StringIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# AWS S3 Configuration
S3_BUCKET = 'your-s3-bucket-name'
S3_KEY = 'your-aws-access-key'
S3_SECRET = 'your-aws-secret-key'
S3_REGION = 'your-aws-region'

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET,
    region_name=S3_REGION
)

def get_s3_file_url(bucket, filename):
    return f"https://{bucket}.s3.{S3_REGION}.amazonaws.com/{filename}"

def load_csv_from_s3(bucket, key):
    try:
        csv_obj = s3.get_object(Bucket=bucket, Key=key)
        return pd.read_csv(csv_obj['Body'])
    except s3.exceptions.NoSuchKey:
        return pd.DataFrame(columns=['Document Name', 'Date Uploaded', 'Last Updated', 'Owner'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    csv_data = load_csv_from_s3(S3_BUCKET, 'documents.csv')
    return render_template('upload.html', tables=[csv_data.to_html(classes='data', header="true", index=False)])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        filename = file.filename
        s3.upload_fileobj(file, S3_BUCKET, filename)

        # Update CSV file
        csv_data = load_csv_from_s3(S3_BUCKET, 'documents.csv')

        # Check if file already exists
        if filename in csv_data['Document Name'].values:
            # Update the existing record
            csv_data.loc[csv_data['Document Name'] == filename, 'Last Updated'] = pd.Timestamp.now()
        else:
            # Add new record
            new_record = {'Document Name': filename, 'Date Uploaded': pd.Timestamp.now(), 'Last Updated': pd.Timestamp.now(), 'Owner': 'OwnerName'}
            csv_data = csv_data.append(new_record, ignore_index=True)

        # Save updated CSV back to S3
        csv_buffer = StringIO()
        csv_data.to_csv(csv_buffer, index=False)
        s3.put_object(Bucket=S3_BUCKET, Key='documents.csv', Body=csv_buffer.getvalue())

        updated_table_html = csv_data.to_html(classes='data', header="true", index=False)
        return jsonify({'message': 'File successfully uploaded to S3', 'table': updated_table_html})

if __name__ == '__main__':
    app.run(debug=True)
