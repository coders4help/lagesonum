$('#result').show();

// Submit post on submit
$('#query-form-new').on('submit', function(event){
    event.preventDefault();
    query_post();
});

function query_post() {
    $('#result').hide();
    $.ajax({
        type: 'POST', // http method
        timeout: 30,
        data: {
            csrfmiddlewaretoken: $('#query-form input[name=csrfmiddlewaretoken]').val(),
            number: $('#numberfield').val()
        }, // data sent with the post

        success: function(json) {
            $('#numberfield').val(''); // remove the value from input
            if (json.result) {
                res = $('#result');
                res.html(json.result);
                res.show();
            }
        },

        error: function(xhr, errmsg, err) {
            console.log('Error: ' + errmsg)
            console.log(xhr.status + ': ' + xhr.responseText)
            res = $('#result');
            res.html(errmsg);
            res.show();
        }
    });
}
