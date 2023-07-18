#==============================================================================
#============================= P O R T U G U E S E ============================

pt = {
    "interface_language": "pt",

    "form": {"filler": "Digite um verbo...",
             "button": "conjugar"},

    "person": ('eu', 'nós', 'tu', 'vós', 'ele', 'eles'),
    "person_sp": {'1s','2s','3s','1p', '2p', '3p'},

    "tenseTypesPT": (
        'Indicativo', 'Conjuntivo', 'Condicional',
        'Infinitivo', 'Gerúndio', 'Imperativo',
        'Particípio'
    ),

    "Indicativo_tenses": (
        'Indicativo presente', 'Indicativo pretérito perfeito simples',
        'Indicativo Pretérito Perfeito Composto',
        'Indicativo pretérito imperfeito',
        'Indicativo Pretérito Mais que Perfeito Composto', 
        'Indicativo Pretérito Mais que Perfeito Simples',
        'Indicativo Pretérito Mais que Perfeito Anterior',
        'Indicativo Futuro do Presente Simples',
        'Indicativo Futuro do Presente Composto'
    ),

    "Conjuntivo_tenses": (
        'Conjuntivo  Subjuntivo Presente',
        'Conjuntivo  Subjuntivo Pretérito Perfeito',
        'Conjuntivo  Subjuntivo Pretérito Imperfeito',
        'Conjuntivo  Subjuntivo Pretérito Mais que Perfeito',
        'Conjuntivo  Subjuntivo Futuro Simples',
        'Conjuntivo  Subjuntivo Futuro Composto',
    ),

    "Condicional_tenses": (
        'Condicional Futuro do Pretérito Simples',
        'Condicional Futuro do Pretérito Composto'
    ),

    "Infinitivo_pessoal_tenses": (
        'Infinitivo Pessoal Presente',
        'Infinitivo Pessoal Pretérito'
    ),

    "Infinitivo": (
        'Infinitivo Infinitivo', # 0 or 1
    ),

    "Gerúndio": (
        'Gerúndio Gerúndio', # 0 or 1
    ),

    #           for these person_sp
    "Imperativo_tenses": (
        'Imperativo Afirmativo',
        'Imperativo Negativo'
    ),

    "Particípio": "Particípio"
}

def clarifyOutputPt(p, tense):
#                    I N D I C A T I V O                         #
    indicativo_pretérito_perfeito_composto = {'eu': 'tenho', 'nós': 'temos', 'tu':'tem',
            'vós':'tendes', 'ele':'tem', 'eles':'têm'}
    
    indicativo_pretérito_mais_que_perfeito_composto = {'eu': 'tinha', 'nós': 'tínhamos', 'tu':'tinhas',
              'vós':'tínheis', 'ele':'tinha', 'eles':'tinham'}
    
    indicativo_futuro_do_presente_composto = {'eu': 'terei', 'nós': 'teremos', 'tu':'terás',
              'vós':'tereis', 'ele':'terá', 'eles':'terão'}
    
    indicativo_preterito_mais_que_perfeito_anterior = {'eu': 'tivera', 'nós': 'tivéramos', 'tu':'tiveras',
              'vós':'tivéreis', 'ele':'tivera', 'eles':'tiveram'}
    
    if tense == 'Indicativo Pretérito Perfeito Composto':
        return f"{p} {indicativo_pretérito_perfeito_composto.get(p)}"
    elif tense == 'Indicativo Pretérito Mais que Perfeito Composto':
        return f"{p} {indicativo_pretérito_mais_que_perfeito_composto.get(p)}"
    elif tense == 'Indicativo Futuro do Presente Composto':
        return f"{p} {indicativo_futuro_do_presente_composto.get(p)}"
    elif tense == 'Indicativo Pretérito Mais que Perfeito Anterior':
        return f"{p} {indicativo_preterito_mais_que_perfeito_anterior.get(p)}"
    
