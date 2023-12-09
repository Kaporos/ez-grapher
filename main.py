import matplotlib.pyplot as plt
import os


for foldername in os.listdir('data'):
    f = os.path.join("data", foldername)
    for filename in os.listdir(f):
        n = os.path.join(f, filename)
        content = open(n).read().split("\n")
        title = foldername
        xlabel = content[0].split(",")[0]
        ylabel = content[0].split(",")[1]
        dataX = [[int(x.split(",")[0])] for x in content[1:] if x!=""]
        dataY = [[int(x.split(",")[1])] for x in content[1:] if x!=""]
        #Lines
        plt.plot(dataX, dataY)

        #Points
        #plt.scatter(dataX, dataY)
        plt.ylabel(xlabel)
        plt.xlabel(ylabel)
    plt.title(title)
    plt.show()
