from data_preparation import download_and_prepare_data
from model import create_model
from predict import predict_next_day_price
from twitter_api import post_content
from config import cryptofiat

if __name__ == '__main__':
    x_train, y_train, scaler, data = download_and_prepare_data()
    model = create_model(input_shape=(x_train.shape[1], 1))
    model.fit(x_train, y_train, epochs=30, batch_size=64)

    # Example call within main.py
    # This assumes you've already loaded or defined `data`, `model`, and `scaler` appropriately
    prediction = predict_next_day_price(model, scaler, data)
    status = f"Predicted price for {cryptofiat} is: ${prediction[0][0]:.2f} (This is a model prediction, not financial advice)"
    post_content(status)
