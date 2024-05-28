from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'your_huggingface_api_key' with your actual Hugging Face API key
HUGGING_FACE_API_KEY = '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'
MODEL_ID = 'HuggingFaceH4/zephyr-7b-beta'
API_URL = f'https://api-inference.huggingface.co/models/{MODEL_ID}'

headers = {
    'Authorization': f'Bearer {HUGGING_FACE_API_KEY}'
}

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    response = requests.post(API_URL, headers=headers, json={"inputs": question})
    
    if response.status_code == 200:
        result = response.json()
        answer = result[0]['generated_text'] if result else "No response"
        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'Failed to get a response from the model'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
