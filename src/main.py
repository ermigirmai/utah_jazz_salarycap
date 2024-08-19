from src.csv_reader import read_csv

def main():
    # Prompt the user to enter the file path
    file_path = input("Please enter the path to the CSV file: ")
    
    # Read the CSV file
    df = read_csv(file_path)
    
    # Check if the DataFrame is not empty and print the first few rows
    if df is not None:
        print(df.head())  # Print the first few rows of the DataFrame

if __name__ == "__main__":
    main()
