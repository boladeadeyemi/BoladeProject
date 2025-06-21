from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins; safe behind NGINX

# Members API route
@app.route("/api/groupmembers", methods=['GET'])
def group_members():
    return jsonify({
        "groupMembers": [
            'Bolade', 'Felix', 'Idowu', 'James', 'Agape', 'Oyerinde',
            'John', 'Folashade', 'Ifeoluwa', 'Paul', 'Peter', 'Peace',
            'Esther', 'Covenant', 'Hassan', 'Ingrid'
        ]
    })

if __name__ == '__main__':
    # Production settings
    app.run(host="0.0.0.0", port=5000)
