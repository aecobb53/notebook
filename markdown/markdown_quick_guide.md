# Markdown quick guide

:sunglasses: Happy Marking :sunglasses:

## Table of contents

- [Headers and Page Breaks](#headers-and-page-breaks)
- [Emphasis](#emphasis)
- [Syntax](#syntax)
- [Links](#links)
- [Lists](#lists)
- [Tables](#tables)
- [Color and boxes](#color-and-boxes)
- [Emojis](#emojis)
- [Dropdown](#dropdown)
- [Inline HTML](#inline-html)
- [Hidden comments](#hidden-comments)
- [Reference links](#references)


The brackets display and the parentheses link. 
The link can't have capitals or spaces. 
Instead of spaces, use `-` characters. 
```
## Table of contents

- [Example Header](#example-header)

## Example Header
```

---

## Headers and Page Breaks

There are size levels of headers

# H1
## H2
### H3
#### H4
##### H5
###### H6

All page breaks look the same despite the different ways to make them

---

`---`

***

`***`

___

`___`

[//]: # (Two antennas got married – the wedding was lousy, but the reception was outstanding.)

## Emphasis

*Italic*

_Italic_

**Bold**

__Bold__

***Bold-Italic***

___Bold-Italic___

~Strikethrough~

\*Escape\*

> Note: Using single `~` and double `~~` both work for strikethrough. 
The difference is the single `~` will not show up when editing the file in the remote repo. 

```md
*Italic*

_Italic_

**Bold**

__Bold__

***Bold-Italic***

___Bold-Italic___

~Strikethrough~

\*Escape\*
```

[//]: # (Why did the Higgs Boson go to church?)
[//]: # (For the mass)

## Syntax

`Text emphases`

```
code block
```


\`Text emphases\`

\`\`\`

code block

\`\`\`

```python
import datetime

print('Hello World!')
```

> Note: You can add the language of the code block and it will be formatted for that language. 

\`\`\`python

import datetime

print('Hello World!')

\`\`\`

<details>
<summary>Supported languages</summary>
 <br>
actionscript3, 
apache, 
applescript, 
asp, 
brainfuck, 
c, 
cfm, 
clojure, 
cmake, 
coffee-script, 
coffeescript, 
coffee, 
cpp - C++, 
cs, 
csharp, 
css, 
csv, 
bash, 
diff, 
elixir, 
erb - HTML + Embedded Ruby, 
go, 
haml, 
http, 
java, 
javascript, 
json, 
jsx, 
less, 
lolcode, 
make - Makefile, 
markdown, 
matlab, 
nginx, 
objectivec, 
pascal, 
PHP, 
Perl, 
python, 
profile - python profiler output, 
rust, 
salt, saltstate - Salt, 
shell, sh, zsh, bash - Shell scripting, 
sql, 
scss, 
sql, 
svg, 
swift, 
rb, jruby, ruby - Ruby, 
smalltalk, 
vim, viml - Vim Script, 
volt, 
vhdl, 
vue, 
xml - XML and also used for HTML with inline CSS and Javascript, 
yaml
</details>

[//]: # (Looking for a boyfriend in engineering: the odds are good, but the goods are odd.)

## Links

[Link to emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

[Scripts readme](/scripts/README_scripts.md)

[Github quick reference guide](github_quick_guide.md) 

![Earth_selfy](image_dir/earth_selfy.jpg)

```md
[Link to emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

[Scripts readme](/scripts/README_scripts.md)

[Github quick reference guide](github_quick_guide.md)

![Earth_selfy](image_dir/earth_selfy.jpg)

Note: you only need to add the leading '/' for git links if you must go back up a directory. 
```

You can link to links further down in the file.

**The quick brown [fox][1], jumped over the lazy [dog][2].**

[1]: https://en.wikipedia.org/wiki/Fox "Wikipedia: Fox"
[2]: https://en.wikipedia.org/wiki/Dog "Wikipedia: Dog"

```md
**The quick brown [fox][1], jumped over the lazy [dog][2].**

[1]: https://en.wikipedia.org/wiki/Fox "Wikipedia: Fox"
[2]: https://en.wikipedia.org/wiki/Dog "Wikipedia: Dog"
```

[//]: # (Looking for a girlfriend in engineering is like looking for a parking space.)
[//]: # (All the good ones are taken and the ones that are left are WAY out there.)

## Lists

There are three types of lists:

1. Number

2. Listed

    - With indent
  
- Regular

- Listed

    - With indent

- \-

* \*

> Note: Three indent spaces are required for numbered lists, but only two for non-numbered


![indent_example](image_dir/nested-list-alignment.png)

```md
1. Number

2. Listed

   - With indent
    
- Regular

- Listed

  - With indent

- \-

* \*
```

- [ ] Unchecked

- [x] Checked

```md
- [ ] Unchecked

- [x] Checked
```

The numbered lists will order all numbers in order not in the order see in the markdown. 
Basickly, if you switch lines around you dont have to update the numbers:

1. one
3. three
2. two

```
1. one
3. three
2. two
```

[//]: # (What's the difference between an introverted and an extroverted engineer?)
[//]: # (An introverted engineer looks at his shoes when he's talking to you, an extroverted engineer looks at your shoes when he's talking to you.)

## Tables

| Style | Example | Syntax |
| ----- | ------- | ------ |
| Italic | *This is italic* | \*This is italic\* or \_This is italic\_ |
| Bold | **This is bold** | \**This is bold\** or \__This is bold\__ |
| Bold-Italic | ***This is bold-italic*** | \*\*\*This is bold-italic\*\*\* or \_\_\_This is bold-italic\_\_\_ |
| Strikethrough | ~This is sticken~ | \~This is sticken\~ or \~\~This is sticken\~\~ |


```md
| Style | Example | Syntax |
| ----- | ------- | ------ |
| Italic | *This is italic* | \*This is italic\* or \_This is italic\_ |
| Bold | **This is bold** | \**This is bold\** or \__This is bold\__ |
| Bold-Italic | ***This is bold-italic*** | \*\*\*This is bold-italic\*\*\* or \_\_\_This is bold-italic\_\_\_ |
| Strikethrough | ~This is sticken~ | \~This is sticken\~ or \~\~This is sticken\~\~ |
```

> Note: You can get away with only placing three `-`for the second row. 
You can also add white space so that the file is easier to read. 

| Style         | Example                   | Syntax |
| ---           | ---                       | --- |
| Italic        | *This is italic*          | \*This is italic\* or \_This is italic\_ |
| Bold          | **This is bold**          | \**This is bold\** or \__This is bold\__ |
| Bold-Italic   | ***This is bold-italic*** | \*\*\*This is bold-italic\*\*\* or \_\_\_This is bold-italic\_\_\_ |
| Strikethrough | ~This is sticken~         | \~This is sticken\~ or \~\~This is sticken\~\~ |

```md
| Style         | Example                   | Syntax |
| ---           | ---                       | --- |
| Italic        | *This is italic*          | \*This is italic\* or \_This is italic\_ |
| Bold          | **This is bold**          | \**This is bold\** or \__This is bold\__ |
| Bold-Italic   | ***This is bold-italic*** | \*\*\*This is bold-italic\*\*\* or \_\_\_This is bold-italic\_\_\_ |
| Strikethrough | ~This is sticken~         | \~This is sticken\~ or \~\~This is sticken\~\~ |
```

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

```md
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```

[//]: # (What did the electrical engineer say when he got shocked?)
[//]: # (That hertz!)

## Color and boxes

- ![#ff0000](https://placehold.it/12/ff0000?text=+) red!
- ![#9900c5](https://placehold.it/15/9900c5?text=+) purple!
- ![#157500](https://placehold.it/20/157500?text=+) green!

![](https://placehold.it/400x90/ff0000/000000?text=IMPORTANT!)

![](https://placehold.it/400x90/ff6600/000?text=WARNING!)

![](https://placehold.it/350x90/009955/fff?text=SUCCESS!)

```md
- ![#ff0000](https://placehold.it/12/ff0000?text=+) red!
- ![#9900c5](https://placehold.it/15/9900c5?text=+) purple!
- ![#157500](https://placehold.it/20/157500?text=+) green!

![](https://placehold.it/400x90/ff0000/000000?text=IMPORTANT!)

![](https://placehold.it/400x90/ff6600/000?text=WARNING!)

![](https://placehold.it/350x90/009955/fff?text=SUCCESS!)
```

| White  | Black  |  Red   |  Blue  | Yellow | Green  | Orange | Purple |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| FFFFFF | 000000 | FF0000 | 0000FF | FFFF00 | 00FF00 | FF6600 | 6600FF |

[//]: # (What to give your favorite electrical engineer for his birthday?)
[//]: # (Shorts.)

## [Emojis](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

:thumbsup:

`:thumbsup:`

[Check out the list](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

[//]: # (Why was the thermometer smarter than the graduated cylinder?)
[//]: # (He had more degrees.)

## Dropdown

<details>
<summary>Basic dropdown</summary>
  Type in your body here. 
  
  This is just a text field. 
<br>
You can also use HTML.
</details>

```md
<details>
<summary>Basic dropdown</summary>
  Type in your body here. 
  
  This is just a text field. 
<br>
You can also use HTML.
</details>
```

<details open>
<summary>Basic open dropdown</summary>
<br>
In this dropdown, the text starts open. 
</details>

```md
<details open>
<summary>Basic open dropdown</summary>
<br>
In this dropdown, the text starts open. 
</details>
```

[//]: # (A pessimist looks at a glass of water and states it is half empty,)
[//]: # (an optimist looks at the same glass and states it is half full,)
[//]: # (but an engineer sees it and states the glass is twice as tall as it should be.)

## Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

```md
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

[//]: # (Why did the electron throw up?)
[//]: # ( He was spinning.)

## Hidden comments

[//]: # (You cannot see this)

<!--or this-->

```md
[//]: # (You cannot see this)

<!--or this-->
```

This is a normal line

<!-- This is commented out. -->

<!-- 
This is commented out. 
-->

Example of a line with<!-- red --> one<!-- clc --> flag. 

This <!-- red -->line <!-- blue --> will <!-- clc --> be <!-- green, back white -->different <!-- clc --> colors.



## References

[Useful Github commands](https://github.digitalglobe.com/p20-20-mcs/MCS-toolbox/blob/dev/docs/resources/github_quick_guide.md)

[Basic writing and formatting syntax](https://help.github.com/en/articles/basic-writing-and-formatting-syntax#headings)

[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

[GitHub Flavored Markdown Spec](https://github.github.com/gfm/#example-265)

[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#videos)

[Dropdown.md](https://gist.github.com/citrusui/07978f14b11adada364ff901e27c7f61)

[How to: The Ultimate Guide to Markdown](https://blog.ghost.org/markdown/)

[5 Markdown Tricks for GitHub](https://grantwinney.com/cool-markdown-tricks-for-github/)

[Placeholder Images Made For You](https://placeholder.com/)
