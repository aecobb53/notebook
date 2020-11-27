
## Links

Staying informed with css
https://www.w3.org/Style/CSS/

Color documentation
https://colours.neilorangepeel.com
https://www.css-tricks.com/examples/HSLaExplorer/

Specificity calculator
https://www.specificity.keegan.st

palet selector 
https://www.coolors.co

fonts link
https://www.cssfontstack.com
https://www.fonts.google.com
https://www.developer.mozilla.org/en-US/docs/Web/CSS/font
This one is gold if it covers  the topic ^^ it also does flexboxes!

css tricks
https://www/css-tricks.com/snippets/css/clear-fix/

browser support
https://www.caniuse.com

grid resource
https://www.mozilla.org/en-US/developer/css-grid

for one class:
```css
.example {
    color: blue;
}
```

```html
<h1 class="example">Herader</h1>
```

for more than one:
```css
.example1 {
    color: grey;
}
```

```html
<h1 class="example example2">Herader</h1>
```

for exactly two
```css
.example.example1 {
    color: grey;
}
```

## Example with desendant selectors

```css
a {
    /* stuff */
}
```

to set something like a section use:
```css
section a {
    /* stuff */
}
```

to make a class part of a secion use
```css
.container a {
    /* stuff */
}
```

For something like using a paragraph and the above:
```css
.container p a {
    /* stuff */
}
```

```html
<section> class="flex-container
  <p><a href="#">Link inside a paragraph</a></p>
  <a href="#">Link outside a paragraph</a>
</section>
<a href="#">Link outside a section</a>
```

> 'a' implies anchor

## links changing styles

link - default
visited - has been clicked
hover - mouse hover over
active - currently clicked
focus - using tab to select links

for example:
```css
a:link {
    /* this applies to the link before anything happens to it */
}
a:visited {
    /* if a link is clicked then this is applioed */
}
```


## Box model

You can define a width and then later define a percet of that width

types inline, block, inline-block

order of padding top, right, bottom, left
or top, right/left, bottom
or top/bottom, right/left
or all

border:
border-width
border-style
border-color
or together border-width border-style border-color


border-width
thin, medium, thick, #px

border-color
name 

border-style
none, hidden, dotted, dashed, solid, double, groove, ridge, inset, outset

margin can have negative values but not the border

auto will center something on the page side to side


## Typography

types of fonts: Script, Decorative, Monospace, Serif, Sans-serif
Script: Hand written feel, good for headers bad fgor content
Decorative: Same as Script use
Monospace: Characters are the same, good for info
Serif: Triditional an dformal
Sans-serif: contemorary motern 

font-family is used for a list of fonts in order of preference. 
If a computer does not have the prefered element, the one after is selected. 
Always include a generic font last so content is still displayed. 

Generic font families: 
serif (serif fonts), 
sans-serif(sans-serif fonts), 
cursive (script or decorative fonts)
fantasy (decorative fonts)
monospace (monospace fonts)

font names may need escape characterse or quotes to use, generic must not have quotes. weird i know

font-weight
light, regular, semi-bold, bold, extra-bold
or weighted from 100 to 900

Italicise with italic, oblique, and normal. 
italic appears cursive whereas oblique appears slanted. 
normal undoes it


font-size: relative and absolute. the default is 16px. avoid decimals here. 
If you use the "em" unit it is a multiple factor of the ancestor font size, this can be decimals. 
1em is the inheritied font size. 
"rem" is m with respect to the root html element

font-styple: italic;
font-size: small-caps;
font-weight: bold;
font-family: 24px;
font-variant: 1.5;
line-height: Helvetica, sans-serif;
or
font: [font-style] [font-variant] [font-weight] font-size/[line-height] font-family;
font: italic small
font-variant = normal OR small-caps
font-size/line-height
font-family must be last

text-decoration: text-decoration-line text-decoration-color text-decoration-stle

text-decoration-line: none, underline, overline, line-through, underline overline, underline line-through
text-decoration-color:
text-decoration-stle: solid, double, dotted, dashed, wavy

font-size and line-height are porportionate. 
if line-height < font-size the lines will overlap. 
if line-height is a % > 100% like 150% then they wont overlap and will scale when font-size increases. 
can also use a unitless multiplier. reccomended to go between 1.25 and 1.5

text-align: center, right, left, justify


## layouts: floats and position

float: left will move the thing to the left and have the main page move around it to the right. 
Can clear the flow in the main html

overflow handles content that is too large for a space. 
auto adds scrollbar if the content is too large
scroll always adds a scroll bar

use width to set the width of the box when doing floats

positions: 
static: not positioned
relative: relative to current position
absolute: relative to containing element
fixed: related to viewport
sticky: relative to conaining element and viewport
This could be useful for table of contents

stack order WRT the z-index. 
The stacks are also stacked by order seen in the CSS bottom on top of the viewport
1. html/body
2. block
3. float
4. inline
5. position

You can add `position: relative;` and it will boost the position to betweeen inline and position. 
You can also add `z-index: <number>;` and it will stack highest number to lowest number


## Flexbox and grid

flex container is the parent element
flex items are the child elements

`flex-wrap: wrap` will wrap flex items to the next row if there is not enough room. 

flex: grow shrink basis;
flex: 0 1 100px; 
grow 0 does not fill, 1 does fill
shrink 1 shirnks to container, 0 overflows the size
basis can be units, %, strings. This is the "ideal value"

justify-content aligns in the main (horizontal) axis
align-items aligns items on the corss (verticle) axis

**Grid index starts at 1!**, they can also be referenced by negative indexing

the unit `fr` is used for fractoins


## Advanced selectors

using a `>` signifies child not just descendant

```css
parent child {}

parent > child {}
```

using `+` signifies the child after so applies to `p` here

```css
h1 + p {}
```
```html
<h1></h1>
<p></p>
```

using `~` applies to any sibling after the first element

```html
<p></p> does not apply
<h1></h1>
<p></p> does apply
<p></p> does apply
```

can use 
:first-child :last-child
:first-type :last-type


## Fluid Responsive Layouts

The folowing block will apply h1 if the screen width is under 1000px

```css
@media screen and (max-width: 1000px) {
    h1 {
        font-size: 16px
    }
}
```

media types
all
print
speech
screen

can use and to combine mulitple medai quries





