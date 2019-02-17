jQuery(function($, undefined) {
    $('#terminal').terminal(function(command) {
        if (command !== '') {
              $.ajax({
                  type:"POST",
                  url: "comando",
                  data:{"command": command},
                  dataType: 'json',
                  success: function(data) {
                    console.log(data);
                  },
                  error: function (request, status, error) {
                    console.log(request.responseText);
                  }
               })
        } else {
           this.echo('');
        }
    }, {
        greetings: 'RaspXbee Interpreter',
        name: 'js_demo',
        height: 500,
        prompt: 'Xbee> '
    });
});
