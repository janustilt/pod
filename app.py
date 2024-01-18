from flask import Flask, request, jsonify
from globals import qrs, qrs_lock

app = Flask(__name__)

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
@app.route('/setStatutScanned', methods=['POST'])
def set_statut_scanned():
    qrcode_param = request.json.get('qrcode')

    if qrcode_param is None:
        return jsonify({'error': 'Le paramètre "qrcode" est requis'}), 400

    with qrs_lock:
        for qr in qrs:
            if qr['qrcode'] == qrcode_param:
                qr['statut'] = 'SCANNED'
                break

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
