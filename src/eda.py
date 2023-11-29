def analyze_df(df):
    """ Return basic analysis of DF """
    print(f'Number of rows: {df.shape[0]}, Number of columns:{df.shape[1]}')
    print(f'\nDuplicated amount: {df.duplicated().sum()}\n')
    print('-'*30 + 'Number of null values' +'-'*30)
    print(df.isna().sum())
    print('-'*30 + 'Type of variables' +'-'*30)
    print(df.dtypes)
    return df.head()