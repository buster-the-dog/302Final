$(document).ready(function() {
    $('#players').DataTable( {
        "order": [[3, "asc"]],
        "scrollX": true,
        "scrollY": 500,
    }
    );
    $('.dataTables_length').addClass('bs-select');
});