import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("paperboy_instance.xlsx")

def vier_kwadranten(df, y_groter, x_groter):
    y_groter = int(y_groter)
    x_groter = int(x_groter)
    df_rb = df[(df["y"] > y_groter) & (df["x"] > x_groter)]
    df_ro = df[(df["y"] < y_groter) & (df["x"] > x_groter)]
    df_lb = df[(df["y"] > y_groter) & (df["x"] < x_groter)]
    df_lo = df[(df["y"] < y_groter) & (df["x"] < x_groter)]

    ##startpunt toevoegen
    row = df.iloc[[0]]
    df_ro = pd.concat([row, df_ro])
    df_lo = pd.concat([row, df_lo])
    df_lb = pd.concat([row, df_lb])

    ## index resetten (mooi tellen)
    df_rb = df_rb.reset_index(drop=True)
    df_ro = df_ro.reset_index(drop=True)
    df_lb = df_lb.reset_index(drop=True)
    df_lo = df_lo.reset_index(drop=True)

    return df_rb, df_ro, df_lb, df_lo

def distance(dataframe): 
    dist = {}
    j = 0
    k = 1
    n = len(dataframe)
    while j < n-1:
        d = abs(dataframe.loc[j,"x"] - dataframe.loc[k,"x"]) + abs(dataframe.loc[j,"y"] - dataframe.loc[k,"y"])
        #d = m.sqrt((df.loc[j, "x"] - df.loc[k, "x"])**2 + (df.loc[j, "y"] - df.loc[k, "y"])**2)
        dist[(j, k)] = d
        dist[(k,j)] = d
        k = k + 1
        if k == n:
            j = j + 1
            #print (j)
            k = j + 1
    #print (dist)
    return dist

def nearest_neighbor(dataframe):
    dist = distance(dataframe)
    #distance(dataframe)
    totaal = 0
    kortste = 1000 
    naar_stad = 0 
    i = 0
    j = [0]
    n = len(dataframe)
    while i < n-1:
        for k in range(n):
            if k not in j:
                afstand = dist[(k,j[i])]
                #print (afstand, j[i], k)
                if afstand < kortste:
                    kortste = afstand
                    naar_stad = k
        if naar_stad == None:
            naar_stad = j[0]
            #print(j[34])
            kortste = dist[(j[n-1],j[0])]
            print(kortste)
        j.append(naar_stad)
        #print(f'vanaf punt {j[i]} is punt {j[i+1]} het dichtste bij')
        totaal = totaal + kortste
        #print (f'de totale afstand is {totaal}, en de afstand van het vorige punt naar dit punt is {kortste}')
        i = i + 1
        kortste = 1000
        k = 0
        naar_stad = None
    print (j)
    print(f'de totale afstand is {totaal}')
    return j

def plot_route(dataframe):
    route = nearest_neighbor(dataframe)
    x = dataframe["x"]
    y = dataframe["y"]

    # Plot alle punten
    plt.scatter(x, y, c="blue", s=50, label="Punten")

    # Labels bij punten
    for idx, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi+0.1, yi+0.1, str(idx), fontsize=9)

    # Route tekenen
    route_x = [dataframe.loc[i, "x"] for i in route]
    route_y = [dataframe.loc[i, "y"] for i in route]

    plt.plot(route_x, route_y, c="red", linewidth=2, label="Route")
    plt.scatter(route_x[0], route_y[0], c="green", s=100, label="Start")
    plt.scatter(route_x[-1], route_y[-1], c="orange", s=100, label="Einde")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Route met Nearest Neighbor")
    plt.legend()
    plt.grid(True)
    plt.show()
    return

def route_lengte(dataframe, lijst):
    dist = distance(dataframe)
    n = len(dataframe)
    print(n)
    totale_afstand = 0
    for i in range (n-1):
        afstand = dist[(lijst[i],lijst[i+1])]
        totale_afstand += afstand
    print (totale_afstand)
    return

def plot_verbeterde_route(dataframe, route):
    x = dataframe["x"]
    y = dataframe["y"]

    # Plot alle punten
    plt.scatter(x, y, c="blue", s=50, label="Punten")

    # Labels bij punten
    for idx, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi+0.1, yi+0.1, str(idx), fontsize=9)

    # Route tekenen
    route_x = [dataframe.loc[i, "x"] for i in route]
    route_y = [dataframe.loc[i, "y"] for i in route]

    plt.plot(route_x, route_y, c="red", linewidth=2, label="Route")
    plt.scatter(route_x[0], route_y[0], c="green", s=100, label="Start")
    plt.scatter(route_x[-1], route_y[-1], c="orange", s=100, label="Einde")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Route met Nearest Neighbor")
    plt.legend()
    plt.grid(True)
    plt.show()
    return

