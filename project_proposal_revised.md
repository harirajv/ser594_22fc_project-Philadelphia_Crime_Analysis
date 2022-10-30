### Title: Crime rate prediction from news tweets
### Author: Hariraj Venkatesan
### Date: 10/30/2022

Keywords: Crime analysis, Forecasting, Regression

### Description:
Crime is one of the biggest dangers to a peaceful society and is a serious obstacle to harmonious living. Accurate crime forecasting will aid law enforcement authorities in formulating plans to increase public safety. It has been difficult for the scientific community to create precise prediction tools for this purpose since the crime rate depends on several variables. This project seeks to forecast crime rates by utilizing the vast volumes of data present in the mammoth social media platform Twitter. The approach involves using tweets from reliable news organizations to predict the trend of crime rates in the future based on instances from the past. Using this, we will be able to answer questions about the events that result in increased criminal activity and the efficacy of law enforcement measures in lowering crime rates. The training set will include all news tweets published by the news organization, including those on droughts, political rebellion against the ruling party, constructive measures like anti-drug campaigns and rehabilitation camps. The number of tweets about criminal incidents will be the target feature.

### Research questions:

* RO1: To capture the trends in crime rates using tweets of news headlines

* RO2: To predict the number of crime related tweets as an indicator to the rate of crime in a given duration.

* RO3: To defend the ability of the model in generating predictions that achieve RO2.

* RO4: To evaluate the causality among the features that lead to increase in trends of crime related news tweets.

### Intellectual Merit:
The results derived from this project will be useful in determining the events that lead to increase in crime such as inflation, increase in drug abuse or political revolts. When a combination of crime-causing events occurs, we will be able to plan for proactive measures such as increasing police surveillance in vulnerable areas. The results from the model will also provide insight about the efficiency of the various initiatives conducted by law enforcement agencies such as providing medical counselling to socially oppressed people to prevent them from indulging in malicious activities. The insights will be useful in enhancing such programs and planning future initiatives that will be effective in preventing crimes such as robbery or shootouts.

### Data Sourcing:
We will use the [`Breaking News from Twitter 2010-2021`](https://www.kaggle.com/datasets/ruchi798/breaking-news-from-twitter-20102021) dataset created by `RUCHI BHATIA`. This dataset contains tweets posted by the official handles of BBC, CNN and the Economist from the year 2010 to 2021. For this project we will only need tweets within the date range of January 1 to June 30 of the year 2021. We will extract the relevant tweets using the date feature and perform preprocessing on the extracted data.

### Related Work:
* Tarlekar, S., Bhosle, R., D’souza, E., & Sheikh, S. (2021). Geographical Crime Rate Prediction System. In 2021 IEEE India Council International Subsections Conference (INDISCON). 2021 IEEE India Council International Subsections Conference (INDISCON). IEEE. https://doi.org/10.1109/indiscon53343.2021.9582218.
* Tarlekar, S., Bhosle, R., D’souza, E., & Sheikh, S. (2021). Geographical Crime Rate Prediction System. In 2021 IEEE India Council International Subsections Conference (INDISCON). 2021 IEEE India Council International Subsections Conference (INDISCON). IEEE. https://doi.org/10.1109/indiscon53343.2021.9582218.
* Lydia Jane G.,, & Hari, S. (2021). Crime Prediction Using Twitter Data. International Journal of e-Collaboration (IJeC), 17(3), 62-74. http://doi.org/10.4018/IJeC.2021070104
* Aghababaei, S., & Makrehchi, M. (2018). Mining Twitter data for crime trend prediction. In Intelligent Data Analysis (Vol. 22, Issue 1, pp. 117–141). IOS Press. https://doi.org/10.3233/ida-163183
* Wang, X., Gerber, M.S., Brown, D.E. (2012). Automatic Crime Prediction Using Events Extracted from Twitter Posts. In: Yang, S.J., Greenberg, A.M., Endsley, M. (eds) Social Computing, Behavioral - Cultural Modeling and Prediction. SBP 2012. Lecture Notes in Computer Science, vol 7227. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-29047-3_28