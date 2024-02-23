import pandas as pd
from config import start, end, cryptofiat, value, prediction_days
import yfinance as yfin
import numpy as np

def predict_next_day_price(model, scaler, data):
    # Assuming 'data' is the historical data frame used for training
    start_test = end - pd.DateOffset(years=1)  # Adjust based on your requirement
    data_test = yfin.download(cryptofiat, start_test, end)
    actual_prices = data_test[value].values

    dataset_total = pd.concat((data[value], data_test[value]), axis=0)
    inputs = dataset_total[len(dataset_total) - len(data_test) - prediction_days:].values
    inputs = inputs.reshape(-1, 1)
    inputs = scaler.transform(inputs)

    real_data = [inputs[len(inputs) - prediction_days:len(inputs) + 1, 0]]
    real_data = np.array(real_data)
    real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

    prediction = model.predict(real_data)
    prediction = scaler.inverse_transform(prediction)

    return prediction
