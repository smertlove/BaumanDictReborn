"use strict";


function clearPreviouslySuggestedElements() {
    let mySuggestions = document.getElementById("mySuggestions");
    let previouslySuggestedElements = mySuggestions.childNodes;
    for (; previouslySuggestedElements.length > 0;) {
        mySuggestions.removeChild(previouslySuggestedElements[0]);
    }
}


function liveSearch(ajaxURL, aHrefURL, pattern){

        $.ajax({
            method: "GET",
            dataType: "json",
            data: {pattern: pattern},
            url: ajaxURL,
            success: function (data) {
                clearPreviouslySuggestedElements();
                if (data['data'].length == 0 && pattern.length>1) {
                    $('#mySuggestions').append(
                        '<p style="margin-left: 5px">nothing found</p>'
                    )
                } else {
                    $.each(data['data'], function (key, obj) {
                        let link = document.createElement('a');
                        link.className = 'suggestin-link';

                        link.href = aHrefURL + "?word=" + obj['word'] + '&module=' + obj['module'];
                        link.innerText = obj['word'];
                        $('#mySuggestions').append(
                            link
                        )
                    })

                }
            }

        })
    return null;
}



document.getElementById('myInput').onclick = clearPreviouslySuggestedElements;
    $('body').on('click', function(e){
        if( e.target != document.getElementById('myInput') ) {
		clearPreviouslySuggestedElements();
		document.getElementById("myInput").value = "";
        }
    });