#                      C O N J U N T I V O                      #
    
    conjuntivo_subjuntivo_pretérito_perfeito = {'eu': 'tenha', 'nós': 'tenhamos', 'tu':'tenhas',
              'vós':'tenhais', 'ele':'tenha', 'eles':'stenham'}
    
    conjuntivo_subjuntivo_pretérito_mais_que_perfeito = {'eu': 'tivesse', 'nós': 'tivéssemos', 'tu':'tivesses',
                'vós':'tivésseis', 'ele':'tivesse', 'eles':'tivessem'}
    
    conjuntivo_subjuntivo_futuro_composto = {'eu': 'tiver', 'nós': 'tivermos', 'tu':'tiveres',
                'vós':'tiverdes', 'ele':'tiver', 'eles':'tiverem'}
    
    if tense == 'Conjuntivo  Subjuntivo Presente':
        return f"que {p}"
    elif tense == 'Conjuntivo  Subjuntivo Pretérito Perfeito':
        return f"{p} {conjuntivo_subjuntivo_pretérito_perfeito.get(p)}"
    elif tense == 'Conjuntivo  Subjuntivo Pretérito Imperfeito':
        return f"se {p}"
    elif tense == 'Conjuntivo  Subjuntivo Pretérito Mais que Perfeito':
        return f"{p} {conjuntivo_subjuntivo_pretérito_mais_que_perfeito.get(p)}"
    elif tense == 'Conjuntivo  Subjuntivo Futuro Simples':
        return f"quando {p}"
    elif tense == 'Conjuntivo  Subjuntivo Futuro Composto':
        return f"{p} {conjuntivo_subjuntivo_futuro_composto.get(p)}"
    
#                      C O N D I C I O N A L                      #
    
    condicional_futuro_do_pretérito_composto = {'eu': 'teria', 'nós': 'teríamos', 'tu':'terias',
                'vós':'teríeis', 'ele':'teria', 'eles':'teriam'}

    if tense == 'Condicional Futuro do Pretérito Composto':
        return f"{p} {condicional_futuro_do_pretérito_composto.get(p)}"

#==============================================================================
#============================= F R E N C H ====================================

fr = {
    #              F O R M ---------------------------------------

    "person": ('je', 'tu', 'il (elle, on)', 'nous', 'vous', 'ils (elles)'),

    "indicative_tenses": (
        # 'Infinitif Présent',
        'Présent',
        'Imparfait',
        'Futur',
        'Passé Simple',
    ),

    "conditional": 'Présent',
    "conditional_complex": {
        'Conditionnel Passé première forme',
        'Conditionnel Passé deuxième forme'
    },
    "subjunctive": {
        'Présent',
        'Imparfait'
    },
    "subjunctive_complex": {
        'Subjonctif Plus-que-parfait', # complex
        'Subjonctif Passé' # complex
    },

    "imperative": 'Imperatif Présent', # no pronoun ''

    "participle_present": 'Participe Présent',

    "participle_past_m": (
        'Participe Passé', # 'masculin singulier'
        'Participe Passé'  # 'masculin pluriel'
    ),

    "participle_past_f": (
        'Participe Passé', # 'feminin singulier'
        'Participe Passé'  # 'feminin pluriel'
    )
}

def clarify_output_fr_etre(p, tense):
#                   I N D I C A T I F                         #
    indicatif_passe_compose = {
        'je': 'suis',
        'tu': 'es',
        'il': 'est',
        'elle': 'est',
        'nous': 'sommes',
        'vous': 'êtes',
        'ils': 'sont',
        'elles': 'sont'
    }
    indicatif_plus_que_parfait = {
        'je': 'étais',
        'tu': 'étais',
        'il': 'était',
        'elle': 'était',
        'nous': 'étions',
        'vous': 'étiez',
        'ils': 'étaient',
        'elles': 'étaient'
    }
    indicatif_passe_anterieur = {
        "je": "fus",
        "tu": "fus",
        "il": "fut",
        "elle": "fut",
        "nous": "fûmes",
        "vous": "fûtes",
        "ils": "furent",
        "elles": "furent"
    }
    indicatif_futur_anterieur = {
        "je": "serai",
        "tu": "seras",
        "il": "sera",
        "elle": "sera",
        "nous": "serons",
        "vous": "serez",
        "ils": "seront",
        "elles": "seront"
    }
    
    if tense == 'Indicatif Passé composé':
        return f"{p} {indicatif_passe_compose.get(p)}"
    elif tense == 'Indicatif Plus-que-parfait':
        return f"{p} {indicatif_plus_que_parfait.get(p)}"
    elif tense == 'Indicatif Passé antérieur':
        return f"{p} {indicatif_passe_anterieur.get(p)}"
    elif tense == 'Indicatif Futur antérieur':
        return f"{p} {indicatif_futur_anterieur.get(p)}"

