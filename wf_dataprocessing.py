import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def processing(data):
    # Remove empty features
    empty_features = list(data.columns[data.isnull().all()])

    for col in empty_features:
        data.drop(col, axis=1, inplace=True)

    datetime_columns = ["created_at", "date"]

    for col in datetime_columns:
        data[col] = pd.to_datetime(data[col])

    for col in datetime_columns:
        data['time'] = pd.to_timedelta(data.time).dt.total_seconds()

    data = data.loc[(data.date>='2021-01-01') & (data.date<='2021-06-30')]

    data['tweet'] = data.tweet.str.lower()
    data = data.replace(to_replace=r'[^\w\s]', value='', regex=True)

    data['tokens']=data.tweet.apply(word_tokenize)

    stopwords_set = set(stopwords.words('english'))
    data['tokens'] = data.tokens.apply(lambda token_words:[word for word in token_words if word not in stopwords_set])

    wnl = WordNetLemmatizer()
    data['cleaned_tokens'] = data.tokens.apply(lambda tokens:[wnl.lemmatize(token) for token in tokens])
    data['cleaned_tweet'] = data.cleaned_tokens.apply(lambda tokens:" ".join(tokens))

    data.index += 1

    return data
