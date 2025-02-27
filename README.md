# Bitcoin Timeframe Tracker

A Python application that automatically collects Bitcoin price data across multiple timeframes from Binance and organizes it into an Excel spreadsheet. This tool is useful for cryptocurrency traders and analysts who need to track Bitcoin price movements across different time intervals.

## Features

- Collects real-time BTC/USDT trading data from Binance
- Tracks data across 14 different timeframes (1m to 1w)
- Stores OHLCV (Open, High, Low, Close, Volume) data in a structured Excel file
- Automatically updates at appropriate intervals for each timeframe
- Timestamp conversion to human-readable format
- Centered formatting in Excel for improved readability

## Requirements

- Python 3.6+
- Required packages:
  - openpyxl
  - ccxt
  - time
  - datetime

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/bitcoin-timeframe-tracker.git
   cd bitcoin-timeframe-tracker
   ```

2. Install required packages:
   ```
   pip install openpyxl ccxt
   ```

3. Run the application:
   ```
   python BitcoinTimeframeTracker.py
   ```

## How It Works

The application connects to the Binance API through the CCXT library and retrieves the latest OHLCV data for BTC/USDT in the following timeframes:
- 1 minute
- 3 minutes
- 5 minutes
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours
- 4 hours
- 6 hours
- 8 hours
- 12 hours
- 1 day
- 3 days
- 1 week

Each timeframe's data is collected at appropriate intervals and stored in a dedicated section of the Excel spreadsheet. The data includes timestamp, open price, high price, low price, close price, and trading volume.

## Excel Output Structure

The Excel file is organized with each timeframe having its own column group with the following headers:
- Timestamp
- Open
- High
- Low
- Close
- Volume

## Usage

Once running, the program will:
1. Initialize an Excel workbook with appropriate headers
2. Connect to Binance and begin retrieving BTC/USDT price data
3. Update the Excel file at appropriate intervals
4. Continue running until manually stopped

The resulting Excel file will be saved as "DATA_crypto.xlsx" in the same directory as the script.

## Customization

You can modify the code to:
- Track different cryptocurrencies by changing the `symbol` variable
- Add additional timeframes by updating the `timeframes` dictionary
- Modify the update intervals by adjusting the timing logic in the `appel_fonction` function

## Disclaimer

This tool is for educational and research purposes only. Cryptocurrency trading involves significant risk. Always do your own research before making investment decisions.

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
