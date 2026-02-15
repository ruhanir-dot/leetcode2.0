import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    filtered_df = actor_director.groupby(['actor_id', 'director_id']).aggregate({
        'timestamp' : 'count'
    }).reset_index()

    filtered_df  = filtered_df[
        filtered_df['timestamp'] >= 3
    ]

    return filtered_df[['actor_id', 'director_id']]