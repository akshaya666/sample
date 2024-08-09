<div class="table-container">
    <table class="data" id="table-header">
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
    max-height: 400px;
    border: 1px solid rgba(0, 71, 123, 0.2);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.table-container table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed; /* Ensures fixed table layout for alignment */
}

.table-body {
    max-height: 350px;
    overflow-y: auto;
}

.table-body::-webkit-scrollbar {
    width: 8px;
}

.table-body::-webkit-scrollbar-thumb {
    background-color: rgba(0, 71, 123, 0.8);
    border-radius: 4px;
}

.table-body::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 71, 123, 1);
}

.table-body::-webkit-scrollbar-track {
    background-color: #f3f3f3;
}

.data th, .data td {
    border: 1px solid rgba(0, 71, 123, 0.2);
    padding: 10px;
    text-align: left;
}

.data th {
    background-color: rgba(0, 71, 123, 0.1);
    position: sticky; /* Ensure the header remains sticky */
    top: 0; /* Stick it to the top of its container */
    z-index: 1;
}

.data td {
    white-space: nowrap; /* Prevent text wrapping for better alignment */
}
