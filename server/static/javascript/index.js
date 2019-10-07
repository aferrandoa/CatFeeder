$('#open_button').click(function() {
    $.ajax({url: ($(this).attr('value')), success: function(result){}
    });
});

$('#close_button').click(function() {
    $.ajax({url: ($(this).attr('value')), success: function(result){}
    });
});