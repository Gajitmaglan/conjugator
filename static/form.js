$(document).ready(function() {
  $(document).on('click', '.mood', function() {
    if ( $(".mood").hasClass("selected") ) {
      $(".mood").removeClass("selected")
    }
    $(this).addClass("selected");
    console.log("mood selected")

    let tenses = '';
    let moodValue = $(this).text()

    $(".tenses").html(listTenses(moodValue, tenses, it));

    function listTenses(moodValue, tenses, it) {
      if ($('.moods-and-tenses.italian')) {
        if (moodValue == 'Indicativo') {
          it.indicativo_tenses_simple.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          it.indicativo_tenses_complex.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          return tenses;
        }

        if (moodValue == 'Congiuntivo') {
          it.congiuntivo_tenses_simple.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          it.congiuntivo_tenses_complex.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          return tenses;
        }

        if (moodValue == 'Condizionale, Imperativo') {
          it.conditionale_tenses.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          it.imperativo_tenses.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          return tenses;
        }

        if (moodValue == 'infinito, participio') {
            tenses += "<div class='tense'>Infinito  Gerundio</div>";
            tenses += "<div class='tense'>Participio Participio</div>";
          return tenses;
        }
      }
    }
  })
  // hieghlight the mood as selected
  $(document).on('click', '.tense', function() {
    if ( $(".tense").hasClass("selected") ) {
      $(".tense").removeClass("selected")
    }
    $(this).addClass("selected");
    console.log("tense selected")
  })


    $("div[data-lvl]").click(function() {
      var dataLvlNumber = $(this).attr("data-lvl");
      var language = window.location.pathname.split('/')[1]; // Extract the language from the URL
      var url;
      if (language === 'it') {
        url = '/it/selected/';
      } else if (language === 'pt') {
        url = '/pt/selected/';
      } else if (language === 'es') {
        url = '/es/selected/';
      } else if (language === 'fr') {
        url = '/fr/selected/';
      } else if (language === 'ro') {
        url = '/ro/selected/';
      }
      selected_mood = $(".mood.selected").text();
      selected_tense = $(".tense.selected").text();
      // /it/<string:mood>_and_<string:tense>_for_level_<int:lvl_nr>/
      window.location.href = selected_mood +'_'+ selected_tense +'_for_'+ dataLvlNumber + "/";
    });

    // Variable to keep track of whether the input is focused or not
    var inputFocused = false;
  
    // Event handler for when the input is focused
    $('#verb').on('focus', function() {
      inputFocused = true;
      displayResults('');
    });
  
    $('#verb').on('blur', function() {
      inputFocused = false;
      setTimeout(function() {
        if (!inputFocused) {
          displayResults('');
        }
      }, 200);
    });
  
    $(document).on('click', '.result', function() {
      var resultText = $(this).text();
      $('#verb').val(resultText);
      displayResults('');
    });
  
    $('#verb').on('input', function() {
      var query = $(this).val();

      var language = window.location.pathname.split('/')[1]; // Extract the language from the URL

      var url;
      if (language === 'it') {
        url = '/it/search/';
      } else if (language === 'pt') {
        url = '/pt/search/';
      } else if (language === 'es') {
        url = '/es/search/';
      } else if (language === 'fr') {
        url = '/fr/search/';
      } else if (language === 'ro') {
        url = '/ro/search/';
      }
  
      $.ajax({
        url: url, // Replace with your server-side search endpoint
        method: 'GET',
        data: { query: query },
        success: function(results) {
          // Only display the results if the input is focused
          if (inputFocused) {
            displayResults(results);
          }
        },
        error: function(error) {
          console.log(error);
        }
      });
    });



  });
  
  function displayResults(results) {
    var searchResults = $('#search-results');
  
    // Clear previous results
    searchResults.empty();
  
    // Display the new results
    for (var i = 0; i < results.length; i++) {
      searchResults.append('<div class="result">' + results[i] + '</div>');
    }
  }