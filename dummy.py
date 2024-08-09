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
        <tbody id="document-table-body">
            <!-- Rows will be populated here -->
        </tbody>
    </table>
</div>

.table-container {
    max-height: 400px;
    border: 1px solid rgba(0, 71, 123, 0.2);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow-y: auto;
    overflow-x: hidden;
}

.data {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed; /* Ensures fixed table layout for alignment */
}

.data th, .data td {
    border: 1px solid rgba(0, 71, 123, 0.2);
    padding: 10px;
    text-align: left;
}

.data th {
    background-color: rgba(0, 71, 123, 0.1);
    position: sticky; /* Sticky header */
    top: 0; /* Stick it to the top */
    z-index: 2; /* Ensure it stays above table body */
}

.data td {
    white-space: nowrap; /* Prevent text wrapping */
}

.table-container::-webkit-scrollbar {
    width: 8px;
}

.table-container::-webkit-scrollbar-thumb {
    background-color: rgba(0, 71, 123, 0.8);
    border-radius: 4px;
}

.table-container::-webkit-scrollbar-thumb:hover {
    background-color: rgba(0, 71, 123, 1);
}

.table-container::-webkit-scrollbar-track {
    background-color: #f3f3f3;
}

.flash-message {
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
}
