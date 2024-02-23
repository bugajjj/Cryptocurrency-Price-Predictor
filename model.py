from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=30, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.4))
    model.add(LSTM(units=30, return_sequences=True))
    model.add(Dropout(0.4))
    model.add(LSTM(units=30))
    model.add(Dropout(0.4))
    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    return model
