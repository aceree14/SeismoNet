from flask_sqlalchemy import SQLAlchemy
from app import db  # Impor instance SQLAlchemy dari app.py

db = SQLAlchemy()

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
