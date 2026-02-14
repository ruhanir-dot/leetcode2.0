import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    filtered_df = pd.DataFrame(store[
        (store['amount'] > 500)
    ].groupby(by = 'customer_id')['bill_id'].count())

    rich_df = pd.DataFrame()
    rich_df['rich_count'] = filtered_df.count()

    return rich_df    