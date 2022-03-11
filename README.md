# line-ui
A simple GUI API (wrapper around PySide2) for Python learners to build simple yet interesting event driven apps.

![a sample line UI app](https://github.com/freemant2000/simgui/raw/main/images/simgui.png)

It provides the following features:
* Create labels, buttons, input fields and comboboxes.
* Respond to events such as button clicks and input text changes.
* Place such widgets on a grid layout easily.
* All is done using simple function calls (no need to understand classes and objects).

With these a Python learner can make GUI apps like: ..., etc.

## How to use
Here is a sample program using line UI that displays a counter, which
is incremented every second or when the user presses the up arrow key.

    from line_ui import *

 
    start(globals())  # must do this to kick start the app with the UI
