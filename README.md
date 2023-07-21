# conjugator
Romance Language Verb Conjugator and Trainer
> (!) Only italian works by now, to ckeck other languages delete these lines in form.html:
```html
  <div class="moods">
    <!-- <div>select a mood</div> -->
    <div class="mood">{{ it.moodsIt[0] }}</div>
    <div class="mood">{{ it.moodsIt[1] }}</div>
    <div class="mood">{{ it.moodsIt[2] }}, {{ it.moodsIt[3] }}</div>
    <div class="mood">{{ it.moodsIt[4] }}, {{ it.moodsIt[5] }}</div>
  </div>

<!--  some code goes here  -->

<script>
  var it = {{ it|tojson }};
  console.log(it);
</script>
```

## How to run
```bash
cd Project_Foulder
(in Windows:) venv\Scripts\activate
(in Linux/Mac:) source myenv/bin/activate
flask --app app.py run --debug
```
go to localhost:5000/<language>
where <language> is one of these: pt/it/ro/es/fr
example path for Portuguese: localhost:5000/pt

(!) might require installing mlconjug3 library grobally
(!) if so, just write in bash:
```bash
pip install mlconjug3
```

## How it works

(if deleted lines above): check language in the <nav> bar, then write a verb in the search bar above to see it's conjugations.
Training functionality is not working yet, it will be similar to [Verbugata](https://www.verbugata.com/), but hopefully better.

Each level on levels panel (one that looks like calculator) corresponds to 25 verbs, sorted by frequency. 2000 total for every language. Functionality is not working yet.

## Future plans

I want to rewrite this project on React and finish it. After finishing it will be an Open Source project for people to train Romance Language Verb Conjugations.
