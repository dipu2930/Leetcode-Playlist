import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employees)
    first_three=df.head(3)
    return first_three
    