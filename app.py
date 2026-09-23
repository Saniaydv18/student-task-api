from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Deploy on AWS", "completed": False},
]

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.get("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title or not isinstance(title, str):
        return jsonify({"error": "title is required"}), 400

    new_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": new_id, "title": title, "completed": False}
    tasks.append(task)

    return jsonify(task), 201

@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})

    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
