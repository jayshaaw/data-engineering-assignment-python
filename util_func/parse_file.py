import pandas as pd


def parse_njson_file(file):
    df = pd.read_json(file, lines=True)

    """Name field"""
    # fix name field
    df['full_name'] = (df.loc[:, 'name']).apply(lambda x: x if type(x) != dict else (x['first'] + ' ' + x['last']))
    mask_na_name = df.full_name.isna()
    df.loc[mask_na_name, 'full_name'] = 'missing or invalid entries'
    # some name fields are empty
    df.full_name = df.full_name.str.strip()
    mask_empty_names = df.loc[:, 'full_name'] == ''
    df.loc[mask_empty_names, 'full_name'] = 'missing or invalid entries'

    """Value field"""
    # Extract numbers from Value field
    a = df['value'].str.extractall(r'(\d+)').droplevel(level='match')
    a = a.rename(columns={0: "value"})
    df = pd.merge(df, a, how='outer', left_index=True, right_index=True)
    df.loc[df.value_y.isna(), 'value_y'] = df.value_x
    df = df.rename(columns={"value_y": "value"}).drop(columns=["value_x", "name"])
    # some Value fields are NaN - fill them with 0
    mask_nan_value = (df.loc[:, 'value']) == ''
    df.loc[mask_nan_value, 'value'] = 0
    # some Value fields are na - fill them with 0
    df.value = df.value.fillna(0)
    # cast value field to int
    df.value = df.value.astype('int', copy=False)

    """Weight field"""
    # come Weight fields are na - fill them with 0
    df.weight = df.weight.fillna(0)
    # cast Weight field to int
    df.weight = df.weight.astype('int', copy=False)

    """Date field"""
    # normalize the date field to midnight
    df.date = df.date.dt.normalize()
    # some Date fields are na or null - set them to 2099 as outliers
    df.date = df.date.fillna('2099-01-01')

    """Description field"""
    # some Description fields are na or null - fill with missing description
    df.description = df.description.fillna('missing or invalid entries')
    # some Description fields have numeric entries
    mask_missing_invalid_desc = df.description.str.isnumeric().isna()
    df.loc[mask_missing_invalid_desc, 'description'] = 'missing or invalid entries'
    # some Description fields are empty
    df.description = df.description.str.strip()
    mask_empty_description = df.loc[:, 'description'] == ''
    df.loc[mask_empty_description, 'description'] = 'missing or invalid entries'
    # df.description.str.fullmatch(r'([0-9]*)')

    """Convert data types"""
    df = df.convert_dtypes()

    return df
