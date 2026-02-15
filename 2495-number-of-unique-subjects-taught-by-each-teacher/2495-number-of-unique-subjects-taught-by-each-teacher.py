import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher_filter = teacher.drop_duplicates(['teacher_id', 'subject_id'])
    filtered_df = pd.DataFrame( 
        teacher_filter.groupby('teacher_id')['subject_id'].count()
    ).reset_index()
    filtered_df = filtered_df.rename(columns = {
        'subject_id' :  'cnt'
        })
    return filtered_df