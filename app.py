from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)






@app.route("/")
def index():
    tasks = [
    "Buy groceries",
    "Call mom",
    "Finish project"
]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", tasks=tasks, timestamp=timestamp)
   


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
