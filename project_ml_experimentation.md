#### SER594: Experimentation
#### Classification of crimes in Philadelphia
#### Hariraj Venkatesan
#### 11/21/2022


## Explainable Records
### Record 1
**Raw Data:**

the_geom                0101000020E6100000A9EEFC68D9CF52C01CA7950084F1...
cartodb_id                                                         210205
the_geom_webmercator    0101000020110F0000CF182A5F34F45FC17876FBF9D97F...
objectid                                                           223360
dc_dist                                                                12
psa                                                                     1
dispatch_date_time                                    2022-08-22 18:31:00
dispatch_date                                                  2022-08-22
dispatch_time                                                    18:31:00
hour_                                                                 NaN
dc_key                                                       202212047884
location_block                                      8800 BLOCK BARTRAM AV
ucr_general                                                           600
text_general_code                                                  Thefts
point_x                                                        -75.247645
point_y                                                         39.886841
lat                                                             39.886841
lng                                                            -75.247645

**Prediction Explanation:**
The predicted class of crime is 600 i.e., Theft. This prediction can be explained with the time of crime, data for which is available from the dispatch_time_seconds feature. Theft is a common crime in the evening hours which matches with the time 18:31hrs. Also areas around the coordinates of (39, 75) seem to be largely affected by Theft.

### Record 2
**Raw Data:**

the_geom                0101000020E6100000B50B1703B5C252C09E833EC36103...
cartodb_id                                                         210730
the_geom_webmercator    0101000020110F0000A990659AE1DD5FC182F9A29CA593...
objectid                                                           222501
dc_dist                                                                15
psa                                                                     3
dispatch_date_time                                    2022-09-04 13:43:00
dispatch_date                                                  2022-09-04
dispatch_time                                                    13:43:00
hour_                                                                 NaN
dc_key                                                       202215064880
location_block                                   6900 BLOCK TORRESDALE AV
ucr_general                                                           300
text_general_code                                      Robbery No Firearm
point_x                                                        -75.042298
point_y                                                         40.026421
lat                                                             40.026421
lng                                                            -75.042298

**Prediction Explanation:**
The predicted class of crime is 0 i.e., Robbery No Firearm. This prediction can be explained using the psa_features that are expanded by one hot encoding. Areas that are covered under the police service area 3 appear to be mostly facing robbery related crimes either with or without a firearm. The time of crime which is afternoon 1pm also explains the robbery because it generally happens in daylight when people move in lonely places that are prone to attacks.  

## Interesting Features
### Feature A
**Feature:** Latitude

**Justification:** Latitude is a coordinate feature and helps locate any place uniquely. This will enable analysis of crimes that happen at the given location. 

### Feature B
**Feature:** dispatch_time_seconds

**Justification:** dispatch_time_seconds shows the time of the crime which will enable us to distinguish crimes that occur in daytime and compare it to night hours.

## Experiments 
### Varying latitude
**Prediction Trend Seen:**
As the latitude is moved from its minimum value to maximum value, the type of crime changes because the location is changed. This moves the area under consideration between different police service areas that face different crimes ranging from Burglary to Aggravated Assault and the number of crimes is uniform across the latitudes. 

### Varying dispatch_time_seconds
**Prediction Trend Seen:**
As the values of dispatch_time_seconds are moved from its minimum to maximum value, the predominant type of crime changes only across few labels as the location is fixed. However, the count of crimes increases in a linear manner as the time value moves from daytime to night.

### Varying latitude and dispatch_time_seconds together
**Prediction Trend Seen:**
When both latitude and dispatch_time_seconds are changed, the maximum occurring label of crime changes with the value increasing across all labels. This is explained by the contribution of both latitude in terms of the type of crime and dispatch_time_seconds that contributes mostly to the number of crimes.

### Varying A and B inversely
**Prediction Trend Seen:**
When both latitude and dispatch_time_seconds are changed inversely, both the type of crime and maximum number of crimes vary due to the contribution of both the features.
