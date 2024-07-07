from flask import Flask, request, jsonify
from rag_query import Extract_context, generate_rag_response

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def respond_to_query():
    data = request.get_json()
    query = data.get('query')

    context = Extract_context(query)
    response = generate_rag_response(context, query)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)