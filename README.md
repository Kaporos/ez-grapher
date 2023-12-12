This script was written fast, it's not meant to be beautiful code lmaoo forgive me for this cursed (yet working) script

# Usage

Create one folder inside of `data` directory per graph you want to make. (The name of the folder will be the name of the graph, look at samples)

Then, inside graph's folder, create as many files `.txt` as you want (and each of them will be plotted on the same graph), following this format:

    plot_type
    Data label
    labelX, labelY
    x1, y1
    x2, y2
    x3, y3

Plot type can be either `line`, `points` or `both` (look at samples)

(etc with all your data, there already are some samples in the `data` directory)

Then, run this to plot graphes one by one with default settings, just do

    python main.py

But you can change settings by adding settings to the command this way (there is 2 of them here but you can put only one):

    python main.py sett1 sett2

And current settings are:

`nogrid` if you want to hide the background grid

`dashed` if you want dashed lines instead of solid ones

so

    python main.py dashed

is a valid command :D

