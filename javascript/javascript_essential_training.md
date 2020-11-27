# Java Script Essential Training

I have a few md's flaoting around but this is intended to be the final copy

## Links

resource hints
https://www.w3.org/TR/resource-hints/

## the basics

Get to js terminal with Chrome > More Tools > Developer Tools > Console or `Shift+Ctr+i`. 
Can clear the space with a button on the top left circle with a slash. 

Send a browser alert with `alert('Hello World!')`. 
To log to consol use `console.log('Hello Wrold!')`. 
js date `new Date()`. 

### inline JavaScript in HTML

you can add `<script>`'s inside the `header`, `body`, or after the `body`. 
Place it in the `header` if you want it to run before the contents of the page are rendered, 
`body` if you want it to run while the page is rendering (order of lines initiates the load), 
or after the `body` if you want it to run after the page renders. 

If you add a script to render in the head it will render before any part of the body starts. 
If its not needed its best to add it to the body. 

Today we can load scripts right away, asyncronously, or deferred. 
Right away results in render blocking. 
If its not needed its best to not do it as it slows everything down. 
If loaded async, it will load alongside others but wont execute async. 
Defer will load the script but wont execute until it is called i think. 

To run in right away i think you do this 
```javascript
<script src="script.js"></script>
```

To run in async 
```javascript
<script src="script.js" async></script>
```

To defer
```javascript
<script src="script.js" defer></script>
```

### Variables/Objects

Create a variable with `var example = stuff;`. 
The nomenclature is camelCase. 
Create objects and classes with uppercase CamelCase. 
So `var NewExample = {};`. 
Create constants with all upcase. 
So `CONSTANT = 3.14;`

### Comments

Single line comments are `//`, multi line comments are `/*  */`

## Working with data

### Datatypes

- Numeric
- String
- Boolean
- null
- undefined

You can define variables with const and let; `const MYCONSTANT = 5;`. 
let will only assign a variable in the statement it was created in. 
See example 4_6 for examples

`console.log(typeof variableName)` will display the type for the variable

If you try to add a string and an int it will assume string. 
4 + '5' = '45'. 
But if you attempt [-*/] and the string is intable it will assume int. 
4 - '5' = -1. 
4 * '5' = 20. 
4 / '5' = .8. 

## Functions and Objects

### Functions

There are three types of functions:
- named functions
- anonymous functions
- immediatly invoked function expressions

**Regular function:**
```javascript
function name() {
    stuff
}
name();
```

**Anonymous function:**
```javascript
var variableName = function() {
    other stuff
}
variableName();
```

**immediatly invoked:**
```javascript
(function() {
    more stuff
})()
```

All funcctions can return with `return`. 

When logging a function, named and anonymous functions return different things
```javascript
// Named
consol.log(theFunction(arg1, arg2))
> 'function details'

//Anonymous
consol.log(theFunction(arg1, arg2))
> 'returned results'
```

### IF

```javascript
if ( condition ) {
    do something.
} else {
    Do something else. 
}
```

`5 == '5'`    will yield `true`

`5 === '5'`   will yield `false`; "strict equality"

shorthand for boolean compare. 
a = true

```javascript
if ( a )
if ( !a )
```

for AND/OR use &&|| no XOR statement

ternary operator
```javascript
a == b ? console.log("Match") : consol.log("No match");
```

### FOR

```javascript
for ( var i = 0; i < 10; i++ ){
    // stuff
}
```

### WHILE

```javascript
var i=0;
while( i < 10 ) {
    i++
}
```

```javascript
do {
    stuff
} while ( bool );
```

### querySelector

When using `querySelector.innerHTML` you can set the element but it must be a string. 
For example 

>Note: the date.getMonth() is one month too young, thus the +1 is added.

```javascript
document.body.innerHTML = "<h1>The date today is " + (date.getMonth()+1) + "/" + date.getDate() + '/' + date.getYear() + "</h1>"
```

continuing that example, `innerHTML` and `outerHTML` yield different stuff... duh. 
`.innerHTML`: `"<h1>The date today is 11/6/120</h1>"`
`.outerHTML`: `"<body><h1>The date today is 11/6/120</h1></body>"`
