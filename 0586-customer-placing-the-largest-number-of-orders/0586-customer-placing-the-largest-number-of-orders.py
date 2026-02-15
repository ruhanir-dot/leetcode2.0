import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    filtered_df = pd.DataFrame(
        orders.groupby('customer_number').count()
    ).reset_index().sort_values(by = 'order_number', ascending = False).iloc[0:1]
    
    return filtered_df[['customer_number']]