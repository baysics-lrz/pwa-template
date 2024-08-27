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
        'targets': [6,7], /* column index */
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

                console.log("test:" + table.$('tr.selected').attr('class'));
                //alert('Detail' + id);
                if (table.$('tr.selected').attr('class').includes('category1')) {
                    console.log('DetailC1' + id);
                    displayDetailSubject('DetailC1' + id);

                } else if (table.$('tr.selected').attr('class').includes('category2')) {
                    console.log('DetailC2' + id);
                    displayDetailSubject('DetailC2' + id);

                } else if (table.$('tr.selected').attr('class').includes('category3')) {
                    console.log('DetailC3' + id);
                    displayDetailSubject('DetailC3' + id);

                } else if (table.$('tr.selected').attr('class').includes('category4')) {
                    console.log('DetailC4' + id);
                    displayDetailSubject('DetailC4' + id);

                } else {
                    console.log('something went wrong');
                }


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