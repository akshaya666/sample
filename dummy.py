let abortController = null;

function fetchBotResponse(message) {
    abortController = new AbortController();
    const { signal } = abortController;

    // Show the stop button
    document.getElementById('stop-generating').style.display = 'inline-block';

    appendLoader(); // Show loader

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
        removeLoader();  // Remove loader
        appendMessage('bot', data.message);
        document.getElementById('stop-generating').style.display = 'none';
        enableFeedback();
    })
    .catch(error => {
        removeLoader();  // Always remove the loader in case of error or abort
        if (error.name !== 'AbortError') {
            appendMessage('bot', 'An error occurred.');
        }
        document.getElementById('stop-generating').style.display = 'none';
    });
}

// Add event listener to the Stop Generating button
document.getElementById('stop-generating').addEventListener('click', function() {
    if (abortController) {
        abortController.abort();  // Cancel the fetch request
        document.getElementById('stop-generating').style.display = 'none';  // Hide the button
        removeLoader();  // Immediately remove the loader
    }
});

function appendLoader() {
    // Show loader (bot typing animation)
    const loaderElem = document.createElement('div');
    loaderElem.className = 'message bot';
    loaderElem.id = 'loader';
    loaderElem.innerHTML = '<div class="dot-loader"><div></div><div></div><div></div></div>';
    chatBox.appendChild(loaderElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeLoader() {
    // Remove loader (bot typing animation)
    const loaderElem = document.getElementById('loader');
    if (loaderElem) {
        loaderElem.remove();
    }
}
