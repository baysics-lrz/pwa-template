$(document).ready(function() {
        $.fn.dataTable.moment('D.M.YYYY');
        var table = $('#Entries').DataTable({
        "language": {
          "emptyTable": "There are no entries available"
        },
        "paging":   false,
        "searching": false,
        "info":     false,
        "order": [[1, "desc" ]],
        'columnDefs': [
            {
            'targets': [7,8], /* column index */
            'orderable': false, /* true or false */
        },
            { type: 'title-numeric', targets: 0 }
        ]
        });
        if ($(window).width() > 560) {
            $('#Entries tbody').on('click', 'tr', function () {
                if ($(this).hasClass('selected')) {
                    $(this).removeClass('selected');
                    displayDetailSubject('nichts');
                    document.getElementById('emptyphoto').style.display = "block";
                } else {
                    table.$('tr.selected').removeClass('selected');
                    $(this).addClass('selected');
                    var id = $(this).children('td').first().children('span').first().html();
                    displayDetailSubject('Detail' + id);
                }
            });
        }
    } );

    var matches = document.querySelectorAll("td");
    for(var index in matches) {
        if (matches[index].textContent === " None") {
            matches[index].textContent = "-";
        }
    }



