
#Model schema used to translate csv data into readable format

class PlayerContract:
    def __init__(self,
                 contract_id,
                 player_id,
                 player_name, 
                 player_dpm,
                 signing_date,
                 signing_team_id,
                 signing_team_name,
                 contract_cap_salary,
                 contract_tax_salary,
                 contract_total_salary,
                 overall_protection_coverage_lk,
                 skill_protection_amount_lk,
                 salary_year,
                 option_lk,
                 contract_type_lk,
                 contract_length):
        self.contract_id = contract_id
        self.player_id = player_id
        self.player_name = player_name
        self.player_dpm = player_dpm
        self.signing_date = signing_date
        self.signing_team_id = signing_team_id
        self.signing_team_name = signing_team_name
        self.contract_cap_salary = contract_cap_salary
        self.contract_tax_salary = contract_tax_salary
        self.contract_total_salary = contract_total_salary
        self.overall_protection_coverage_lk = overall_protection_coverage_lk
        self.skill_protection_amount_lk = skill_protection_amount_lk
        self.salary_year = salary_year
        self.option_lk = option_lk
        self.contract_type_lk = contract_type_lk
        self.contract_length = contract_length
	
    def __repr__(self):
        return f"{self.player_name}" #f"{self.player_name} ({self.position}) - {self.team}: {self.contract_years} years, ${self.total_salary} total (${self.annual_salary}/year)"
