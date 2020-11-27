# Terminal Multiplexer

**CAUTION!** TMUX is very powerful, and can be easy to abuse.
Do not use unles you know what you are doing

## Table of contents

- [Structure](#structure)
- [Most common commands](#most-common-commands)
- [How to use](#how-to-use)
- [When it is useful](#when-it-is-useful)

---

### Structure

The order of waht you see

| Name | What it does |
| --- | --- |
| Session | lists of windows |
| Window | can be devided into pane |
| Pane | terminal where you do work |

tmux is linked to a specific user and host. 

### Most common commands

I dont know yet

### How to use

I dont know yet

#### Commands from original terminal

| Command | What it does |
| --- | --- |
| tmux | Opens a new window |
| tmux a | Re-opens the last session 'attach' |
| tmux a -r | Attach a read-only window |
| tmux a -t myname | Attach a named window |
| tmux ls | List out the current windows |
| tmux new -s <name> | Opens a named window |
| tmux kill-session -t < name > | Kill a window |

#### In a Session

| Command | What it does |
| --- | --- |
| :new< CR > | New session |
| s | List sessions |
| $ | Name session |

#### In a Window

`ctr + b` lets tmux know that you are about to send a command not in the window. 

| Command | What it does |
| --- | --- |
| ctr + b | Non windowed command |
| exit | Kiklk the window |
| c | Create window |
| w | List windows |
| n | Next window |
| p | Previous window |
| f | Find window |
| , | Name window |
| & | Kill window |

#### In a Pane

| Command | What it does |
| --- | --- |
| % | vertical split
| " | horizontal split
| o | swap panes
| q | show pane numbers
| x | kill pane
| + | break pane into window (e.g. to select text by mouse to copy)
| - | restore pane from window
| ⍽ | space - toggle between layouts
| <prefix> q | (Show pane numbers, when the numbers show up type the key to goto that pane)
| <prefix> { | (Move the current pane left)
| <prefix> } | (Move the current pane right)
| <prefix> z | toggle pane zoom

#### Closing a window

| Command | What it does |
| --- | --- |
| d | closes the window 'detach' |

#### Other

| Command | What it does |
| --- | --- |
| t | big clock |
| ? | list shortcuts |
| : | prompt |

### When it is useful

Kepler
Runnincg CPG when you have to pass off to another person on shift.

### Troubleshooting

Not enough is known yet to really know how to troubleshoot... 
so google it and let us know what worked and what didnt. 

https://gist.github.com/MohamedAlaa/2961058
