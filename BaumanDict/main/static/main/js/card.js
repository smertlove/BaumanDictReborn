'use strict';

var rotated = false;
var side1;
var side2;

function getCard(ajaxURL){
    $.ajax({
    method: "GET",
    url: ajaxURL,
    success: function(data){
        side1 = data['side1']
        side2 = data['side2']
        console.log(side1, side2)
        if(rotated){
            flip()
        }else{
            document.getElementById('myCardContent').innerText = side2;
        }

    }
})
}




function flip(){
    document.getElementById("flipper").classList.toggle("flip");
    if(rotated){
        rotated = false;

        setTimeout(function (){document.getElementById('myCardContent').innerText = side2;}, 250)

    }else{
        rotated = true;
        setTimeout(function (){document.getElementById('myCardContent').innerText = side1;}, 250)
    }
}

$('#flipper').on('click', function(){flip()})