#                   S U B J O N C T I F                        #
    
    subjonctif_plus_que_parfait = {
        "je": "fusse",
        "tu": "fusses",
        "il": "fût",
        "elle": "fût",
        "nous": "fussions",
        "vous": "fussiez",
        "ils": "fussent",
        "elles": "fussent"
    }

    subjonctif_passe = {
        "je": "sois",
        "tu": "sois",
        "il": "soit",
        "elle": "soit",
        "nous": "soyons",
        "vous": "soyez",
        "ils": "soient",
        "elles": "soient"
    }

    if tense == 'Subjonctif Plus-que-parfait':
        return f"{p} {subjonctif_plus_que_parfait.get(p)}"
    elif tense == 'Subjonctif Passé':
        return f"{p} {subjonctif_passe.get(p)}"
    elif tense == 'Présent':
        return f"que {p}"
    elif tense == 'Imparfait':
        return f"que {p}"

#                C O N D I T I O N N E L                                 #

    conditionnel_passe_premiere_forme = {
        "je": "serais",
        "tu": "serais",
        "il": "serait",
        "elle": "serait",
        "nous": "serions",
        "vous": "seriez",
        "ils": "seraient",
        "elles": "seraient"
    }
    conditionnel_passe_deuxieme_forme = {
        'je': 'fusse',
        'tu': 'fusses',
        'il': 'fût',
        'elle': 'fût',
        'nous': 'fussions',
        'vous': 'fussiez',
        'ils': 'fussent',
        'elles': 'fussent'
    }
    if tense == 'Conditionnel Passé première forme':
        return f"{p} {conditionnel_passe_premiere_forme.get(p)}"
    elif tense == 'Passé deuxième forme':
        return f"{p} {conditionnel_passe_deuxieme_forme.get(p)}"
    
def clarify_output_fr_avoir(p, tense):
#                     I N D I C A T I F                              #
    indicatif_passe_compose = {
        "je": "ai",
        "tu": "as",
        "il (elle, on)": "a",
        "nous": "avons",
        "vous": "avez",
        "ils": "ont"
    }

    indicatif_plus_que_parfait = {
        'je': 'avais',
        'tu': 'avais',
        'il (elle, on)': 'avait',
        'nous': 'avions',
        'vous': 'aviez',
        'ils': 'avaient'
    }

    indicatif_passe_anterieur = {
        'je': 'eus',
        'tu': 'eus',
        'il (elle, on)': 'eut',
        'nous': 'eûmes',
        'vous': 'eûtes',
        'ils': 'eurent'
    }

    indicatif_futur_anterieur = {
        'je': 'aurai',
        'tu': 'auras',
        'il (elle, on)': 'aura',
        'nous': 'aurons',
        'vous': 'aurez',
        'ils': 'auront'
    }

    if tense == 'Passé composé':
        return f"{p} {indicatif_passe_compose.get(p)}"
    elif tense == 'Plus-que-parfait':
        return f"{p} {indicatif_plus_que_parfait.get(p)}"
    elif tense == 'Passé antérieur':
        return f"{p} {indicatif_passe_anterieur.get(p)}"
    elif tense == 'Futur antérieur':
        return f"{p} {indicatif_futur_anterieur.get(p)}"
#                     S U B J O N C T I F                            #

    # subjonctif_present = 
    # que + ...

    # subjonctif_imparfait = 
    # que + ...

    subjonctif_plus_que_parfait = {
        "je": "eusse",
        "tu": "eusses",
        "il": "eût",
        "nous": "eussions",
        "vous": "eussiez",
        "ils": "eussent"
    }

    subjonctif_passé = {
        "je": "aie",
        "tu": "aies",
        "il": "ait",
        "nous": "ayons",
        "vous": "ayez",
        "ils": "aient"
    }

    # if tense == 'Présent':
    #     return f"{p} {subjonctif_present.get(p)}"
    # elif tense == 'Imparfait':
    #     return f"{p} {subjonctif_imparfait.get(p)}"
    if tense == 'Subjonctif Plus-que-parfait':
        return f"{p} {subjonctif_plus_que_parfait.get(p)}"
    elif tense == 'Subjonctif Passé':
        return f"{p} {subjonctif_passé.get(p)}"

