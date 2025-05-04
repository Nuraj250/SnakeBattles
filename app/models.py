from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, default=0)
    skin_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Player {self.username}>"
