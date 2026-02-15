import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame: 
    filtered_df = pd.DataFrame(
        courses.groupby('class').count()
    ).reset_index()

    final_df = filtered_df[
        filtered_df['student'] >= 5
    ]

    return  final_df[['class']]