#                  C O N D I T I O N N E L                          #
    conditionnel_passe_premiere_forme = {
        "je": "aurais",
        "tu": "aurais",
        "il": "aurait",
        "nous": "aurions",
        "vous": "auriez",
        "ils": "auraient"
    }

    conditionnel_passe_deuxième_forme = {
        'je': 'eusse',
        'tu': 'eusses',
        'il': 'eût',
        'nous': 'eussions',
        'vous': 'eussiez',
        'ils': 'eussent'
    }

    if tense == 'Conditionnel Passé première forme':
        return f"{p} {conditionnel_passe_premiere_forme.get(p)}"
    elif tense == 'Conditionnel Passé deuxième forme':
        return f"{p} {conditionnel_passe_deuxième_forme.get(p)}"

#==============================================================================
#============================= S P A N I S H ==================================

es = {

    # F O R M ---------------------------------------

    "person": ('yo', 'tú', 'él', 'nosotros', 'vosotros', 'ellos'),

    "tenseTypesEs": (
        'Indicativo', 'Subjuntivo', 'Imperativo',
        'Condicional', 'Infinitivo', 'Gerundio',
        'Participo'
    ),

    "Indicativo_tenses": (
        'Indicativo Pretérito imperfecto',
        'Indicativo Pretérito pluscuamperfecto',
        'Indicativo presente',
        'Indicativo pretérito perfecto compuesto',
        'Indicativo pretérito imperfecto',
        'Indicativo pretérito pluscuamperfecto',
        'Indicativo pretérito perfecto simple',
        'Indicativo pretérito anterior',
        'Indicativo futuro',
        'Indicativo futuro perfecto'
    ),

    "Subjuntivo_tenses": (
        'Subjuntivo Pretérito imperfecto 1',
        'Subjuntivo Pretérito pluscuamperfecto 1',
        'Subjuntivo Futuro',
        'Subjuntivo Futuro perfecto',
        'Subjuntivo pretérito perfecto',
        'Subjuntivo pretérito imperfecto 1',
        'Subjuntivo pretérito pluscuamperfecto 1',
        'Subjuntivo pretérito imperfecto 2',
        'Subjuntivo pretérito pluscuamperfecto 2',
        'Subjuntivo futuro',
        'Subjuntivo futuro perfecto'
    ),

    "Condicional_tenses": (
        'Condicional Condicional',
        'Condicional perfecto'
    ),

    "Infinitivo_tenses": (
        'Infinitivo Pessoal Presente',
        'Infinitivo Pessoal Pretérito'
    ),

    "Infinitivo": 'Infinitivo Infinitivo',

    "Gerundio": 'Gerundio Gerondio',

    # start with tu
    "Imperativo_tenses": (
        'Imperativo Afirmativo',
        'Imperativo non'
    ),

    "Participo": 'Participo Participo'
}

def clarifyOutputEs(p, tense):

#                    I N D I C A T I V O                         #
        
    indicativo_preterito_perfecto_compuesto = {'yo': 'he', 'tú': 'has', 'él': 'ha',
            'nosotros': 'hemos', 'vosotros': 'habéis', 'ellos': 'han'}

    indicativo_preterito_pluscuamperfecto = {'yo': 'había', 'tú': 'habías', 'él': 'había',
           'nosotros': 'habíamos', 'vosotros': 'habíais', 'ellos': 'habían'}

    indicativo_preterito_anterior = {'yo': 'hube', 'tú': 'hubiste', 'él': 'hubo',
           'nosotros': 'hubimos', 'vosotros': 'hubisteis', 'ellos': 'hubieron'}

    indicativo_futuro_perfecto = {'yo': 'habré', 'tú': 'habrás', 'él': 'habrá',
           'nosotros': 'habremos', 'vosotros': 'habréis', 'ellos': 'habrán'}
    
    if tense == 'Indicativo pretérito perfecto compuesto':
        return f"{p} {indicativo_preterito_perfecto_compuesto.get(p)}"
    elif tense == 'Indicativo Pretérito pluscuamperfecto':
        return f"{p} {indicativo_preterito_pluscuamperfecto.get(p)}"
    elif tense == 'Indicativo pretérito anterior':
        return f"{p} {indicativo_preterito_anterior.get(p)}"
    elif tense == 'Indicativo futuro perfecto':
        return f"{p} {indicativo_futuro_perfecto.get(p)}"
    
