"use strict";


var answer;

function getTask(ajaxURL, data){
    $.ajax({
    method: "GET",
    dataType: "json",
        data: data,
    url: ajaxURL,
    success: function(data){
        $('#exercise').empty().append(data['task']);
        answer = data['answer']
    }
})
}






function checkAnsw (){

    if ( answer.includes($('#answer').val()) ) {
        alert('Great!');
    } else {
        alert('Wrong answer.\nCorrect: ' + answer)

    }

    $('#answForm')[0].reset();
}