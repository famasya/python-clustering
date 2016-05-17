import pandas as pd
import random
import matplotlib.pyplot as plt
import math

k = 2
colorarray = []
clustered = []

def main():
    df = pd.read_csv("dummy.csv")
    df['g'] = 0
    l = len(df)
    for i,row in df.iterrows():
        c = color()
        plt.scatter(row['x'],row['y'],color=c)
        row['g'] = i
        colorarray.append(c)

    # while available cluster > k, iterate
    while(l>k):
        l = group(df,l)
        print 'Jumlah cluster',l
    print df
    plt.show()

def color():
    r = lambda: random.randint(0,255)
    return ('#%02X%02X%02X' % (r(),r(),r()))

def group(df,l):
    merge = []
    merge.append(0)
    merge.append(0)
    minval = 99999
    # calculate two closest data
    for x,y in df.iterrows():
        for j,k in df.iterrows():
            if((j > x) and (y['g'] != k['g'])):
                c = math.sqrt((y['x']-k['x'])**2+(y['y']-k['y'])**2)
                if(c < minval):
                    minval = c
                    merge[0] = x
                    merge[1] = j
    ga = df['g'][merge[0]]
    gb = df['g'][merge[1]]
    # merge it to most populate cluster
    if(clustered.count(ga) > clustered.count(gb)):
        a = merge[1]
        b = merge[0]
    else:
        a = merge[0]
        b = merge[1]
    plt.scatter(df['x'][a],df['y'][a],color=colorarray[b])
    colorarray[a] = colorarray[b]
    df['g'][a] = df['g'][b]
    clustered.append(df['g'][b])
    # return how many cluster left
    return len(set(df['g']))


if __name__ == '__main__':
    main()
