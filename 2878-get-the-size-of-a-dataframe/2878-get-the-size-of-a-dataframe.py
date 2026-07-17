import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players)
    rows,cols=df.shape
    result=[rows, cols]
    return result
    