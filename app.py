from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# AWS S3 configuration
S3_BUCKET = 'your_s3_bucket_name'
S3_KEY = 'your_aws_access_key'
S3_SECRET = 'your_aws_secret_key'
S3_REGION = 'your_s3_region'

s3 = boto3.client('s3', region_name=S3_REGION, aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            s3.upload_fileobj(file, S3_BUCKET, filename)
            flash('File successfully uploaded')
            return redirect(url_for('upload'))
    
    files = s3.list_objects_v2(Bucket=S3_BUCKET).get('Contents', [])
    return render_template('upload.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
