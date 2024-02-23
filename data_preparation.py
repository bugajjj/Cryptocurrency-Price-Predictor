import yfinance as yfin
from sklearn.preprocessing import MinMaxScaler
from config import start, end, cryptofiat, value, prediction_days
import numpy as np

yfin.pdr_override()

def download_and_prepare_data():
    data = yfin.download(cryptofiat, start, end)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[value].values.reshape(-1, 1))

    x_train, y_train = [], []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x - prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    return x_train, y_train, scaler, data
