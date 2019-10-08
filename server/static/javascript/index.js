$(document).ready(function() {
    refresh_jobs();
});

$('#open_button').click(function() {
    $.ajax({url: ($(this).attr('value')), success: function(result){}
    });
});

$('#close_button').click(function() {
    $.ajax({url: ($(this).attr('value')), success: function(result){}
    });
});

$('#add_job_button').click(function() {
    $.ajax({url: ($(this).attr('value')), success: function(result){
            refresh_jobs();
        }
    });
});

function refresh_jobs(){
    $.ajax({url: ($('#get_jobs').attr('value')), success: function(result) {
        //alert(result.name + " -> " + result.id);
        $('#jobs_list').html("<p>" + result.id + " -> " + result.name + "</p>");
        }
    });
};
