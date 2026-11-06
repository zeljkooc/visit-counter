import os
from flask import Flask, jsonify, request
import redis
import socket

application = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)

@application.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello DevOps", "host": socket.gethostname()}), 200

@application.route("/health", methods=["GET"])
def health():
    if redis_client is not None:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "error"}), 503

@application.route("/visits", methods=["GET"])
def ping():
    key = "visits"
    val = redis_client.incr(key)
    return jsonify({"visits": val}), 200

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=os.getenv("APP_PORT", "8080"))