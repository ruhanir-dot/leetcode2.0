import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee['name'] = employee['name'].fillna('Name')
    manager_count = employee.groupby('managerId').aggregate(
        cnt = ('name', 'count')
    ).reset_index().rename(columns = {
        'managerId' : 'id'
    })

    output_df = pd.merge(employee, manager_count, on = 'id', how = 'inner')
    final_df = output_df[
        output_df['cnt'] >= 5
    ]
    final_df['name'] = final_df['name'].replace('Name', np.nan)
    return final_df[['name']]