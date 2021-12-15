'use strict';




var answer;

function getTask(ajaxURL, data){
    $.ajax({
    method: "GET",
    dataType: "json",
        data: data,
    url: ajaxURL,
    success: function(data){
        $('#exercise').empty().append(data['task']);
        let btns = document.getElementsByClassName('submitAnsw');
        for (let i = 0; i<4; i++){
            let btn = btns[i]
            btn.innerText = data['answs'][i];
        }
        answer = data['right_answ'];
        console.log(data['lang']);
    }
})
}








