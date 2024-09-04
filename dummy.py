from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import boto3
import os
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Initialize S3 client
s3 = boto3.client('s3')
BUCKET_NAME = 'your-bucket-name'

# Placeholder for local knowledge base (in a real app, this would be a database or stored on S3)
knowledge_bases = ["Knowledgebase 1", "Knowledgebase 2"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/manage_knowledgebase', methods=['GET', 'POST'])
def manage_knowledgebase():
    if request.method == 'POST':
        # Create a new knowledge base (in a real app, you'd store this in a DB or S3)
        new_knowledgebase = request.form.get('knowledgebase_name')
        if new_knowledgebase:
            knowledge_bases.append(new_knowledgebase)
            flash(f'Knowledgebase "{new_knowledgebase}" created successfully!', 'success')
        else:
            flash('Please enter a valid knowledgebase name.', 'error')
        return redirect(url_for('manage_knowledgebase'))

    # Render the knowledge base management page
    return render_template('manage_knowledgebase.html', knowledge_bases=knowledge_bases)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    knowledgebase = request.args.get('knowledgebase')
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_key = f"{knowledgebase}/{file.filename}"
            s3.upload_fileobj(file, BUCKET_NAME, file_key)
            flash(f'File "{file.filename}" uploaded successfully to {knowledgebase}!', 'success')
            return redirect(url_for('upload', knowledgebase=knowledgebase))

    return render_template('upload.html', knowledgebase=knowledgebase)


@app.route('/api/documents', methods=['GET'])
def get_documents():
    # Example: Fetch a list of documents from S3 (assuming CSV is stored in S3)
    documents = []
    try:
        # Use boto3 to fetch the CSV file that holds the document information
        response = s3.get_object(Bucket=BUCKET_NAME, Key='knowledge_base/documents.csv')
        content = response['Body'].read().decode('utf-8')
        csv_reader = csv.DictReader(content.splitlines())
        for row in csv_reader:
            documents.append(row)
    except Exception as e:
        print(f"Error fetching documents: {e}")

    return jsonify(documents)


if __name__ == '__main__':
    app.run(debug=True)

