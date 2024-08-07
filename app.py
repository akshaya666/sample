from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = 'your-openai-api-key-here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quick_search')
def quick_search():
    return render_template('quick_search.html')

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
        return jsonify({"message": bot_message})

    return jsonify({"message": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
