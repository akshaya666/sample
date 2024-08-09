/* Custom Scrollbar Styling for Chat Window */
.chat-window {
    max-height: 500px; /* Adjust as needed */
    overflow-y: auto;
    scrollbar-width: thin; /* For Firefox */
    scrollbar-color: rgba(0, 71, 123, 1) #f3f3f3; /* Thumb and track colors for Firefox */
}

.chat-window::-webkit-scrollbar {
    width: 8px; /* Width of the scrollbar */
}

.chat-window::-webkit-scrollbar-thumb {
    background-color: rgba(0, 71, 123, 1); /* Color of the scrollbar thumb */
    border-radius: 4px; /* Roundness of the scrollbar thumb */
    border: 2px solid #f3f3f3; /* Padding around the thumb for better aesthetics */
}

.chat-window::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 71, 123, 0.8); /* Darken the thumb on hover */
}

.chat-window::-webkit-scrollbar-track {
    background-color: #f3f3f3; /* Color of the scrollbar track */
    border-radius: 4px; /* Roundness of the scrollbar track */
}
