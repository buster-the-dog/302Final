$(document).ready(function() {
    $('#players').DataTable( {
        "order": [[2, "asc"]],
        "scrollX": true,
        "scrollY": 500,
    }
    );
    $('.dataTables_length').addClass('bs-select');
});

$('[data-toggle="tooltip"]').tooltip();

