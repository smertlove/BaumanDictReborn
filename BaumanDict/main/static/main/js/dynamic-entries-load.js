"use strict";




function load_more_entries(ajaxURL, aHrefURL){
        let lastEntryIndex = $('#lastEntryIndexer').attr('count')
        let data = {
            lastEntryIndex: lastEntryIndex
        }
        $.ajax({
            method: "GET",
            dataType: "json",
            data: data,
            url: ajaxURL,
            success: function(data){
                $('#lastEntryIndexer').attr('count', data['count'])
                if(!data['moreEntries']){
                    $('#load-more-entries').css('display', 'none')
                }else{
                    $.each(data['data'], function(key, obj){
                        $('.allEntries').append(
                            '<a href="' +aHrefURL + '?word='+obj['word']+'&module='+obj['module']+'"'+
                             'class="btn btn-outline-primary dict-btn col-12 align-text-left">'+
                              "<b>"+obj['word']+"</b> - " + obj['translation'] +" (module"+ obj['module'] + ")"+
                            '</a>'
                        )
                    })
                }
            }
        })
    return null;
    }

