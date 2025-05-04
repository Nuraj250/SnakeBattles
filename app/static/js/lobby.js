const socket = io();

function joinGame() {
    const username = document.getElementById('username').value;
    const room = document.getElementById('room').value || 'default';
    if (!username) {
        alert('Please enter your username!');
        return;
    }
    window.location.href = `/game?username=${username}&room=${room}`;
}

async function sendChat() {
    const message = document.getElementById('chat-input').value;
    if (!message) return;

    const response = await fetch('/ai_chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    chatBox.innerHTML += `<p><strong>AI:</strong> ${data.reply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
    document.getElementById('chat-input').value = '';
}

function sendEmoji(emoji) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${emoji}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
