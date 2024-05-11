from flask import Flask, jsonify
from decouple import config
import psycopg2


app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "oke"})
                    

@app.route("/db_check")                 
def db_check():
    conn_pg = psycopg2.connect(
        host=config['MB_DB_HOST'],
        database=config['MB_DB_DBNAME'],
        user=config['MB_DB_USER'],
        password=config['MB_DB_PASS'],
        port=config['MB_DB_PORT'],
    )
    cur = conn_pg.cursor()
    return jsonify({"status": 200, "db": "connected"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")