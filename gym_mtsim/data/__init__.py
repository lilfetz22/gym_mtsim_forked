import os


DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FOREX_DATA_PATH = os.path.join(DATA_DIR, 'symbols_forex.pkl')
FOREX_DATA_PATH_TRAIN = os.path.join(DATA_DIR, 'symbols_forex_1_1_20_12_31_23.pkl')
FOREX_DATA_PATH_TEST = os.path.join(DATA_DIR, 'symbols_forex_1_1_24_4_11_24.pkl')
STOCKS_DATA_PATH = os.path.join(DATA_DIR, 'symbols_stocks.pkl')
CRYPTO_DATA_PATH = os.path.join(DATA_DIR, 'symbols_crypto.pkl')
MIXED_DATA_PATH = os.path.join(DATA_DIR, 'symbols_mixed.pkl')