import os
import socket

import redis
from flask import Flask, jsonify
from redis import RedisError

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
    try:
        redis_client.ping()
        return jsonify({"status": "ok"}), 200
    except RedisError:
        return jsonify({"status": "error"}), 503

@application.route("/visits", methods=["GET"])
def ping():
    key = "visits"
    val = redis_client.incr(key)
    return jsonify({"visits": val}), 200

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=os.getenv("APP_PORT", "8080"))