import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler


def processing(data):
    data = data.copy()
    data = data[data["ucr_general"].isin([500, 600, 700, 1100, 1400, 1800])]
    data["dispatch_date_time"] = pd.to_datetime(data["dispatch_date_time"])
    data.set_index("dispatch_date_time")

    date_column = pd.to_datetime(data["dispatch_date"])
    data["dispatch_day_name"] = date_column.dt.day_name()
    data["dispatch_day"] = date_column.dt.day
    data["dispatch_month"] = date_column.dt.month
    data["dispatch_year"] = date_column.dt.year
    data["dispatch_time_seconds"] = pd.to_timedelta(data['dispatch_time']).dt.total_seconds()
    dt_obj = pd.to_datetime(data['dispatch_time']).dt
    data["dispatch_hour"] = dt_obj.hour
    data["dispatch_minute"] = dt_obj.minute
    data["dispatch_second"] = dt_obj.second

    data["psa"] = data["psa"].fillna("Unknown")

    latitude_imputer = KNNImputer(n_neighbors=5)
    data["lat"] = latitude_imputer.fit_transform(data["lat"].to_frame())

    longitude_imputer = KNNImputer(n_neighbors=5)
    data["lng"] = longitude_imputer.fit_transform(data["lng"].to_frame())

    for feature in ["dispatch_day", "dispatch_time_seconds"]:
        min_max_scaler = MinMaxScaler()
        data[feature] = min_max_scaler.fit_transform(data[feature].to_frame())

    for feature in ["lat", "lng"]:
        min_max_scaler = MinMaxScaler(feature_range=(-1,1))
        data[feature] = min_max_scaler.fit_transform(data[feature].to_frame())

    for feature in ["dispatch_day_name", "psa", "dc_dist"]:
        transformer = make_column_transformer(
            (OneHotEncoder(), [feature]),
            remainder='passthrough',
            verbose_feature_names_out=False
        )
        transformed = transformer.fit_transform(data)
        col_names = list(data.columns)
        col_names.remove(feature)
        data = pd.DataFrame(
            transformed,
            columns=transformer.get_feature_names_out()
        )

    return data
