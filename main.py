import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os, sys

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 120


prop = fm.FontProperties(fname='Montserrat-Medium.ttf', weight='bold', size=10)
print(sys.argv)
if len([x for x in sys.argv if "nogrid" in x]) == 0:
    plt.style.use([x for x in plt.style.available if "whitegrid" in x][0])

dashed = len([x for x in sys.argv if "dashed" in x])

#plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

for foldername in os.listdir('data'):
    f = os.path.join("data", foldername)
    plt.figure(figsize=(10,6))
    for filename in os.listdir(f):
        n = os.path.join(f, filename)
        content = open(n).read().split("\n")        
        type = content[0]
        line_label = content[1]
        xlabel = content[2].split(",")[0]
        ylabel = content[2].split(",")[1]
        dataX = [[int(x.split(",")[0])] for x in content[3:] if x!=""]
        dataY = [[int(x.split(",")[1])] for x in content[3:] if x!=""]
        #Lines
        if type == "points":
            plt.scatter(dataX, dataY, label=line_label)
        else:
            plt.plot(dataX, dataY, ('--' if dashed else '-') + ('o' if type == "both" else ''), label=line_label)
        

        plt.xlabel(xlabel, fontproperties=prop)
        plt.ylabel(ylabel, fontproperties=prop)
    title = foldername
    plt.title(title, fontproperties=prop)
    plt.legend(prop=prop)
    plt.show()
