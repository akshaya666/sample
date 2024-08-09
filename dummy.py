<div class="table-container">
    <div id="table-loader" class="table-loader">
        <div class="dot-loader"><div></div><div></div><div></div></div>
        <p>Loading data...</p>
    </div>
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

function loadDocuments() {
    const tableLoader = $('#table-loader');
    tableLoader.show(); // Show loader when loading starts

    $.get('/api/documents', function(data) {
        const tableBody = $('#document-table-body');
        tableBody.empty();
        data.forEach(doc => {
            const row = $('<tr>');
            row.append($('<td>').text(doc['Document Name']));
            row.append($('<td>').text(doc['Date Uploaded']));
            row.append($('<td>').text(doc['Last Updated']));
            row.append($('<td>').text(doc['Owner']));
            tableBody.append(row);
        });
    }).always(function() {
        tableLoader.hide(); // Hide loader when loading ends
    });
}

.table-loader {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.8);
    z-index: 10;
}

.dot-loader {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 24px;
    margin-bottom: 10px;
}

.dot-loader div {
    width: 8px;
    height: 8px;
    background-color: rgba(0, 71, 123, 1);
    border-radius: 50%;
    margin: 0 2px;
    animation: dot-loader 1.4s infinite ease-in-out both;
}

.dot-loader div:nth-child(1) {
    animation-delay: -0.32s;
}

.dot-loader div:nth-child(2) {
    animation-delay: -0.16s;
}

@keyframes dot-loader {
    0%, 80%, 100% {
        transform: scale(0);
    }
    40% {
        transform: scale(1);
    }
}

.table-loader p {
    font-size: 16px;
    color: rgba(0, 71, 123, 1);
}
