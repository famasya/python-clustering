from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import math

color = ['red','green','aqua','orange','blue']
centroid = []
k = 4

def main():
    df = pd.read_csv("dataset.csv")
    df['g'] = 0
    plt.scatter(df['x'],df['y'])
    for i in range(k):
        x = randint(0,150)
        y = randint(0,150)
        plt.scatter(x,y,color=color[i],edgecolors='black')
        centroid.append([x,y])

    # assign initial data to data
    assign(df)
    # while centroid is moving, re-cluster data
    while(calculate(df)):
        assign(df)
    # print variance
    print "Variance",show_variance(df)
    plt.show()

def assign(df):
    for i,row in df.iterrows():
        distance = 999999
        for j,x in enumerate(centroid):
            # calculate euclidean distance
            c = math.sqrt((row['x']-x[0])**2+(row['y']-x[1])**2)
            if(c < distance):
                # assign data to closest cluster
                distance = c
                plt.scatter(row['x'],row['y'],color=color[j])
                df['g'][i] = j

def calculate(df):
    # this function calculate position centroid
    change = False
    for i in range(k):
        tx = 0
        ty = 0
        c = 0
        for index,row in df.iterrows():
            if(row['g'] == i):
                tx += row['x']
                ty += row['y']
                c += 1
        if(c != 0):
            tx /= c
            ty /= c
            # if centroid is moving, return change = True to continue looping
            if((centroid[i][0] != tx) or (centroid[i][1] != ty)):
                plt.scatter(centroid[i][0],centroid[i][1],color='white',edgecolors='white')
                change = True
                centroid[i] = [tx,ty]
            # else:
            #     replot(centroid)
    if(change):
        # print centroid
        replot(centroid)
    else:
        print "stabil"
    return change

def replot(centroid):
    for i in range(k):
        plt.scatter(centroid[i][0],centroid[i][1],color=color[i],edgecolors='black')

def show_variance(df):
    x = 0
    y = 0
    v = 0
    vc = []

    # count vw
    for i in range(k):
        vcx = 0
        for idx,row in df.iterrows():
            if(i == row['g']):
                c = (row['x']-centroid[i][0])**2+(row['y']-centroid[i][1])**2
                v += c
                vcx += c
        vc.append(vcx)
    vw = v/(len(df)-k)

    # count vb
    for j in range(k):
        x += centroid[j][0]
        y += centroid[j][1]
    mx = x/k
    my = y/k
    vb = 0
    for i in range(k):
        c = (centroid[i][0]-mx)**2+(centroid[i][1]-my)**2
        vb += c

    return vw/vb

if __name__ == '__main__':
    main()
