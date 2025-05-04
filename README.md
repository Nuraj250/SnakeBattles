# 🐍 SnakeBattles

An exciting **real-time multiplayer Snake Game** with **AI-powered features**:
- Multiplayer via **WebSocket**
- AI-generated **Snake Skins** (Stable Diffusion)
- AI **Chatbot** for the Lobby (DialoGPT)
- AI **Snake Bots** if no opponents found
- **TTS Victory Voice** announcements
- Beautiful **Glassmorphism + Neon Glow** UI
- Private **Room Codes** for friends-only matches
- **Emoji reactions** in chat
- **Docker Deployment** ready

Built using:
- Backend: **Flask**, **Flask-SocketIO**
- Frontend: **HTML5**, **Canvas API**, **Vanilla JS**
- AI Models: via **Hugging Face Inference API**
- Deployment: **Docker** supported

---

# 🚀 Features

| Feature | Description |
|:---|:---|
| 🎮 Multiplayer Snake Game | Play with friends in real-time |
| 🎨 AI Snake Skins | Custom skins generated for each player |
| 🧑‍🎨 AI Avatars | Cute avatars auto-generated |
| 💬 AI Chatbot | Talk to a bot while waiting |
| 🤖 Auto Snake Bots | AI snakes join if players are missing |
| 🔈 Victory TTS | Celebrate wins with voice |
| ✨ Neon Glow Effects | Glowing snake effects |
| 🔒 Private Room Codes | Invite-only game rooms |
| 😂 Emoji Chat | Fun reactions in lobby |
| 🎵 Background Music | Relaxing lobby music |
| 🐳 Dockerfile | Deploy anywhere easily |

---

# 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nuraj250/snakebattles-ai.git
cd snakebattles-ai
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
```

(🔑 Get your Hugging Face API token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens))

### 4. Create Database

```bash
flask shell
>>> from app import db
>>> db.create_all()
```

(Optional: Seed sample players)

```bash
python database/seed.py
```

### 5. Run the App

```bash
python run.py
```

Go to: [http://localhost:5000](http://localhost:5000)

---

# 🐳 Run using Docker

```bash
docker build -t snakebattles-ai .
docker run -p 5000:5000 snakebattles-ai
```

---

# 📂 Project Structure

```bash
snakebattles-ai/
│
├── app/
│   ├── ai/                # AI modules (skins, chat, bots, tts)
│   ├── static/            # CSS, JS, Audio, Images
│   ├── templates/         # HTML pages
│   ├── models.py          # Database models
│   ├── routes.py          # Flask routes
│   ├── sockets.py         # WebSocket events
│   ├── utils.py           # Helpers
│   └── __init__.py        # App Factory
├── database/
│   ├── db.sqlite3
│   └── seed.py
├── tests/
│   ├── test_game_logic.py
│   ├── test_ai_features.py
├── run.py
├── requirements.txt
├── config.py
├── .env
├── Dockerfile
└── README.md
```

---

# 🎯 Future Roadmap

* ELO Ranking System 📈
* Smart RL Snake Bots 🤖
* Powerups & Boosters ⚡
* Customizable Maps 🗺️
* Mobile-friendly version 📱
* Skins Marketplace 🎨

---

# 🙌 Credits

* [Flask](https://flask.palletsprojects.com/)
* [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
* [Hugging Face API](https://huggingface.co/)
* [Stable Diffusion Models](https://huggingface.co/stabilityai)
* [OpenAssistant Chat Models](https://huggingface.co/OpenAssistant)

---

# 📢 License

MIT License.
Feel free to use, modify, and have fun! 🚀

---

# 🎉 Enjoy the Battles!

> "Real champions don't just survive — they slither to victory!" 🐍🏆