<button id="stop-generating" style="display: none;">Stop Generating</button>


let abortController = null;

function fetchBotResponse(message) {
    // Create a new AbortController for each new request
    abortController = new AbortController();
    const { signal } = abortController;

    // Show the stop button
    document.getElementById('stop-generating').style.display = 'inline-block';

    appendMessage('bot', '', false, true); // Show loader

    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message }),
        signal: signal  // Attach signal for aborting request
    })
    .then(response => response.json())
    .then(data => {
        // Remove loader and stop button
        const lastBotMessage = document.querySelector('.message.bot:last-child');
        if (lastBotMessage && lastBotMessage.innerHTML.includes('dot-loader')) {
            lastBotMessage.remove();
        }
        appendMessage('bot', data.message);
        document.getElementById('stop-generating').style.display = 'none';
        enableFeedback();
    })
    .catch(error => {
        if (error.name === 'AbortError') {
            appendMessage('bot', 'Response generation stopped.');
        } else {
            appendMessage('bot', 'An error occurred.');
        }
        document.getElementById('stop-generating').style.display = 'none';
        console.error('Error:', error);
    });
}

// Add event listener to the Stop Generating button
document.getElementById('stop-generating').addEventListener('click', function() {
    if (abortController) {
        abortController.abort();  // Cancel the fetch request
        document.getElementById('stop-generating').style.display = 'none';  // Hide the button
    }
});



#stop-generating {
    background-color: rgba(0, 71, 123, 1);
    color: white;
    border: none;
    padding: 10px;
    font-size: 14px;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 10px;
    display: none;  /* Initially hidden */
}

#stop-generating:hover {
    background-color: rgba(0, 71, 123, 0.8);
}

