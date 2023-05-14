const messages = document.getElementById('messages');
const query = document.getElementById('query');
const send = document.getElementById('send');

messages.innerHTML = '<div class="message">Hi there! 😊 Ask me anything about the Twitter algorithm.</div>';

function appendMessage(text, isUser) {
    const msg = document.createElement('div');
    msg.innerText = text;
    msg.classList.add('message');
    if (isUser) {
        msg.classList.add('user-message');
    }
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
}

send.addEventListener('click', async () => {
    if (!query.value.trim()) return;

    appendMessage(query.value, true);

    const thinkingMsg = document.createElement('div');
    thinkingMsg.classList.add('message', 'thinking-message');
    messages.appendChild(thinkingMsg);

    const response = await fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `question=${encodeURIComponent(query.value)}`
    });

    const data = await response.json();
    messages.removeChild(thinkingMsg);
    appendMessage(data.answer, false);

    query.value = '';
});

query.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        send.click();
    }
});
