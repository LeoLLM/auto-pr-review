#!/usr/bin/env python3
# API for PR automation test

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    """Return the current status of the application."""
    return jsonify({
        'status': 'healthy',
        'version': '0.1.0',
        'environment': 'development'
    })

@app.route('/api/pull-requests', methods=['GET'])
def list_pull_requests():
    """Mock endpoint to list pull requests."""
    # This is just a mock response
    return jsonify([
        {
            'id': 1,
            'title': 'Add frontend feature',
            'author': 'developer1',
            'status': 'open'
        },
        {
            'id': 2,
            'title': 'Fix backend bug',
            'author': 'developer2',
            'status': 'merged'
        }
    ])

if __name__ == '__main__':
    app.run(debug=True)