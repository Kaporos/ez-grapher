# Usage

Create one folder inside of data/ per graph you want to made. (look at samples)

Then, inside graph's folder, create as many files `.txt` as you want (and each of them will be plotted on the same graph), following this format:

    labelX, labelY
    x1, y1
    x2, y2
    x3, y3

(etc with all your data)

Then, run this to plot graphes one by one.

    python main.py

If you want lines leave everything by default, but you can also do

    python main.py points

If you want to not to draw a line between points.
