# Cryptocurrency Price Prediction

## Project Overview
This project is aimed at predicting cryptocurrency prices using historical price data. It utilizes a deep learning approach, specifically Long Short-Term Memory (LSTM) networks, to model and forecast the future prices of cryptocurrencies like Ethereum (ETH) against the USD.

## Features
- **Data Preparation:** Downloads historical cryptocurrency data.
- **Model Training:** Utilizes LSTM networks to learn from past price movements.
- **Price Prediction:** Predicts the next day's price based on learned patterns.
- **Twitter Integration:** Posts predictions automatically to Twitter.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- pip and virtualenv
- A Twitter Developer account and API keys if you wish to use the Twitter posting feature.

## Installation
To install the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptocurrency-prediction.git
   ```
2. Navigate into the project directory:
   ```bash
   cd cryptocurrency-prediction
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Before running the project, you need to set up your environment variables for Twitter API access:
1. Create a `.env` file in the project root.
2. Add your Twitter API keys and tokens:
   ```plaintext
   API_KEY=yourapikey
   API_SECRET=yourapisecret
   ACCESS_TOKEN=youraccesstoken
   ACCESS_SECRET=youraccesssecret
   ```

## Usage
To use the project, follow these steps:

1. Run the main script to start the prediction and posting process:
   ```bash
   python main.py
   ```
2. Check your console for logs and Twitter for the posted prediction.

## Contributing
Contributions to this project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
Distributed under the BSD License. See `LICENSE` for more information.

## Contact
Your Name - [@bugajj_eth](https://twitter.com/bugajj_eth)

Project Link: [https://github.com/bugajjj/Cryptocurrency-Price-Predictor](https://github.com/bugajjj/Cryptocurrency-Price-Predictor)