BASE_DIR = "./benchmark_results"
PROCESSED_DIR = f"{BASE_DIR}/processed"
PLOTS_DIR = f"{BASE_DIR}/plots"
RAW_DIR = f"{BASE_DIR}/raw"
CONFIG_FILE_PATH = './config.json'

# length = length + 1 (for comma), example: "34.5ms," "10m0s"
MILLISECONDS_LENGTH = 3
MICROSECONDS_LENGTH = 3
SECONDS_LENGTH = 2
MINUTES_LENGTH = 4

NUMBER_OF_MS_IN_SECOND = 1000
NUMBER_OF_MICROSEC_IN_SECOND = 1000000
NUMBER_OF_SECONDS_IN_MINUTE = 60

TOO_MANY_REQUEST_ERROR = 429