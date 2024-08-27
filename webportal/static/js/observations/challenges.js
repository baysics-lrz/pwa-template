$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

function count() {
   var x = []
    x.sort();

    var current = null;
    var cnt = 0;
    for (var i = 0; i < x.length; i++) {
        if (x[i] != current) {
            if (cnt > 0) {
                document.write(current + ' comes --> ' + cnt + ' times<br>');
            }
            current = x[i];
            cnt = 1;
        } else {
            cnt++;
        }
    }
    if (cnt > 0) {
        document.write(current + ' comes --> ' + cnt + ' times');
    }

}

count();

var category1count = 0
{% if category1_list %}
{% for category1 in category1_list %}
    category1count += 1
{% endfor %}
{% endif %}
console.log(category1count)

var category2count = 0
{% if category2_list %}
{% for category2 in category2_list %}
    category2count += 1
{% endfor %}
{% endif %}
console.log(category2count)

var category3count = 0
{% if category3_list %}
{% for category3 in category3_list %}
    console.log(category3)
    category3count += 1
{% endfor %}
{% endif %}
console.log(category3count)

var category4count = 0
{% if category4_list %}
{% for category4 in category4_list %}
    category4count += 1
{% endfor %}
{% endif %}
console.log(category4count)
