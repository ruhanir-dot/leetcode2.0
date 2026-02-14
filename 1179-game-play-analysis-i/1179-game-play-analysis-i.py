import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by = 'event_date')
    filter_df = pd.DataFrame(
        activity.groupby(['player_id'])['event_date'].first()
    ).reset_index()

    filter_df = filter_df.rename(columns = {
        'event_date' : 'first_login'
    })
    return filter_df