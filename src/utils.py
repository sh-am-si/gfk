import pandas as pd
# import datetime

def prepare_df(droprows=None):

    data_file = '../data/test_data2.csv'

    df = pd.read_csv(data_file)

    df['period_end_date'] = pd.to_datetime(df['period_end_date'], errors='coerce')
    df['translated_when'] = pd.to_datetime(df['translated_when'], errors='coerce')

    columns_numerical_pwith_nan = ['delivery_type_id', 'predict_automatch', 'country_id_n']

    for column in columns_numerical_pwith_nan:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    col_with_nan = ['period_end_date', 'delivery_type_id', 'predict_automatch', 'country_id_n']
    if droprows:
        assert all([c in col_with_nan for c in droprows])
        df.dropna(axis=0, how='any', subset=droprows, inplace=True)

    return df