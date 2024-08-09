/* Custom Scrollbar Styling for Chat Window */
.chat-box {
    flex: 1;
    background-color: white;
    border-radius: 10px;
    padding: 10px;
    overflow-y: auto;
    border: 1px solid rgba(0, 71, 123, 1);
    margin-bottom: 10px;
    max-height: calc(100vh - 200px);
    display: flex;
    flex-direction: column;
    scrollbar-width: thin; /* For Firefox */
    scrollbar-color: rgba(0, 71, 123, 1) #f3f3f3; /* Thumb and track colors for Firefox */
}

.chat-box::-webkit-scrollbar {
    width: 8px; /* Width of the scrollbar */
}

.chat-box::-webkit-scrollbar-thumb {
    background-color: rgba(0, 71, 123, 1); /* Color of the scrollbar thumb */
    border-radius: 4px; /* Roundness of the scrollbar thumb */
    border: 2px solid #f3f3f3; /* Padding around the thumb for better aesthetics */
}

.chat-box::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 71, 123, 0.8); /* Darken the thumb on hover */
}

.chat-box::-webkit-scrollbar-track {
    background-color: #f3f3f3; /* Color of the scrollbar track */
    border-radius: 4px; /* Roundness of the scrollbar track */
}