#                      C O N J U N T I V O                      #

    subjuntivo_pretérito_pluscuamperfecto_1 = {'yo': 'hubiera', 'tú': 'hubieras', 'él': 'hubiera',
            'nosotros': 'hubiéramos', 'vosotros': 'hubierais', 'ellos': 'hubieran'}

    subjuntivo_futuro_perfecto = {'yo': 'hubiere', 'tú': 'hubieres', 'él': 'hubiere',
           'nosotros': 'hubiéremos', 'vosotros': 'hubiereis', 'ellos': 'hubieren'}

    subjuntivo_preterito_imperfecto_2 = {'yo': 'hubiese', 'tú': 'hubieses', 'él': 'hubiese',
            'nosotros': 'hubiésemos', 'vosotros': 'hubieseis', 'ellos': 'hubiesen'}

    subjuntivo_preterito_perfecto = {'yo': 'haya', 'tú': 'hayas', 'él': 'haya',
           'nosotros': 'hayamos', 'vosotros': 'hayáis', 'ellos': 'hayan'}
    
    if tense == 'Subjuntivo Pretérito pluscuamperfecto 1':
        return f"{p} {subjuntivo_pretérito_pluscuamperfecto_1.get(p)}"
    elif tense == 'Subjuntivo Futuro perfecto':
        return f"{p} {subjuntivo_futuro_perfecto.get(p)}"
    elif tense == 'Subjuntivo pretérito imperfecto 2':
        return f"{p} {subjuntivo_preterito_imperfecto_2.get(p)}"
    elif tense == 'Subjuntivo pretérito perfecto':
        return f"{p} {subjuntivo_preterito_perfecto.get(p)}"

#                      C O N D I C I O N A L                      #

    conditional_perfecto = {'yo': 'habría', 'tú': 'habrías', 'él': 'habría', 'nosotros': 'habríamos', 'vosotros': 'habríais', 'ellos': 'habrían'}
    
    if tense == 'Condicional perfecto':
        return f"{p} {conditional_perfecto.get(p)}"

#          INFINITIVO COMPUESTO
#          haber dormido


#==============================================================================
#============================= I T A L I A N ==================================

it = {
    "person": ('io', 'tu', 'egli/ella', 'noi', 'voi', 'essi/esse'),
    "essere_pronouns": ("io", "tu", "lui", "lei",
                        "noi", "voi", "loro", "loro"),
    "person_sp": ("1s", "2s", "3s", "1p", "2p", "3p"),

    "moodsIt": (
        'Indicativo', 'Congiuntivo', 'Condizionale',
        'Imperativo', 'infinito', 'participio',
    ),

    "indicativo_tenses_simple": (
            'Indicativo presente',
            'Indicativo imperfetto',
            'Indicativo passato remoto',
            'Indicativo futuro semplice'
    ),
    "indicativo_tenses_complex": (
            # for these pronouns: 0-7 (including):
            'Indicativo passato prossimo',
            'Indicativo trapassato prossimo',
            'Indicativo trapassato remoto',
            'Indicativo futuro anteriore'
    ),

    "congiuntivo_tenses_simple": (
            'Congiuntivo presente',
    ),
    "congiuntivo_tenses_complex": (
            'Congiuntivo imperfetto',
            #  for these pronouns: 0-7 (including):
            'Congiuntivo passato',
            'Congiuntivo trapassato'
    ),

    "conditionale_tenses": (
            'Condizionale presente',
            #  for these pronouns: 0-7 (including):
            'Condizionale passato'
    ),

    "imperativo_tenses": (                   #1s-3p for all, 1s = None:
            'Imperativo Affermativo',
            'Imperativo non',
            # 'Imperativo Non'
    ),

    "infinito": 'Infinito  Gerundio', #       0-3 including
    "participio": 'Participio Participio' #   0-4 including
}

