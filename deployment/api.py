from flask import Flask, request, jsonify
from src.agent.agent import SmartAssistAgent
from src.rag.rag_pipeline import RAGPipeline

app = Flask(__name__)

rag = RAGPipeline()
agent = SmartAssistAgent(rag)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
    result = agent.run(query)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
