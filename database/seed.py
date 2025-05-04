from app import create_app, db
from app.models import Player

app = create_app()
app.app_context().push()

def seed_players():
    players = [
        Player(username="player1", score=100),
        Player(username="player2", score=200),
        Player(username="bot_snake", score=50)
    ]
    db.session.bulk_save_objects(players)
    db.session.commit()

if __name__ == "__main__":
    seed_players()
    print("Database seeded successfully!")
