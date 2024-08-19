import pandas as pd

def read_csv(file_path):
    """Reads a CSV file and returns a DataFrame."""
    local_file_path = "./data/"+file_path
    try:
        df = pd.read_csv(local_file_path)
        return df
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
