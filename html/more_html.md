# More HTML

# Form

Forms are used to taek user input. 
This one takes input for a url
```html
<form action="your-url">
    <input type="url" name="url">
    <input type="text" name="code">
    <input type="submit" value="Shorten">
</form>
```

The above form looks better if its the following. 
```html
<form action="your-url">
  <label for="url">Website URL</label>
    <input type="url" name="url" value="" required>
    <br>
    <label for="code">Short Name</label>
    <input type="text" name="code" value="" required>
    <br>
    <input type="submit" value="Shorten">
</form>
```

You can change the form to be a post instead of a get by adding a `method` indicator. 
```html
<form action="your-url" method="post">
```
> Note: by default Flask only allows GET requests

**important** The form will submit the data to the url specified in the `action`!!


# Input

You can require input with `value""= required`. 

## Other

This will list out `code`s provided
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

`ul` will set it as an unordered list. 
`li` is a list item. 
The atag wraps each code so that it lists both the code for the url data and the url for this example. 
The example was listing out abreviated urls

---

`base.html` is used as a base for every page in a project. 

An example base that displays messages on every webpage in the projcet is this. `base.html`
```html
<head>
  <title>{% block title %}{% endblock %}</title>
</head>

{% for message in get_flashed_messages() %}
<h2>{{ message }}</h2>
{% endfor %}

{% block main %}
{% endblock %}
```

The main html calls the blocks.html blocks
```html
{% extends 'base.html' %}

{% block title %}URL Shortener{% endblock %}

{% block main %}

<!-- <main file stuff> -->

{% endblock %}

```

Here the `home.html` will load and pass the url shortener header to the `base.html` file. 
The file will then display the `home.html`s title in the header of `base.html` and then 
display any error messages in the for block. 
The `base.html` file then calls the main block which brings it back to the `home.html` file. 
So by running `home.html` the info for that page is wrapped up and passed to `base.html` and displayed there. 


