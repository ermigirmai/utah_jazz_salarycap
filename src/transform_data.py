from constants import salary_caps
from itertools import islice

#Data transformation entry point
def transform_contracts_data(contracts):
    results = {}

    for salary_year, contracts_by_year in contracts.items():
        if not is_contract_year_valid(salary_year):
                continue
        
        for contract_id, contract in contracts_by_year.items():
            if salary_year not in results:
                results[contract["salary_year"]] = {}

            contract_with_percent_cap = add_percent_of_cap_to_contract(contract, contract["salary_year"])
            results[contract["salary_year"]][contract_id] = contract_with_percent_cap

    transformed_contracts = filter_noisy_data(results)
    return transformed_contracts

#Method to append the % of cap value of a contract based on salary cap for that year
def add_percent_of_cap_to_contract(contract, contract_year):

    contract_percent_cap = calc_percent_of_cap(contract["contract_cap_salary"], contract_year)
    if contract_percent_cap < 1.0:
        #Categorizing contracts with less than 1.0% cap hit as noisy
        return None
    else:
        contract["contract_percent_cap"] = contract_percent_cap

    return contract

#Method to split DPM and % of cap data points of each contract for analysis (cleaning noisy transformed data)
def filter_noisy_data(contracts):

    filtered_contracts = {}

    for salary_year, contracts_by_year in contracts.items():
        filtered_contracts[salary_year] = {}

        for contract_id, contract in contracts_by_year.items():
            if contract is not None:
                # Check if the required keys DPM and % of cap are present
                if 'player_dpm' not in contract:
                    if 'contract_percent_cap' not in contract:
                        print(f"Missing required keys in contract: {contract_id}")
                        continue

                # Extract the DPM and % of cap of each contract
                filtered_contracts[salary_year][contract_id] = {
                    'player_dpm': contract['player_dpm'],
                    'percent_of_cap': contract['contract_percent_cap']
                }

    return filtered_contracts

#Method to validate contract's year is between our window of interest 2011-2029
def is_contract_year_valid(year):
    if year >= 2011 and year <= 2029:
        return True
    return False

#Method to calculate contract's percent of cap
def calc_percent_of_cap(salary, year):
    return 100*(salary/salary_caps[year])