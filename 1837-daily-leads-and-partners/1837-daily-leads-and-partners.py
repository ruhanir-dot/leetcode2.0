import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_unique_leads = pd.DataFrame(
        daily_sales.drop_duplicates(subset =['date_id', 'make_name','lead_id'])
        .groupby(['make_name','date_id'])
        .agg(
            unique_leads = ('lead_id', 'count'),
        )
        ).reset_index().reset_index()
    daily_unique_partners = pd.DataFrame(
        daily_sales.drop_duplicates(subset =['date_id', 'make_name','partner_id'])
        .groupby(['make_name','date_id'])
        .agg(
            unique_partners = ('partner_id', 'count'),
        )
        ).reset_index().reset_index()
    
    output_df = pd.merge(daily_unique_leads, daily_unique_partners, on = 'index', how = 'left').rename(
        columns = {
            'date_id_x' : 'date_id', 
            'make_name_x' : 'make_name'
        }
    )
    return output_df[['date_id', 'make_name', 'unique_leads', 'unique_partners']]