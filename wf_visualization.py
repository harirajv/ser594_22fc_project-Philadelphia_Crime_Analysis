import pandas as pd
import os
import matplotlib.pyplot as plt

quantitative_features = ["replies_count", "retweets_count", "likes_count"]

def summary_statistics(data):
    for ft in quantitative_features:
        print("\nFeature: ", ft)
        print("Min: ", min(data[ft]))
        print("Max: ", max(data[ft]))
        print("Median: ", data[ft].median())

    uniq_words = []
    data.unique_words.map(lambda x:uniq_words.extend(x))
    uniq_words = pd.Series(uniq_words)
    counts = uniq_words.value_counts()
    print("Number of unique words: ", len(counts))
    print("Most frequent: ", counts.index[0])
    print("Least frequent: ", counts.index[-1])

def correlation(data):
    print(data[quantitative_features].corr())

def scatter_plots(data):
    fig, ax = plt.subplots()
    ax.set(title="replies_count vs retweets_count", xlabel="replies_count", ylabel="retweets_count")
    ax.scatter(data["replies_count"], data["retweets_count"])
    ax.legend()
    fig.savefig("visuals/replies_countANDretweets_count.png")

    fig, ax = plt.subplots()
    ax.set(title="replies_count vs likes_count", xlabel="replies_count", ylabel="likes_count")
    ax.scatter(data["replies_count"], data["likes_count"])
    ax.legend()
    fig.savefig("visuals/replies_countANDlikes_count.png")

    fig, ax = plt.subplots()
    ax.set(title="retweets_count vs likes_count", xlabel="retweets_count", ylabel="likes_count")
    ax.scatter(data["retweets_count"], data["likes_count"])
    ax.legend()
    fig.savefig("visuals/retweets_countANDlikes_count.png")
