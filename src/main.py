from extract_data import extract_raw_data, get_raw_data_location
from transform_data import transform_contracts_data
from clean_data import clean_raw_data
from visualize_data import split_data_and_plot

def main():

    ### FIND RAW DATA SOURCE
    raw_data_location = get_raw_data_location()
    
    ### EXTRACT RAW DATA
    raw_contracts_list = extract_raw_data(raw_data_location)
    
    ### CLEAN DATA
    cleaned_contracts_dict = clean_raw_data(raw_contracts_list)

    ### TRANSFORM DATA
    transformed_contracts_by_year = transform_contracts_data(cleaned_contracts_dict)

    ### VISUALIZE DATA
    split_data_and_plot(transformed_contracts_by_year)

if __name__ == "__main__":
    main()
