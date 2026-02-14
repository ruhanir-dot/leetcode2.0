import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    filtered_df = delivery[
        (delivery['customer_pref_delivery_date'] == delivery['order_date'])
    ]
    percentage = (len(filtered_df) / len(delivery)) * 100
    immediate_df = pd.DataFrame({'immediate_percentage' : [round(percentage, 2)] })

    return immediate_df