## Start Serving (for windows)

1. Enter project folder
2. install mlconjug3 globally (guess it's not included in the virtual env...):
```cmd
pip install mlconjug3
```
4. activate virtual environment (windows)
```cmd
venv\Scripts\activate
```
4.5. install Flask if necessary
5. run the server:
```cmd
flask --app app.py run --debug
```
6. go to localhost:5000/{lang-code}/

lang-codes: pt, it, es, ro, (fr is not ready yet)