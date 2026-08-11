from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host="postgres",
        database="mydb",
        user="postgres",
        password="password"
    )


@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM users WHERE id = 1;")
    name = cur.fetchone()[0]

    cur.close()
    conn.close()

    return f"Hello {name}"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
