<div class="table-container">
    <table class="data">
        <thead>
            <tr>
                <th>Document Name</th>
                <th>Date Uploaded</th>
                <th>Last Updated</th>
                <th>Owner</th>
            </tr>
        </thead>
    </table>
    <div class="table-body">
        <table class="data">
            <tbody id="document-table-body">
                <!-- Rows will be populated here -->
            </tbody>
        </table>
    </div>
</div>

.table-container {
    max-height: 400px; /* Set a fixed height for the table container */
    border: 1px solid rgba(0, 71, 123, 0.2); /* Optional: add a border around the table container */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Optional: add a shadow for better visibility */
    overflow: hidden; /* Hide overflow to contain scrolling */
}

.table-body {
    max-height: 350px; /* Adjust as needed */
    overflow-y: auto; /* Enable vertical scrolling */
}

.table-body::-webkit-scrollbar {
    width: 8px; /* Width of the scrollbar */
}

.table-body::-webkit-scrollbar-thumb {
    background-color: rgba(0, 71, 123, 0.8); /* Color of the scrollbar thumb */
    border-radius: 4px; /* Roundness of the scrollbar thumb */
}

.table-body::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 71, 123, 1); /* Color of the scrollbar thumb when hovered */
}

.table-body::-webkit-scrollbar-track {
    background-color: #f3f3f3; /* Color of the scrollbar track */
}
