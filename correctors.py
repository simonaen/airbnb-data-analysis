def remove_zero(df, col_names):
    for col_name in col_names:
        new = df[df[col_name] != 0]
    return new

def zero_to_third_quartile_corrector(df, col, third):
    new = df[col].between(0, third)
    corrected = df.loc[new, col]