def clarify_output_it_avere(p, tense):
    #================== I N D I C A T I V O =====================   avere

    avere_passato_prossimo = {'io': 'ho', 'tu': 'hai', 'egli/ella': 'ha',
                'noi': 'abbiamo', 'voi': 'avete', 'essi/esse': 'hanno'}
    
    avere_trapassato_prossimo = {'io': 'avevo', 'tu': 'avevi', 'egli/ella': 'aveva',
                'noi': 'avevamo', 'voi': 'avevate', 'essi/esse': 'avevano'}
                
    avere_trapassato_remoto = {'io': 'ebbi', 'tu': 'avesti', 'egli/ella': 'ebbe',
                'noi': 'avemmo', 'voi': 'aveste', 'essi/esse': 'ebbero'}

    avere_futuro_anteriore = {'io': 'avrò', 'tu': 'avrai', 'egli/ella': 'avrà',
                'noi': 'avremo', 'voi': 'avrete', 'essi/esse': 'avranno'}
    
    if tense == 'Indicativo passato prossimo':
        return f"{p} {avere_passato_prossimo.get(p)}"
    elif tense == 'Indicativo trapassato prossimo':
        return f"{p} {avere_trapassato_prossimo.get(p)}"
    elif tense == 'Indicativo trapassato remoto':
        return f"{p} {avere_trapassato_remoto.get(p)}"
    elif tense == 'Indicativo futuro anteriore':
        return f"{p} {avere_futuro_anteriore.get(p)}"

    # ============== C O N G I U N T I V O ====================   avere
    
    avere_congiuntivo_passato = {'io': 'abbia', 'tu': 'abbia', 'egli/ella': 'abbia',
          'noi': 'abbiamo', 'voi': 'abbiate', 'essi/esse': 'abbiano'}

    avere_congiuntivo_trapassato = {'io': 'avessi', 'tu': 'avessi', 'egli/ella': 'avesse',
          'noi': 'avessimo', 'voi': 'aveste', 'essi/esse': 'avessero'}

    if tense == 'Congiuntivo passato':
        # return f"che {p} {avere_passato_prossimo.get(p)}"
        return f"che {p} {avere_congiuntivo_passato.get(p)}"
    elif tense == 'Congiuntivo trapassato':
        # return f"che {p} {avere_trapassato_prossimo.get(p)}"
        return f"che {p} {avere_congiuntivo_trapassato.get(p)}"
    elif tense == 'Congiuntivo imperfetto':
        return f"che {p}"
    elif tense == 'Congiuntivo presente':
        return f"che {p}"

    # ============= C O N D I Z I O N A L E ====================   avere

    avere_condizionale_passato = {'io': 'avrei', 'tu': 'avresti', 'egli/ella': 'avrebbe',
          'noi': 'avremmo', 'voi': 'avreste', 'essi/esse': 'avrebbero'}
    
    if tense == 'Condizionale passato':
        return f"{p} {avere_condizionale_passato.get(p)}"
    
    # ============= G E R U N D I O =========================   avere
    if tense == "gerundio passado":
        return "avendo" # + past participle

def clarify_output_it_essere(p, tense):

    ("io", "tu", "lui", "lei",
        "noi", "voi", "loro", "loro"),

    essere_passato_prossimo = {"io": "sono", "tu": "sei", "lui": "è", "lei": "è",
                 "noi": "siamo", "voi": "siete", "loro": "sono", "loro": "sono"}
    
    essere_trapassato_prossimo = {"io": "ero", "tu": "eri", "lui": "era", "lei": "era",
                 "noi": "eravamo", "voi": "eravate", "loro": "erano", "loro": "erano"}

    essere_trapassato_remoto = {"io": "fui", "tu": "fosti", "lui": "fu", "lei": "fu",
                 "noi": "fummo", "voi": "foste", "loro": "furono", "loro": "furono"}

    essere_futuro_anteriore = {"io": "sarò", "tu": "sarai", "lui": "sarà", "lei": "sarà",
                 "noi": "saremo", "voi": "sarete", "loro": "saranno", "loro": "saranno", }

    if tense == 'Indicativo passato prossimo':
        return f"{p} {essere_passato_prossimo.get(p)}"
    elif tense == 'Indicativo trapassato prossimo':
        return f"{p} {essere_trapassato_prossimo.get(p)}"
    elif tense == 'Indicativo trapassato remoto':
        return f"{p} {essere_trapassato_remoto.get(p)}"
    elif tense == 'Indicativo futuro anteriore':
        return f"{p} {essere_futuro_anteriore.get(p)}"

            # C O N G I U N T I V O ------------------------------
    essere_congiuntivo_passato = {"io": "sia", "tu": "sia", "lui": "sia", "lei": "sia",
                 "noi": "siamo", "voi": "siate", "loro": "siano", "loro": "siano"}

    essere_congiuntivo_trapassato = {"io": "fossi", "tu": "fossi", "lui": "fosse", "lei": "fosse",
                 "noi": "fossimo", "voi": "foste", "loro": "fossero", "loro": "fossero"}

    if tense == 'Congiuntivo presente':
        return f"che {p}"
    elif tense == 'Congiuntivo imperfetto':
        return f"che {p}" #  + Past Participle?????
    elif tense == 'Congiuntivo passato':
        return f"che {p} {essere_congiuntivo_passato.get(p)}" # + past participle
    elif tense == 'Congiuntivo trapassato':
        return f"che {p} {essere_congiuntivo_trapassato.get(p)}" # + past participle
    
