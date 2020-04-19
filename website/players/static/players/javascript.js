$(document).ready(function() {
    $('#players').DataTable( {
        "ordering": true,
        "scrollX": true,
        "scrollY": 500
    }
    );
    $('.dataTables_length').addClass('bs-select');
});