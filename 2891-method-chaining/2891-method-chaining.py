import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(animals)
    df.sort_values('weight',ascending=False,inplace=True)
    df=df[df['weight']>100]
    return df[['name']]
    