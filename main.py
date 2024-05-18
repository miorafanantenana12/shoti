from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Remplacez par votre clé API Shoti
API_KEY = 'shoti-1hu4snpkc7h9rlvnm5'
SHOTI_API_URL = 'https://shoti-api.deno.dev/'  # Remplacez par l'URL correcte de l'API Shoti

@app.route('/get_data', methods=['GET'])
def get_data():
    # Les paramètres de la requête peuvent être ajoutés ici si nécessaire
    params = {
        'api_key': API_KEY
        # Ajoutez d'autres paramètres nécessaires pour l'API Shoti ici
    }

    try:
        response = requests.get(SHOTI_API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, params=params)
        response.raise_for_status()  # Génère une exception si la requête a échoué
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    