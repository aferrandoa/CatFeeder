$(document).ready(function() {
    refresh_jobs();

    $('.timepicker').timepicker({
        timeFormat: 'HH:mm',
        interval: 15,
        minTime: '00:00',
        maxTime: '23:30',
        defaultTime: '11',
        startTime: '00:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});

$('#open_button').click(function() {
    $.get({url: ($(this).attr('value')), success: function(result){}
    });
});

$('#close_button').click(function() {
    $.get({url: ($(this).attr('value')), success: function(result){}
    });
});

$('#remove_job_button').click(function() {
    var $table = $('#jobs_table')
    var selections = $table.bootstrapTable('getSelections')

    if(selections.length == 0){
        alert("No row selected")
        return;
    }

    var params = {job_id: selections[0].id}

    $.get({url: ($(this).attr('value')), data: params, success: function(result){
        refresh_jobs();
    }
    });
});

function add_job(){

    var job_name=$("#jobNameInput").val();
    var hour=$("#jobTimeInput").val().split(':')[0];
    var minute=$("#jobTimeInput").val().split(':')[1];

    var params={job_name: job_name, hour: hour, minute: minute};

    $.get({url: ($('#add_job_button').attr('value')), data: params, success: function(result){
        refresh_jobs();
    }
    });
};

function refresh_jobs(){
    $.get({url: ($('#get_jobs').attr('value')), success: function(result) {
        var $table = $('#jobs_table')
        $table.bootstrapTable('destroy').bootstrapTable({data: result})
        }
    });
};
