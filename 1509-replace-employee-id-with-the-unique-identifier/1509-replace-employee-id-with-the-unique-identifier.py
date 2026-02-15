import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.merge(employees, employee_uni, on = 'id', how = 'left')

    return output_df[['unique_id', 'name']]