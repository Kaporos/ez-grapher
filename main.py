import matplotlib.pyplot as plt
import os, sys


for foldername in os.listdir('data'):
    f = os.path.join("data", foldername)
    for filename in os.listdir(f):
        n = os.path.join(f, filename)
        content = open(n).read().split("\n")
        line_label = content[0]
        xlabel = content[1].split(",")[0]
        ylabel = content[1].split(",")[1]
        dataX = [[int(x.split(",")[0])] for x in content[2:] if x!=""]
        dataY = [[int(x.split(",")[1])] for x in content[2:] if x!=""]
        #Lines
        if len(sys.argv) > 1 and sys.argv[1] == "points":
            plt.scatter(dataX, dataY, label=line_label)
        else:
            plt.plot(dataX, dataY, label=line_label)

        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
    title = foldername
    plt.title(title)
    plt.legend()
    plt.show()
