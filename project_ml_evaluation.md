#### SER594: Machine Learning Evaluation
#### Classification of crimes in Philadelphia
#### Hariraj Venkatesan
#### 11/21/2022

## Evaluation Metrics
### Metric 1
**Name:** Accuracy

**Choice Justification:**

Accuracy describes the performance of the model across both positive and negative samples. In this multi-class classification problem, this will be helpful in measuring the ability of the model in predicting the most appropriate label for the crime and not predicting the wrong label when similar time and location data is given. 

**Interpretation:**

The accuracy for each of the model's predictions is calculated and RandomForestClassifier achieves the highest accuracy for a maximum depth set to 32. This shows that the coordinate based features and time based features enable the model to make decisions at each level of the tree and use it in an one-vs-all manner for multi-class classification.

### Metric 2
**Name:** Precision

**Choice Justification:**

Precision describes the performance of the model in predicting the positive labels. In the multi-class classification, this metric will be useful in determining the model's ability in predicting the correct label for the given record. 

**Interpretation:**

The precision for each of the model's predictions is calculated and RandomForestClassifier achieves the highest precision for a maximum depth set to 32. This justifies that each of the trees in the forest avoid the negative samples and are able to predict the correct label.

## Alternative Models
### Alternative 1
**Construction:** KNN classifier that use 8 neighbors

**Evaluation:**

The model is evaluated using accuracy and precision of predictions on the test set.
This model scored accuracy and precision values of 0.279 and 0.068 respectively.

### Alternative 2
**Construction:** KNN classifier that uses 10 neighbors

**Evaluation:**

The model is evaluated using accuracy and precision of predictions on the test set.
This model scored accuracy and precision values of 0.287 and 0.069 respectively.

### Alternative 3
**Construction:** Random Forest classifier with maximum depth of tree set to 32

**Evaluation:**

The model is evaluated using accuracy and precision of predictions on the test set.
This model scored accuracy and precision values of 0.339 and 0.287 respectively.

## Visualization
### Visual 1
### Scatter plot of Latitudes and Longitudes
#### File: visuals/latANDlng.png
**Analysis:** There is high correlation between the latitude and longitude of the location where the crime occurred. However, there exist values in both features that contribute to both linear and inverse linear correlation.

### Visual 2
### Scatter plot of Latitudes and dispatch_time_seconds
#### File: visuals/latANDdispatch_time_seconds.png
**Analysis:** The scatterplot does not fit any polynomial function. This shows that the latitude and time of crime have very minimal correlation.

### Visual 3
### Scatter plot of Longitudes and dispatch_time_seconds
#### File: visuals/lngANDdispatch_time_seconds.png
**Analysis:** The scatterplot does not fit any polynomial function. This shows that the longitude and time of crime have very minimal correlation.

### Visual 4
### Histogram of unique words
#### File: visuals/dispatch_month_hist.png
**Analysis:** This is a histogram of the feature dispatch_month. It shows that the highest number of crimes were recorded in the 11th month i.e., November and the lowest number of crimes were recorded in the 3rd month i.e., March.

## Best Model

**Model:** Random Forest classifier with maximum depth of tree set to 32