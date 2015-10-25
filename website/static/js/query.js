
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

function clickLanguageSelect(){
    // Taken from:
    // http://stackoverflow.com/questions/3846735/trigger-a-select-form-element-to-show-its-options-open-drop-down-options-list
    var element = $("select")[0],
        worked = false;
    if(document.createEvent) { // all browsers
        var e = document.createEvent("MouseEvents");
        e.initMouseEvent("mousedown", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        worked = element.dispatchEvent(e);
    } else if (element.fireEvent) { // ie
        worked = element.fireEvent("onmousedown");
    }
}

$('document').ready(function(){
    $('#result').show();

    // Submit post on submit
    $('#query-form-new').on('submit', function(event){
        event.preventDefault();
        query_post();
    });

    // Submit post on submit

    $('#setlang-form').on('change', function(){
        $('#setlang-form').submit();
    });

    var nav = responsiveNav(".nav-collapse", { // Selector
        animate: true, // Boolean: Use CSS3 transitions, true or false
        transition: 284, // Integer: Speed of the transition, in milliseconds
        insert: "before", // String: Insert the toggle before or after the navigation
        customToggle: "nav-trigger", // Selector: Specify the ID of a custom toggle
        closeOnNavClick: false, // Boolean: Close the navigation when one of the links are clicked
        openPos: "relative", // String: Position of the opened nav, relative or static
        navClass: "nav-collapse", // String: Default CSS class. If changed, you need to edit the CSS too!
        navActiveClass: "js-nav-active", // String: Class that is added to  element when nav is active
        jsClass: "js", // String: 'JS enabled' class which is added to  element
        init: function(){}, // Function: Init callback
        open: function(){}, // Function: Open callback
        close: function(){} // Function: Close callback
    });
});

