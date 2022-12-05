import numpy
import os
import matplotlib.pyplot as plt

quantitative_features = ["lat", "lng", "dispatch_time_seconds"]

def summary_statistics(data):
    rows = [["Feature", "Min", "Max", "Median"]]
    for ft in quantitative_features:
        print("\nFeature: ", ft)
        print("Min: ", min(data[ft]))
        print("Max: ", max(data[ft]))
        print("Median: ", data[ft].median())
        rows.append([ft, min(data[ft]), max(data[ft]), data[ft].median()])

    rows.append([""]*4)

    rows.append(["Features", "Number of categories", "Most frequent", "Least frequent"])
    counts = data["dispatch_month"].value_counts()
    print("Number of unique values: ", data["dispatch_month"].nunique())
    print("Most frequent: ", counts.index[0])
    print("Least frequent: ", counts.index[-1])
    rows.append(["dispatch_month", data["dispatch_month"].nunique(), counts.index[0], counts.index[-1]])

    numpy.savetxt('data_processed/summary.txt', numpy.matrix(rows), fmt='%s')

def correlation(data):
    df = data[quantitative_features].corr()
    # df.columns = quantitative_features
    # df.index = quantitative_features
    # numpy.savetxt('data_processed/correlations.txt', df.values, fmt='%d')
    with open('data_processed/correlations.txt', 'w') as f:
        dfAsString = df.to_string()
        f.write(dfAsString)

def draw_plots(data):
    outdir = './visuals'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fig, ax = plt.subplots()
    ax.set(title="Latitude vs Longitude", xlabel="Latitude", ylabel="Longitude")
    ax.scatter(data["lat"], data["lng"])
    fig.savefig("visuals/latANDlng.png")

    fig, ax = plt.subplots()
    ax.set(title="Latitude vs dispatch_time_seconds", xlabel="Latitude", ylabel="dispatch_time_seconds")
    ax.scatter(data["lat"], data["dispatch_time_seconds"])
    fig.savefig("visuals/latANDdispatch_time_seconds.png")

    fig, ax = plt.subplots()
    ax.set(title="Longitude vs dispatch_time_seconds", xlabel="Longitude", ylabel="dispatch_time_seconds")
    ax.scatter(data["lng"], data["dispatch_time_seconds"])
    fig.savefig("visuals/lngANDdispatch_time_seconds.png")

    fig, ax = plt.subplots()
    ax.set(title="ucr_general vs dispatch_hour", xlabel="ucr_general", ylabel="dispatch_hour")
    ax.scatter(data["ucr_general"], data["dispatch_hour"])
    fig.savefig("visuals/ucr_generalANDdispatch_hour.png")

    fig, ax = plt.subplots()
    ax.set(title="ucr_general vs Longitude", xlabel="ucr_general", ylabel="Longitude")
    ax.scatter(data["ucr_general"], data["lng"])
    fig.savefig("visuals/ucr_generalANDLongitude.png")

    fig, ax = plt.subplots()
    ax.set(title="Histogram of dispatch_month", xlabel="Month", ylabel="Count")
    ax.hist(data["dispatch_month"])
    fig.savefig("visuals/dispatch_month_hist.png")