#----------------------  C O N D I Z I O N A L E =====================

    essere_condizionale_passato = {"io": "sarei", "tu": "saresti", "lui": "sarebbe", "lei": "sarebbe",
             "noi": "saremmo", "voi": "sareste", "loro": "sarebbero", "loro": "sarebbero"}

    if tense == 'Condizionale passato':
        return f"{p} {essere_condizionale_passato.get(p)}"

# ========================== G E R U N D I O =====================================
    if tense == "Infinito  Gerundio":
        return "essendo"          # + past participle

#==============================================================================
#============================= R O M A N I A N ================================

ro = {
    "person": ('eu', 'tu', 'el/ea', 'noi', 'voi', 'ei/ele'),

    "viitor_tenses": ('Viitor I', 'Viitor I popular', 'Viitor II', 'Viitor II popular'),

    'Prezent': 'Prezent Prezent',
    'Imperfect': 'Imperfect Imperfect',
    'Conjunctiv': ('Conjunctiv prezent', 'Conjunctiv perfect'),

    'Infinitiv': 'Infinitiv Afirmativ',     # only 1

    'Perfect': ('Perfect simplu',
                'Perfect compus'),

    'Mai': 'Mai mult ca perfect', # doesn't work...

    'Viitor': ('Viitor I', 'Viitor I popular', 'Viitor II', 'Viitor II popular'),
#   'Viitor': "Viitor I popular old"   -->   which is not in the mlconjug3

    'Conditional': ('Conditional prezent', 'Conditional perfect'),

#      only               tu                    voi                     nu
    'Imperativ': ('Imperativ Imperativ', 'Imperativ Imperativ', 'Imperativ Negativ'),

    'Gerunziu': 'Gerunziu Gerunziu',
    'Participiu': 'Participiu Participiu'
}

def clarify_output_ro(p, tense):
    perfect_compus = {"eu": "am", "tu": "ai", "el/ea": "a",
                    "noi": "am", "voi": "aţi", "ei/ele": "au"}

    Viitor_I = {'eu': 'voi', 'tu': 'vei', 'el/ea': 'va',
                'noi': 'vom', 'voi': 'veţi', 'ei/ele': 'vor'}

    Viitor_II = {'eu': 'voi fi', 'tu': 'vei fi', 'el/ea': 'va fi',
                 'noi': 'vom fi', 'voi': 'veţi fi', 'ei/ele': 'vor fi'}

    Viitor_II_popular = {'eu': 'am să fi', 'tu': 'ai să fi', 'el/ea': 'are să fi',
                'noi': 'avem să fi', 'voi': 'aveţi să fi', 'ei/ele': 'au să fi'}

    Viitor_I_popular_old = {'eu': 'oi', 'tu': 'îi', 'el/ea': 'a',
                        'noi': 'om', 'voi': 'îţi', 'ei/ele': 'or'}

    Conditional_prezent = {'eu': 'aş', 'tu': 'ai', 'el/ea': 'ar',
                           'noi': 'am', 'voi': 'aţi', 'ei/ele': 'ar'}

    if tense == 'Conjunctiv perfect':
        return f"{p} fi"
    elif tense == 'Perfect compus':
        return f"{p} {perfect_compus.get(p)}"
    elif tense == 'Viitor I':
        return f"{p} {Viitor_I.get(p)}"
    elif tense == 'Viitor I popular':
        return f"{p} o să"
    elif tense == 'Viitor I popular old':
        return f"{p} {Viitor_I_popular_old.get(p)}"        # + atacar   . ... . . . . .
    elif tense == 'Viitor II':
        return f"{p} {Viitor_II.get(p)}"
    elif tense == 'Viitor II popular':
        return f"{p} {Viitor_II_popular.get(p)}"
    elif tense == 'Conditional prezent':
        return f"{p} {Conditional_prezent.get(p)}"
    elif tense == 'Conditional perfect':
        return f"{p} {Conditional_prezent.get(p)} fi"

