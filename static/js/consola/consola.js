jQuery(function($, undefined) {
    $('#terminal').terminal(function(command) {
        if (command !== '') {
          var this_terminal = this
          try {
            var response = '';
             $.ajax({
                type:"GET",
                url: command,
                data:{"command": command},
                dataType: 'json',
                success: function(data) {
                  this_terminal.echo("--> DataFrame <-- ")
                  this_terminal.echo(data.df)
                  this_terminal.echo("--> Score: <-- ")
                  this_terminal.echo(data.score)
                  console.log(data);
                },
                error: function (request, status, error) {
                  console.log(request);
                }
             })
             console.log(response);
          } catch(e) {
            this.error(new String(e));
          }
        } else {
           this.echo('-->Error: comando disponibles:');
           this.echo('-->load_data');
        }
    }, {
        greetings: 'RaspXbee Interpreter',
        name: 'js_demo',
        height: 500,
        prompt: 'Xbee> '
    });
});
