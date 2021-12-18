'use strict';



var allowed_modules = [];


var CSStoggleON = {'backgroundColor': '#689CD3'};

var CSStoggleOFF = {'backgroundColor': ''};


function deleteElem(arr, elem) {
    let i = arr.indexOf(elem);
    if (i !== -1) {
        arr.splice(i, 1);
        return arr;
    }
    return arr;
}

function insertElem(arr, elem) {
    let i = arr.indexOf(elem);
    if (i === -1) {
        arr.push(elem);

    }
    return arr;
}

function steroidRStrip(str, pattern){
    let ind = str.lastIndexOf(pattern);
    return str.substr(0, ind);
}

function changeBtnsHrefs(){
    $.each($('.get-task'), function (){
        let cur = $(this)
        cur.attr('href', steroidRStrip(cur.attr('href'), '&') + '&modules=' + allowed_modules.join(';'))
    })
}

$('.module-filter').on('click', function(){
    var cur = $(this);
    if(cur.attr('toggled') == 'false'){
        cur.attr('toggled', 'true');
        cur.css(CSStoggleON);
        allowed_modules = insertElem(allowed_modules, cur.text());
        console.log(cur.attr('href'))

    }else{
        cur.attr('toggled', 'false');
        cur.css(CSStoggleOFF);
        allowed_modules = deleteElem(allowed_modules, cur.text());

    }
    changeBtnsHrefs();

})






