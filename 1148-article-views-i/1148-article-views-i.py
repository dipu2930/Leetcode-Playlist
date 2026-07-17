import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(views)
    res=df[df["author_id"]==df["viewer_id"]][["author_id"]].sort_values("author_id").drop_duplicates()
    res=res.rename(columns={"author_id":"id"})
    return res
    