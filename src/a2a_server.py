from flask import Flask, request, jsonify
from src.agents_core import CoordinatorAgent

app = Flask(__name__)
agent = CoordinatorAgent()

@app.route("/a2a", methods=["POST"])
def a2a():
    data = request.get_json()
    result = agent.route(data["input"])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()
