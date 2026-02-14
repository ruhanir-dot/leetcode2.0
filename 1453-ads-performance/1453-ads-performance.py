import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads_unique = ads['ad_id'].unique()

    clicks_df= pd.DataFrame(
        ads[ads['action'] == 'Clicked'].groupby('ad_id').size().reset_index(name = 'click_count')
        )

    views_df = pd.DataFrame(
        ads[ads['action'] == 'Viewed'].groupby('ad_id').size().reset_index(name = 'views_count')
    )

    final_df = pd.DataFrame({
        'ad_id' : ads_unique
    })

    final_df = pd.merge(final_df, clicks_df, on = 'ad_id', how = 'outer')
    final_df = pd.merge(final_df, views_df, on = 'ad_id', how = 'outer')
    final_df = final_df.fillna(0)

    final_df['ctr'] = round( ((final_df['click_count'] / (final_df['click_count'] + final_df['views_count'])) * 100), 2 
    )
    
    final_df = final_df.fillna(0)

    result = final_df[['ad_id', 'ctr']].sort_values(
        by=['ctr', 'ad_id'], 
        ascending=[False, True]
    )

    return result