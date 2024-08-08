<head>
    ...
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>

function appendMessage(sender, message, isFeedback = false, isLoader = false) {
    const messageElem = document.createElement('div');
    messageElem.className = `message ${sender}`;
    if (isLoader) {
        messageElem.innerHTML = '<div class="dot-loader"><div></div><div></div><div></div></div>';
    } else {
        messageElem.innerHTML = marked(message);
        if (sender === 'bot' && !isFeedback) {
            const copyIcon = document.createElement('i');
            copyIcon.className = 'fas fa-copy';
            copyIcon.onclick = () => {
                navigator.clipboard.writeText(message);
            };
            messageElem.appendChild(copyIcon);
        }
    }
    chatBox.appendChild(messageElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}

.message {
    margin: 10px;
    padding: 10px 15px;
    border-radius: 10px;
    position: relative;
    max-width: 60%;
    word-wrap: break-word;
    display: flex;
    box-sizing: border-box;
}
