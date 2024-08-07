from flask import Flask, render_template, request, jsonify, session
import openai

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Initialize OpenAI API key
openai.api_key = 'your-openai-api-key-here'

# List of documents
documents = ["Document 1", "Document 2", "Document 3"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quick_search')
def quick_search():
    selected_document = session.get('selected_document', documents[0])
    return render_template('quick_search.html', documents=documents, selected_document=selected_document)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if user_message:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        bot_message = response.choices[0].text.strip()
        return jsonify({'message': bot_message})

    return jsonify({'message': 'No message received'}), 400

@app.route('/api/select_document', methods=['POST'])
def select_document():
    data = request.json
    selected_document = data.get('document')
    session['selected_document'] = selected_document
    return jsonify({'message': 'Document selection updated'})

if __name__ == '__main__':
    app.run(debug=True)
