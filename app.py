from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ini mengaktifkan CORS untuk semua rute

# In-memory storage for earthquakes
earthquakes = {}

# Load initial data from gempaterkini.json (if necessary)
# with open('gempaterkini.json', 'r') as file:
#     earthquakes = json.load(file)

@app.route('/api/earthquakes', methods=['GET'])
def get_earthquakes():
    return jsonify(list(earthquakes.values()))

@app.route('/api/earthquakes/<id>', methods=['GET'])
def get_earthquake(id):
    earthquake = earthquakes.get(id)
    if earthquake is None:
        abort(404)
    return jsonify(earthquake)

@app.route('/api/earthquakes', methods=['POST'])
def create_earthquake():
    if not request.json or not 'Tanggal' in request.json:
        abort(400)
    id = str(len(earthquakes) + 1)
    earthquake = {
        "id": id,
        "Tanggal": request.json['Tanggal'],
        "Jam": request.json.get('Jam', ""),
        "DateTime": request.json.get('DateTime', ""),
        "Coordinates": request.json.get('Coordinates', ""),
        "Lintang": request.json.get('Lintang', ""),
        "Bujur": request.json.get('Bujur', ""),
        "Magnitude": request.json.get('Magnitude', ""),
        "Kedalaman": request.json.get('Kedalaman', ""),
        "Wilayah": request.json.get('Wilayah', ""),
        "Potensi": request.json.get('Potensi', "")
    }
    earthquakes[id] = earthquake
    return jsonify(earthquake), 201

@app.route('/api/earthquakes/<id>', methods=['PUT'])
def update_earthquake(id):
    earthquake = earthquakes.get(id)
    if earthquake is None:
        abort(404)
    if not request.json:
        abort(400)
    earthquake['Tanggal'] = request.json.get('Tanggal', earthquake['Tanggal'])
    earthquake['Jam'] = request.json.get('Jam', earthquake['Jam'])
    earthquake['DateTime'] = request.json.get('DateTime', earthquake['DateTime'])
    earthquake['Coordinates'] = request.json.get('Coordinates', earthquake['Coordinates'])
    earthquake['Lintang'] = request.json.get('Lintang', earthquake['Lintang'])
    earthquake['Bujur'] = request.json.get('Bujur', earthquake['Bujur'])
    earthquake['Magnitude'] = request.json.get('Magnitude', earthquake['Magnitude'])
    earthquake['Kedalaman'] = request.json.get('Kedalaman', earthquake['Kedalaman'])
    earthquake['Wilayah'] = request.json.get('Wilayah', earthquake['Wilayah'])
    earthquake['Potensi'] = request.json.get('Potensi', earthquake['Potensi'])
    earthquakes[id] = earthquake
    return jsonify(earthquake)

@app.route('/api/earthquakes/<id>', methods=['DELETE'])
def delete_earthquake(id):
    earthquake = earthquakes.pop(id, None)
    if earthquake is None:
        abort(404)
    return jsonify({'result': True})

@app.route('/api/earthquakes/delete_by_criteria', methods=['DELETE'])
def delete_by_criteria():
    ids_to_delete = [id for id, eq in earthquakes.items() if not eq.get('id')]
    for id in ids_to_delete:
        del earthquakes[id]
    return jsonify({'deleted_ids': ids_to_delete, 'result': True})

@app.route('/api/earthquakes/filter', methods=['GET'])
def filter_earthquakes_by_get():
    depth_km = request.args.get('depth_km')
    potential = request.args.get('potential')

    filtered_earthquakes = []
    for id, eq in earthquakes.items():
        if eq.get('Kedalaman') == depth_km and eq.get('Potensi') == potential:
            filtered_earthquakes.append(eq)

    return jsonify(filtered_earthquakes)

@app.route('/api/earthquakes/filter', methods=['POST'])
def filter_earthquakes_by_post():
    # Mendapatkan data filter dari permintaan
    filter_data = request.json

    # Lakukan proses filter data sesuai dengan data yang diberikan

    # Contoh: Lakukan filter data berdasarkan kedalaman (depth) dan potensi (potential)
    filtered_earthquakes = []
    for earthquake in earthquakes.values():
        if earthquake['Kedalaman'] == filter_data['depth'] and earthquake['Potensi'] == filter_data['potential']:
            filtered_earthquakes.append(earthquake)

    return jsonify(filtered_earthquakes)


if __name__ == '__main__':
    app.run(debug=True)
