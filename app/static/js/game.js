const socket = io();
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const params = new URLSearchParams(window.location.search);
const username = params.get('username');
const room = params.get('room') || 'default';

const player = { x: 300, y: 300, dx: 20, dy: 0, color: 'cyan', alive: true };

// Movement Control
document.addEventListener('keydown', e => {
    if (e.key === 'ArrowUp') { player.dx = 0; player.dy = -20; }
    if (e.key === 'ArrowDown') { player.dx = 0; player.dy = 20; }
    if (e.key === 'ArrowLeft') { player.dx = -20; player.dy = 0; }
    if (e.key === 'ArrowRight') { player.dx = 20; player.dy = 0; }
});

// Join Room
socket.emit('join_game', { username: username, room: room });

// Game Loop
setInterval(() => {
    if (!player.alive) return;

    player.x += player.dx;
    player.y += player.dy;

    // Detect Wall Crash
    if (player.x < 0 || player.x > canvas.width || player.y < 0 || player.y > canvas.height) {
        player.alive = false;
        flashDeath();
        socket.emit('leave_game', { username: username, room: room });
        return;
    }

    socket.emit('player_move', { username: username, room: room, x: player.x, y: player.y });
    draw();
}, 100);

// Draw Function
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (player.alive) {
        ctx.shadowBlur = 20;
        ctx.shadowColor = player.color;
        ctx.fillStyle = player.color;
    } else {
        ctx.shadowBlur = 5;
        ctx.shadowColor = 'red';
        ctx.fillStyle = 'red';
    }
    ctx.fillRect(player.x, player.y, 20, 20);
}

// Death Flash Animation
function flashDeath() {
    let flashes = 0;
    const interval = setInterval(() => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (flashes % 2 === 0) {
            ctx.fillStyle = 'red';
            ctx.fillRect(player.x, player.y, 20, 20);
        }
        flashes++;
        if (flashes > 5) clearInterval(interval);
    }, 200);
}

// Victory Voice Event
socket.on('victory_voice', data => {
    const audio = new Audio(data.audio_url);
    audio.play();
    flashVictory();
});

// Victory Screen Flash
function flashVictory() {
    const overlay = document.createElement('div');
    overlay.style.position = 'absolute';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.background = 'rgba(0,255,0,0.6)';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.style.fontSize = '60px';
    overlay.style.fontWeight = 'bold';
    overlay.innerText = '🏆 YOU WIN!';
    document.body.appendChild(overlay);
    
    setTimeout(() => overlay.remove(), 2000);
}
