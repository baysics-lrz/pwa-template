/**
 * Fetches information about a observation
 * @param modus {String}    The modus of the lexicon {'category2', 'category4', 'category1', 'category3'}
 * @param subject {String}  The searched subject
 * @returns {Promise<*>}    A Promise with the data fetch for the lexicon
 */
function fetchLexiconData(modus, subject) {
    let urlPath = `/api/lexicon/${modus}?SubjectName=${subject}`
    return fetch(urlPath).then(function (response) {
        return response.json();
    }).then(function (jsonData) {
        return jsonData;
    })
}


function convertListToHTML(list, tag) {
    let result = ''
    if (tag === 'p') {
        for (let entry of list) {
            result += `<p>${entry}</p>`
        }
        return result
    } else if (tag === 'li') {
        result += '<ul>'
        for (let entry of list) {
            result += `<li>${entry}</li>`
        }
        result += '</ul>'
        return result
    }
}

function makePhotoCarousellHTML(photo_list) {
    if (photo_list.length === 0) {
        return ''
    }
    let result = '<style>.carousel-control-prev-icon {width: 40px;height: 40px;'
    result += `background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%24435a' width='8' height='8' viewBox='0 0 8 8'%3e%3cpath d='M5.25 0l-4 4 4 4 1.5-1.5L4.25 4l2.5-2.5L5.25 0z'/%3e%3c/svg%3e");}`
    result +=`.carousel-control-next-icon {width: 40px;height: 40px;background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%24435a' width='8' height='8' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5L3.75 4l-2.5 2.5L2.75 8l4-4-4-4z'/%3e%3c/svg%3e");}`
    result +=`</style><div id="carouselExampleIndicatorsLexicon" class="carousel slide">`

    result += '<div class="carousel-inner">'
    let i=0
    for (let photo of photo_list) {
        // Create active item if it is the first one
        if (i==0){
            result += '<div class="carousel-item active" style="position: relative;padding-bottom: 56.25%;">'
        }
        else {
            result += '<div class="carousel-item" style="position: relative;padding-bottom: 56.25%;">'
        }
        result += `<img class="d-block w-100" style="position: absolute;width: 100%;height: 100%; object-fit: contain" src="/static/${photo.Url}" alt="">`
        if (photo.Cite) {
            result += `<div style="position: absolute;bottom: 0;width: 100%;height: 1.5rem;text-align: right;color: var(--darkblue);text-shadow: 0 0 5px white;padding-right: 5px;"><i>Source: ${photo.Cite}</i></div>`
        }
        result += '</div>'
        i=i+1
    }
    // If there are more than 2 photos make prev and next icons
    if (i>1){
        result += '<a class="carousel-control-prev" href="#carouselExampleIndicatorsLexicon" role="button" data-slide="prev">'
        result += '<span class="carousel-control-prev-icon" aria-hidden="true"></span>'
        result += '<span class="sr-only">Previous</span>'
        result += '</a>'
        result += '<a class="carousel-control-next" href="#carouselExampleIndicatorsLexicon" role="button" data-slide="next">'
        result += '<span class="carousel-control-next-icon" aria-hidden="true"></span>'
        result += '<span class="sr-only">Next</span>'
        result += '</a>'
    }
    result += '</div>'
    return result


}


