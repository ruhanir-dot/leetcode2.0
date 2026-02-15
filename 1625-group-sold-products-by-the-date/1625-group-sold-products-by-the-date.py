import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates(subset = ['sell_date', 'product'])
    filtered_df = pd.DataFrame(
        activities.groupby(['sell_date'])['product']
    ).drop(columns = 0).reset_index()

    filtered_df2 = pd.DataFrame(
        activities.groupby(['sell_date'])['product'].count()
    ).reset_index().reset_index()

    output_df = pd.merge(filtered_df, filtered_df2, on = 'index', how = 'outer').rename(
        columns = {
            1 : 'products',
            'product' : 'num_sold' 
        }
    )
    output_df['products'] = output_df['products'].apply(sorted).str.join(',')
    return output_df[['sell_date', 'num_sold', 'products']]