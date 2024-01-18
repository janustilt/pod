from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint pour le service "pod"
@app.route('/pod', methods=['GET'])
def get_pod():
    # Récupérer le paramètre "site" depuis la requête du client
    site_param = request.args.get('site')

    # Vérifier si le paramètre "site" est fourni
    if site_param is None:
        return jsonify({'error': 'Le paramètre "site" est requis'}), 400

    # Générer la réponse JSON en fonction du paramètre "site"
    response_data = {
        'site': site_param,
        'message': f'Données pour le site {site_param}',
        'autre_information': 'Vos données spécifiques ici',
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
