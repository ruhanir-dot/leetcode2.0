import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(subset = ['sell_date', 'product'])
    activities = activities.sort_values(by = ['sell_date', 'product'])

    result_df = pd.DataFrame(
        activities.groupby('sell_date').aggregate(
            num_sold = ('product', 'count'),
            products = ('product', ','.join)
        )
        ).reset_index()

    return result_df