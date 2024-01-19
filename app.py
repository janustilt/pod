from flask import Flask, request, jsonify
#from flask_cors import CORS
from globals import qrs, qrs_lock

app = Flask(__name__)
#CORS(app)  # Active CORS pour toutes les routes

# Endpoint pour le service "getList"
@app.route('/getList', methods=['GET'])
def get_list():
    site_param = request.args.get('site')

    if site_param is None:
        return jsonify({'error': 'Le paramètre "site" est requis'}), 400

    with qrs_lock:
        filtered_qrs = [qr for qr in qrs if qr['site'] == site_param]

    response_data = filtered_qrs
    return jsonify(response_data)

# Endpoint pour le service "setStatutScanned"
@app.route('/setStatutScanned', methods=['GET', 'POST'])
def set_statut_scanned():
    if request.method == 'GET':
        qrcode_param = request.args.get('qrcode')
        qui_param = request.args.get('qui')
    elif request.method == 'POST':
        qrcode_param = request.json.get('qrcode')
        qui_param = request.json.get('qui')
    else:
        return jsonify({'error': 'Méthode non autorisée'}), 405

    if qrcode_param is None:
        return jsonify({'error': 'Le paramètre "qrcode" est requis'}), 400

    with qrs_lock:
        for qr in qrs:
            if qr['qrcode'] == qrcode_param:
                qr['statut'] = 'SCANNED'
                site = qr['site']
                if qui_param is not None:
                    qr['qui'] = qui_param
                break

    return jsonify({'site': site})
    
if __name__ == '__main__':
    app.run(debug=True)
