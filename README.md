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
