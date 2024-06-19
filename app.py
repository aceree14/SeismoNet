from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)  # Ini mengaktifkan CORS untuk semua rute

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://gempa:@localhost/gempa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)  # inisialisasi app Flask ke SQLAlchemy

# Definisi kelas Earthquake
class Earthquake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Tanggal = db.Column(db.String(255), nullable=False)
    Jam = db.Column(db.String(255), nullable=True)
    DateTime = db.Column(db.String(255), nullable=True)
    Coordinates = db.Column(db.String(255), nullable=True)
    Lintang = db.Column(db.String(255), nullable=True)
    Bujur = db.Column(db.String(255), nullable=True)
    Magnitude = db.Column(db.String(255), nullable=True)
    Kedalaman = db.Column(db.String(255), nullable=True)
    Wilayah = db.Column(db.String(255), nullable=True)
    Potensi = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "Tanggal": self.Tanggal,
            "Jam": self.Jam,
            "DateTime": self.DateTime,
            "Coordinates": self.Coordinates,
            "Lintang": self.Lintang,
            "Bujur": self.Bujur,
            "Magnitude": self.Magnitude,
            "Kedalaman": self.Kedalaman,
            "Wilayah": self.Wilayah,
            "Potensi": self.Potensi
        }

@app.route('/api/earthquakes', methods=['GET'])
def get_earthquakes():
    earthquakes = Earthquake.query.all()
    return jsonify([eq.to_dict() for eq in earthquakes])

@app.route('/api/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake is None:
        abort(404)
    return jsonify(earthquake.to_dict())

@app.route('/api/earthquakes', methods=['POST'])
def create_earthquake():
    if not request.json or not 'Tanggal' in request.json:
        abort(400)
    earthquake = Earthquake(
        Tanggal=request.json['Tanggal'],
        Jam=request.json.get('Jam', ""),
        DateTime=request.json.get('DateTime', ""),
        Coordinates=request.json.get('Coordinates', ""),
        Lintang=request.json.get('Lintang', ""),
        Bujur=request.json.get('Bujur', ""),
        Magnitude=request.json.get('Magnitude', ""),
        Kedalaman=request.json.get('Kedalaman', ""),
        Wilayah=request.json.get('Wilayah', ""),
        Potensi=request.json.get('Potensi', "")
    )
    db.session.add(earthquake)
    db.session.commit()
    return jsonify(earthquake.to_dict()), 201

@app.route('/api/earthquakes/<int:id>', methods=['PUT'])
def update_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake is None:
        abort(404)
    if not request.json:
        abort(400)
    earthquake.Tanggal = request.json.get('Tanggal', earthquake.Tanggal)
    earthquake.Jam = request.json.get('Jam', earthquake.Jam)
    earthquake.DateTime = request.json.get('DateTime', earthquake.DateTime)
    earthquake.Coordinates = request.json.get('Coordinates', earthquake.Coordinates)
    earthquake.Lintang = request.json.get('Lintang', earthquake.Lintang)
    earthquake.Bujur = request.json.get('Bujur', earthquake.Bujur)
    earthquake.Magnitude = request.json.get('Magnitude', earthquake.Magnitude)
    earthquake.Kedalaman = request.json.get('Kedalaman', earthquake.Kedalaman)
    earthquake.Wilayah = request.json.get('Wilayah', earthquake.Wilayah)
    earthquake.Potensi = request.json.get('Potensi', earthquake.Potensi)
    db.session.commit()
    return jsonify(earthquake.to_dict())

@app.route('/api/earthquakes/<int:id>', methods=['DELETE'])
def delete_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake is None:
        abort(404)
    db.session.delete(earthquake)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)