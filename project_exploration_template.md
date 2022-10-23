#### SER594: Exploratory Data Munging and Visualization
#### Crime rate prediction from news tweets
#### Hariraj Venkatesan
#### 10/20/2022

## Basic Questions
**Dataset Author(s):** Ruchi Bhatia

**Dataset Construction Date:** 03/25/2020

**Dataset Record Count:** 24901

**Dataset Field Meanings:**
| Field | Description |
| ----- | ----------- |
| id    | Unique identifier of each tweet |
| conversation_id | Unique identifier to each conversation |
| created_at | Timestamp for creation |
| date  | Date of creation |
| time  | Time of creation |
| timezone | Timezone of tweet |
| user_id   | Unique identifier of tweet author |
| username | Username of tweet author |
| name | Name of tweet author |
| place | Location where tweet was posted |
| tweet | Content of tweet |
| language | Language of tweet content |
| mentions | Users mentioned in comment |
| urls  | URLs included in tweet content |
| photos | Images inserted in tweet content |
| replies_count | Number of replies |
| retweets_count | Number of retweets |
| likes_count | Number of likes |
| hashtags | Hashtags part of tweet content |
| cashtags | Company tickers part of tweet |
| link | Link to tweet |
| retweet | True if it is a retweet |
| quote_url | URL of quotes included in tweet content |
| video | 1 if video is included in tweet content, else 0 |
| thumbnail | URLs of thumbnail images part of tweet content |
| near | Location tags present in tweet |
| geo | Geographic coordinates of tweet location |
| source | Device type used for creating tweet |
| user_rt_id | IDs of retweeted users |
| user_rt | Users who retweeted |
| retweet_id | Unique identifier of retweets |
| reply_to | User to whom the tweet is being replied to |
| retweet_date | Date of retweet |
| translate | True if tweet is a translation |
| trans_src | Original language of translated tweet |
| trans_dest | Destination language of translated tweet |

**Dataset File Hash(es):**
- tweets_bbc.csv - a9d4e73b6e5e8bc6b1a143f94786cbab
- tweets_cnn.csv - 5d941c0a2c37eb2ae1ba8550fa545154
- tweets_eco.csv - 03f2e6f50d5fd013b3e7387b6f5a9012

