from constants import beginning_date_datetime, datetime_format_Ymd
from datetime import datetime
from itertools import islice

def clean_raw_data(raw_contracts_list):
    
    if (raw_contracts_list is not None) and (len(raw_contracts_list) > 0):

        cleaned_contracts_dict = {}
        contracts_processed = {} #Mapping used to keep track of contracts already processed to clean out duplicates

        for contract in raw_contracts_list:
            signing_date = convert_to_datetime(contract.signing_date)
            
            if (signing_date >= beginning_date_datetime) and (contract.contract_cap_salary > 0) and (not is_duplicate_contract(contracts_processed, contract)):
                '''Cleaning criteria is 3-fold:
                   1. Was contract signed on or after December 01, 2011?
                   2. Does contract hold a cap hit?
                   3. Is contract being processed already processed based on a composite value (i.e. same player signing same contract type on the same day for the same salary year for the same team)
                '''

                if contract.salary_year not in cleaned_contracts_dict:
                    cleaned_contracts_dict[contract.salary_year] = {}

                if contract.contract_id not in cleaned_contracts_dict[contract.salary_year]:
                    cleaned_contracts_dict[contract.salary_year][contract.contract_id] = {}

                cleaned_contracts_dict[contract.salary_year][contract.contract_id] = contract.__dict__

                #Bookkeeping logic to catch duplicates
                if contract.player_name not in contracts_processed:
                    contracts_processed[contract.player_name] = set()
                contracts_processed[contract.player_name].add(get_year_team_date_composite_value(contract))

    return cleaned_contracts_dict

#Method to convert string date to datetime type to evaluate contract signing date
def convert_to_datetime(date_str):
    return datetime.strptime(date_str, datetime_format_Ymd)

#Method to clean up duplicate contract entries
def is_duplicate_contract(contracts_processed, contract):
    year_and_team_composite = get_year_team_date_composite_value(contract)
    if (contract.player_name in contracts_processed) and (year_and_team_composite in contracts_processed[contract.player_name]):
        return True
    else:
        return False
    
#Utility method to determine arbitrary composite value for duplicate entry identification
def get_year_team_date_composite_value(contract):
    return str(contract.salary_year)+"/"+str(contract.signing_team_id)+"/"+contract.signing_date