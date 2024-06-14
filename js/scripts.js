$(document).ready(function () {
    // Fetch all data
    $('#fetchData').click(function () {
        $.ajax({
            url: 'http://127.0.0.1:5000/api/earthquakes', // Ubah URL di sini
            method: 'GET',
            success: function (data) {
                displayData(data, '#earthquakeList');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    // Search data with filters
    $('#searchButton').click(function () {
        const magnitude = $('#magnitude').val();
        const depth = $('#depth').val();
        const potential = $('#potential').val();
        const filters = {};

        if (magnitude) filters.magnitude = magnitude;
        if (depth) filters.depth = depth;
        if (potential) filters.potential = potential;

        $.ajax({
            url: 'http://127.0.0.1:5000/api/earthquakes', // Ubah URL di sini
            method: 'GET',
            success: function (data) {
                const filteredData = data.filter(earthquake => {
                    return (!filters.magnitude || earthquake.Magnitude >= filters.magnitude) &&
                        (!filters.depth || earthquake.Kedalaman <= filters.depth) &&
                        (!filters.potential || earthquake.Potensi === filters.potential);
                });
                displayData(filteredData, '#searchResults');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    function displayData(data, container) {
        const $container = $(container);
        $container.empty();
        if (data.length === 0) {
            $container.append('<p>No data found.</p>');
            return;
        }

        data.forEach(earthquake => {
            $container.append(
                `<div class="list-group-item">
                    <h5>${earthquake.Tanggal} - ${earthquake.Wilayah}</h5>
                    <p>Magnitude: ${earthquake.Magnitude}</p>
                    <p>Depth: ${earthquake.Kedalaman} km</p>
                    <p>Potential: ${earthquake.Potensi}</p>
                </div>`
            );
        });
    }
});
