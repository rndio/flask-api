from app import db

class Dosen(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  nidn = db.Column(db.String(30), index=True, unique=True, nullable=False)
  nama = db.Column(db.String(250), nullable=False)
  phone = db.Column(db.String(15), nullable=False)
  alamat = db.Column(db.String(250), nullable=False)

  def __repr__(self):
    return '<Dosen {}>'.format(self.nama)
