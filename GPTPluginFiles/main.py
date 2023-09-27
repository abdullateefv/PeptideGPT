import os
from waitress import serve
from flask import Flask, request, jsonify, send_from_directory
import requests
import random

app = Flask(__name__)

def get_energy(peptideSequence):
  return {"energy": random.random() * 200 - 100}


@app.route('/dock', methods=['GET'])
def dock():
  sequence = request.args.get('sequence')

  try:
    energy = get_energy(sequence)
    return jsonify({
      "sequence": sequence,
      "energy": energy
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 400

# https://hoster.abdullateef2.repl.co/.well-known/ai-plugin.json
@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')


# https://hoster.abdullateef2.repl.co/.well-known/openapi.yaml
@app.route('/.well-known/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


if __name__ == '__main__':
  serve(app, host="0.0.0.0", port=8080)
