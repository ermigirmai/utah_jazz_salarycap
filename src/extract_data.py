import pandas as pd
from player_contract_model import PlayerContract 

def get_raw_data_location():
    file_path = "contract_data.csv"
    if file_path is None:
        # Prompt the user to enter the file path if csv file is not hardcoded
        file_path = input("Please enter the path to the CSV file: ")
    return file_path

def extract_raw_data(file_path):
    local_file_path = "../data/"+file_path
    try:
        df = pd.read_csv(local_file_path)
        contracts = []
        for _, row in df.iterrows():
            contract = PlayerContract(
                contract_id = row["CONTRACT_ID"],
                player_id = row["PLAYER_ID"],
                player_name = row["FULL_NAME"], 
                player_dpm = row["DPM"],
                signing_date = row["SIGNING_DATE"],
                signing_team_id = row["SIGNING_TEAM_ID"],
                signing_team_name = row["TEAM_FULL_NAME"],
                contract_cap_salary = row["CONTRACT_CAP_SALARY"],
                contract_tax_salary = row["CONTRACT_TAX_SALARY"],
                contract_total_salary = row["TOTAL_SALARY"],
                overall_protection_coverage_lk = row["OVERALL_PROTECTION_COVERAGE_LK"],
                skill_protection_amount_lk = row["SKILL_PROTECTION_AMOUNT"],
                salary_year = row["SALARY_YEAR"],
                option_lk = row["OPTION_LK"],
                contract_type_lk = row["CONTRACT_TYPE_LK"],
                contract_length = row["CONTRACT_LENGTH"]
            )
            contracts.append(contract)
        return contracts
    
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