## Interpretable Records
### Record 1
**Raw Data:**
id                                               1410283196890103810
conversation_id                                  1410283196890103810
created_at                                       2021-06-30 22:34:50
date                                             2021-06-30 00:00:00
time                                                        0.000081
timezone                                                         530
user_id                                                      5402612
username                                                 bbcbreaking
name                                               BBC Breaking News
tweet              us comedian bill cosbys sex assault conviction...
language                                                          en
mentions                                                            
urls                                               httpsbbcin364fdZq
photos                                                              
replies_count                                                    292
retweets_count                                                   405
likes_count                                                      825
hashtags                                                            
cashtags                                                            
link               httpstwittercomBBCBreakingstatus14102831968901...
retweet                                                        False
quote_url                                                        NaN
video                                                              0
thumbnail                                                        NaN
reply_to                                                            
tokens             [us, comedian, bill, cosbys, sex, assault, con...
cleaned_tokens     [u, comedian, bill, cosbys, sex, assault, conv...
cleaned_tweet      u comedian bill cosbys sex assault conviction ...
unique_words       [bill, court, pennsylvania, top, paving, comed...

**Interpretation:**
This tweet was created at 2021-06-30 22:34:50 by BBC Breaking News in English. It garnered 292 replies, 405 retweets and was liked by 825 people. It is about the court hearing against comedian Bill Cosbys for an alleged sexual assault case for which he was convicted. The high number of replies show that lot of people took interested and discussed the topic of the tweet.

### Record 2
**Raw Data:**
id                                               1387728889439457287
conversation_id                                  1387728889439457287
created_at                                       2021-04-29 16:52:04
date                                             2021-04-29 00:00:00
time                                                        0.000061
timezone                                                         530
user_id                                                      5988062
username                                                theeconomist
name                                                   The Economist
tweet              did the prime minister really need to spend 58...
language                                                          en
mentions                                                            
urls                                              httpseconst3vyhGpL
photos                                                              
replies_count                                                     10
retweets_count                                                    13
likes_count                                                       49
hashtags                                                            
cashtags                                                            
link               httpstwittercomTheEconomiststatus1387728889439...
retweet                                                        False
quote_url                                                        NaN
video                                                              0
thumbnail                                                        NaN
reply_to                                                            
tokens             [prime, minister, really, need, spend, 58000, ...
cleaned_tokens     [prime, minister, really, need, spend, 58000, ...
cleaned_tweet      prime minister really need spend 58000 redecor...
unique_words       [redecorating, flat, httpstcoevpvczxcyu, minis...

**Interpretation:** This tweet was posted by The Economist on 2021-04-29 at 4:52PM. It describes the actions of the prime misiter in spending $58,000 for redecoration purposes. It gathered only 10 replies, 49 likes and was retweeted only 13 times. The low numbers show that the people were not interested in the content of the tweet.

## Data Sources
- tweets_bbc.csv
    URL: https://www.kaggle.com/datasets/ruchi798/breaking-news-from-twitter-20102021
    MD5 hash: a9d4e73b6e5e8bc6b1a143f94786cbab
- tweets_cnn.csv
    URL: https://www.kaggle.com/datasets/ruchi798/breaking-news-from-twitter-20102021
    MD5 hash: 5d941c0a2c37eb2ae1ba8550fa545154
- tweets_eco.csv
    URL: https://www.kaggle.com/datasets/ruchi798/breaking-news-from-twitter-20102021
    MD5 hash: 03f2e6f50d5fd013b3e7387b6f5a9012

### Transformation 1
**Description:** Remove empty features

**Soundness Justification:** The following columns do not have any non-null values:
['place',
 'near',
 'geo',
 'source',
 'user_rt_id',
 'user_rt',
 'retweet_id',
 'retweet_date',
 'translate',
 'trans_src',
 'trans_dest']
 
Hence removing these features will not affect the dataset.

### Transformation 2
**Description:** Datatype conversions

**Soundness Justification:** The created_at and date features are stored as object columns which is very generic. Converting them to datetime values will enable date based operations on these columns.

### Transformation 3
**Description:** Filtering rows by date value in range 2021-01-01 to 2021-06-30

**Soundness Justification:** The minimum date value of the dataset is 2010-01-01 and the maximum value is 2021-07-02. We need records for a duration of 6 months as the sample data. So filtering the rows by date range will give the required rows.


## Visualization
### Visual 1
### Scatter plot of replies_count and likes_count
#### File: visuals/replies_countANDlikes_count.png
**Analysis:** There is high correlation between the replies and likes for most number of tweets. This proves that there is high dependency between these features when the number of replies is less than 4000 and likes is less than 50000. Thus tweets with high number of likes are expected to have high number of replies.

### Visual 2
### Scatter plot of replies_count and retweets_count
#### File: visuals/replies_countANDretweets_count.png
**Analysis:** There is high correlation between the replies and retweets. There is high dependency between these features when the number of replies is less than 3500 and retweets is less than 10000. Tweets with high number of replies are expected to be retweeted.

### Visual 3
### Scatter plot of retweets_count and likes_count
#### File: visuals/retweets_countANDlikes_count.png
**Analysis:** There is high correlation between retweets and likes. There is high dependency between these features when the number of likes is less than 30000 and retweets is less than 10000. Tweets with high number of likes are expected to be retweeted.

### Visual 4
### Histogram of unique words
#### File: visuals/unique_words.png
**Analysis:** This is a histogram of the 100 least frequent words that appeared tweets collected over BBC, CNN and The Economist after processing the tweets to remove stop words. Various examples are conviction, government, vaccine and study. The histogram shows that for the least 100 words the frequency is similar for all of them.
