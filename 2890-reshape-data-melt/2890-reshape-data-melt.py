import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(report)
    melted_df=df.melt(
        id_vars='product',
        var_name='quarter',
        value_name='sales'
    )
    return melted_df
    