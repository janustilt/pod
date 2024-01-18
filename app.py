from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint pour le service "pod"
@app.route('/pod', methods=['GET'])
def get_pod():
    # Récupérer le paramètre "site" depuis la requête du client
    site_param = request.args.get('site')

    qrs = [
        {
            'qrcode' : '406f0859-fc2c-4d70-ac29-4b3302049703',
            'filename' : '123456_AZERTY_20240124180212_OR.TXT',
            'type' : 'TPM',
            'rest_home_name' : 'Paix du soir',
            'logistic_tag' : '1erEtage',
            'officine' : '159',
            'site' : 'SPL',
            'statut' : 'PMI',
            'creation_date' : '2024-01-24 18:06:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : '66051d36-a268-4292-b6fd-6187aa7871d3',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'LEGACY',
            'rest_home_name' : 'Silence',
            'logistic_tag' : 'rez',
            'officine' : '38',
            'site' : 'LIEGE',
            'statut' : 'PMI',
            'creation_date' : '2024-01-24 18:10:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : 'c1cf5616-7a54-426c-b5b1-8c61e58de0e2',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'EXTRA',
            'rest_home_name' : '',
            'logistic_tag' : '',
            'officine' : '721',
            'site' : 'LIEGE',
            'statut' : 'EXTRA',
            'creation_date' : '2024-01-24 18:10:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : '1f19866b-3c48-46a9-ace5-330d564c8aa2',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'RC',
            'rest_home_name' : 'ARCADIA',
            'logistic_tag' : 'top',
            'officine' : '721',
            'site' : '721',
            'statut' : 'RC',
            'creation_date' : '2024-01-24 8:00:12',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : 'ab6d9f53-0d8c-47cb-9af0-fa58af2907d9',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'RC',
            'rest_home_name' : 'ARCADIA',
            'logistic_tag' : 'ciel',
            'officine' : '721',
            'site' : '721',
            'statut' : 'RC',
            'creation_date' : '2024-01-24 8:00:13',
            'qui' : 'addQRcodeRC'
        }
    ]
        
    # Vérifier si le paramètre "site" est fourni
    if site_param is None:
        return jsonify({'error': 'Le paramètre "site" est requis'}), 400

    filtered_qrs = [qr for qr in qrs if qr['site'] == site_param]
    
    # Générer la réponse JSON en fonction du paramètre "site"
    response_data = filtered_qrs

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
