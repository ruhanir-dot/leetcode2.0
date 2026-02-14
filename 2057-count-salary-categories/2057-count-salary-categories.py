import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    filtered_low = accounts[
        (accounts['income'] < 20000)
    ]
    low_count = len(filtered_low)

    filtered_avg = accounts[
        (accounts['income'] >= 20000) & 
        (accounts['income'] <= 50000)
    ]
    avg_count = len(filtered_avg)

    filtered_high = accounts[
        (accounts['income'] > 50000)
    ]
    high_count = len(filtered_high)

    output_df = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [ low_count, avg_count, high_count]
    })
    return output_df.sort_values(by = 'accounts_count', ascending = False)