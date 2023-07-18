function listTensesIT(moodValue, tenses, it) {
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

function listTensesES(moodValue, tenses, es) {
    if ($('.moods-and-tenses.spanish')) {
      if (moodValue == 'Indicativo') {
        es.Indicativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Subjuntivo') {
        es.Subjuntivo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Imperativo, Condicional') {
        es.Imperativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        es.Condicional_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Infinitivo, Gerundio, Participo') {
          tenses += "<div class='tense'>Infinitivo Infinitivo</div>";
          tenses += "<div class='tense'>Gerundio Gerondio</div>";
          tenses += "<div class='tense'>Participo Participo</div>";
        return tenses;
      }
    }
  }

function listTensesES(moodValue, tenses, pt) {
    if ($('.moods-and-tenses.portuguese')) {
      if (moodValue == 'Indicativo') {
        pt.Indicativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Conjuntivo') {
        pt.Conjuntivo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Condicional, Imperativo') {
        pt.Imperativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        pt.Condicional_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Infinitivo, Gerundio, Participo') {
          pt.Infinitivo_pessoal_tenses.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          tenses += "<div class='tense'>Infinitivo Infinitivo</div>";
          tenses += "<div class='tense'>Gerúndio Gerúndio</div>";
          tenses += "<div class='tense'>Particípio</div>";
        return tenses;
      }
    }
  }

function listTensesES(moodValue, tenses, ro) {
    if ($('.moods-and-tenses.portuguese')) {
      if (moodValue == 'Indicativo') {
        ro.Indicativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Conjuntivo') {
        ro.Conjuntivo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Condicional, Imperativo') {
        ro.Imperativo_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        ro.Condicional_tenses.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        return tenses;
      }

      if (moodValue == 'Infinitivo, Gerundio, Participo') {
          ro.Infinitivo_pessoal_tenses.forEach(function(tense) {
            tenses += "<div class='tense'>" + tense + "</div>";
          });
          tenses += "<div class='tense'>Infinitivo Infinitivo</div>";
          tenses += "<div class='tense'>Gerúndio Gerúndio</div>";
          tenses += "<div class='tense'>Particípio</div>";
        return tenses;
      }
    }
  }




  // NOT FINISHED !
  function listTensesIT(moodValue, tenses, fr) {
    if ($('.moods-and-tenses.italian')) {
      if (moodValue == 'Indicativo') {
        fr.indicativo_tenses_simple.forEach(function(tense) {
          tenses += "<div class='tense'>" + tense + "</div>";
        });
        fr.indicativo_tenses_complex.forEach(function(tense) {
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