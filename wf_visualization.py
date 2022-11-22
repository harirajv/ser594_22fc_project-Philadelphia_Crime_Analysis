import pandas as pd
import numpy
import os
import matplotlib.pyplot as plt

# quantitative_features = ["replies_count", "retweets_count", "likes_count"]
quantitative_features = ["lat", "lng", "dispatch_time_seconds"]

def summary_statistics(data):
    rows = [["Feature", "Min", "Max", "Median"]]
    for ft in quantitative_features:
        print("\nFeature: ", ft)
        print("Min: ", min(data[ft]))
        print("Max: ", max(data[ft]))
        print("Median: ", data[ft].median())
        rows.append([ft, min(data[ft]), max(data[ft]), data[ft].median()])

    rows.append([])

    rows.append(["Features", "Number of categories", "Most frequent", "Least frequent"])
    counts = data["dispatch_month"].value_counts()
    print("Number of unique values: ", data["dispatch_month"].nunique())
    print("Most frequent: ", counts.index[0])
    print("Least frequent: ", counts.index[-1])
    rows.append(["dispatch_month", data["dispatch_month"].nunique(), counts.index[0], counts.index[-1]])

    numpy.savetxt('data_processed/summary.txt', numpy.matrix(rows), fmt='%s')

def correlation(data):
    print(data[quantitative_features].corr())

def draw_plots(data):
    outdir = './visuals'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fig, ax = plt.subplots()
    ax.set(title="Latitude vs Longitude", xlabel="Latitude", ylabel="Longitude")
    ax.scatter(data["lat"], data["lng"])
    ax.legend()
    fig.savefig("visuals/latANDlng.png")

    fig, ax = plt.subplots()
    ax.set(title="Latitude vs dispatch_time_seconds", xlabel="Latitude", ylabel="dispatch_time_seconds")
    ax.scatter(data["lat"], data["dispatch_time_seconds"])
    ax.legend()
    fig.savefig("visuals/latANDdispatch_time_seconds.png")

    fig, ax = plt.subplots()
    ax.set(title="Longitude vs dispatch_time_seconds", xlabel="Longitude", ylabel="dispatch_time_seconds")
    ax.scatter(data["lng"], data["dispatch_time_seconds"])
    ax.legend()
    fig.savefig("visuals/lngANDdispatch_time_seconds.png")

    fig, ax = plt.subplots()
    ax.set(title="Histogram of dispatch_month")
    ax.hist(data["dispatch_month"])
    ax.legend()
    fig.savefig("visuals/dispatch_month_hist.png")
