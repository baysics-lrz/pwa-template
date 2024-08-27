$(document).ready(function () {
    $('#faq-table thead tr:eq(1) th').each(function (i) {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="' + title + '" />');

        $('input', this).on('keyup change', function () {
            if (table.column(i).search() !== this.value) {
                table
                .column(i)
                .search(this.value)
                .draw();
            }
        });
    });

    var table = $('#faq-table').dataTable({
        orderCellsTop: true,
        pageLength: 20,
        fixedHeader: true,
        responsive: true,
        language: {
           "lengthMenu": "Show _MENU_ entries per page",
           "zeroRecords": "No entries could be found - try another search.",
           "info": "Show page _PAGE_ from _PAGES_",
           "infoEmpty": "No entries available",
           "infoFiltered": "(filtered from total _MAX_ entries)",
           "emptyTable": "There are no entries in this table",
           "info": "Show _START_ from _END_ from total _TOTAL_ entries",
           "infoEmpty": "Show 0 from 0 from total 0 entries",
           "loadingRecords": "loading...",
           "processing": "processing...",
           "search": "<b>Search:</b>",
           "paginate": {
             "first": "first",
             "last": "last",
             "next": "next",
             "previous": "previous"
           },
           "aria": {
             "sortAscending": ": Ascending order",
             "sortDescending": ": Descending order"
           }
        }

    });
});