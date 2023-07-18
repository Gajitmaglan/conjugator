$(document).ready(function() {
    var language = window.location.pathname.split('/')[1];
    console.log("from a .js file: " + verb_sequence);
  
    
    $("button").click(function(event) {
      event.preventDefault(); // Prevent the default form submission
        
      let verb_id = verb_sequence[0];
      verb_sequence.shift();
      if(verb_sequence[0]) {
          var url = '/' + language + '/next_verb:_' + verb_id + '/';
          $.ajax({
            url: url,
            method: 'GET',
            contentType: 'application/json', // Set the Content-Type header
            data: JSON.stringify({ verb_id: verb_id }),
            success: function(next_verb) {
              console.log("next verb: ", next_verb);
            },
            error: function(error) {
              console.log(error);
            }
          });
      } else {
        $("button").text("Finish!")
      }
    });
  });
  