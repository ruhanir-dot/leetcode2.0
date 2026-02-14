import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame: 
    employees['total_time'] = employees['out_time'] - employees['in_time'] 
    grouped_df = pd.DataFrame(
        employees.groupby(['emp_id', 'event_day'])['total_time'].sum()
    ).reset_index()    
    grouped_df = grouped_df.rename(columns = {
        'event_day':'day'
        })
    return grouped_df