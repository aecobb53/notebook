# Flask

For the coures use the following to spin up flask. 
The name of the file is `hello.py`. 
```bash
export FLASK_APP=app
flask run
```

Top run in development mode (auto update). 
```bash
export FLASK_ENV=development
```

Flask looks for a directory named `templates` for its templates. 
To return html to the web page it is called like this. 
The name is a variable
```python
@app.route('/')
def home():
    return render_template('home.html', name='Nick')
```

To call the variable using `Jinja` add this to the html:
```html
<h2>{{ name }}</h2>
```

You can make the provided variable more detailed with. 
The `'code'` is referencing the part of the `.args` that this example wanted. 
The args are gotten from what was provided to the html input. 
```python
def your_url():
    return render_template('your_url.html', code=request.args['code'])
```

The html input that linked to the above is. 
```html
<input type="text" name="code" value="" required>    
```

Flask by default only allows GET requests. 
To add the different methods to the list of accepted do the following. 
```python
@app.route('/your-url', methods=['GET','POST'])
```

For Flask if you want to accept multiple methods off one url you need if logic. 
```python
@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not valid'
```
> Note: The requests.args is now a request.form

## Redirect

You can redirect flow with redirect. 
```python
return redirect('/')

# OR

return redirect(url_for('home'))
```

In this example the html `name` returns the url
```html
<input type="url" name="url" value="" required>
```
It then goes through this function as a POST and adds it to a dict
```python
def your_url():
    if request.method == 'POST':
        urls = {}
        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
```

## Flash

Flash is used to display info to the user. 
The python side has this
```python
flash('That short name has already been taken. Please select another name.')
```
The html side has this
```html
{% for message in get_flashed_messages() %}
<h2>{{ message }}</h2>
{% endfor %}
```

to do all this you also need to add a secret key to enable sending messages. 
```python
app = Flask(__name__)
app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'
```

## url wildcards

To accept a url and set it to code use this.
```python
@app.route('/<string:code>')
def redirect_to_url(code):
```

## Static

Flask looks for a directory named `static` for static files. 
Files would be javascript, css, images. 

To grab a file with flask. 
```python
return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
```
`static` means static file
`filename=` is the file name

For flask abort returns a 404 or other error code pages. 
```python
reutrn abort(404)
```

You can overrite the error by creatign another function. 
```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

The html for this particular new 404 page is.
```html
<h1>Page Not Found</h1>

<p>We couldn't find what you are looking for. Come visit our homepage :)</p>

<p><a href="{{ url_for('home') }}">Home</a></p>
```
The link for the home page could also be
```html
<p><a href="/">Home</a></p>

```



## Cookies

To add cookie data use session.
```python
session[request.form['code']] = True
```
Im not sure if its important but it was in a with open
```python
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True
```

The data for the session is pulled into the home path using this
```python
@app.route('/')
def home():
    return render_template('home.html', codes=session.keys())
```

The html to display it all looks like this
```html
{% if codes %}
<h2>Codes you have created</h2>
<ul>
  {% for code in codes %}
  <a href="{{ url_for('redirect_to_url', code=code) }}">
  <li>{{ code }}</li>
  </a>
  {% endfor %}
</ul>
{% endif %}
```

This is an unordered list that displayes the data provided as the list of codes. 











