import os


DATA_DIR = os.path.dirname(os.path.abspath(__file__))

FOREX_DATA_PATH = os.path.join(DATA_DIR, 'symbols_forex.pkl')
FOREX_DATA_PATH_PRODUCTION = os.path.join(DATA_DIR, 'symbols_forex_production.pkl')
FOREX_DATA_PATH_PRODUCTION_MS = os.path.join(DATA_DIR, 'symbols_forex_production_ms.pkl')
FOREX_DATA_PATH_PRODUCTION_TESTING = os.path.join(DATA_DIR, 'symbols_forex_production_testing.pkl')
FOREX_DATA_PATH_TRAIN = os.path.join(DATA_DIR, 'symbols_forex_1hr_1_1_10_5_3_24.pkl')
FOREX_DATA_PATH_TEST = os.path.join(DATA_DIR, 'symbols_forex_1_1_24_4_11_24.pkl')
STOCKS_DATA_PATH = os.path.join(DATA_DIR, 'symbols_stocks.pkl')
CRYPTO_DATA_PATH = os.path.join(DATA_DIR, 'symbols_crypto.pkl')
MIXED_DATA_PATH = os.path.join(DATA_DIR, 'symbols_mixed.pkl')
# MODEL_PATH = os.path.join(DATA_DIR, 'model_0.pkl')
MODEL_PATH = os.path.join(DATA_DIR, 'model_89_2024-05-17.pkl')
FOREX_DATA_PATH_1HR = os.path.join(DATA_DIR, 'symbols_forex_1hr_2008-05-19_2024-05-08')
FOREX_DATA_PATH_15MIN = os.path.join(DATA_DIR, 'symbols_forex_15min_2020-05-11_2024-05-08')
FOREX_DATA_PATH_5MIN = os.path.join(DATA_DIR, 'symbols_forex_5min_2023-01-09_2024-05-08')