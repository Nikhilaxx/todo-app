from flask import Flask, render_template
import os
app = Flask(__name__)

tasks = [
    "Buy groceries",
    "Call mom",
    "Finish project"
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


   


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
