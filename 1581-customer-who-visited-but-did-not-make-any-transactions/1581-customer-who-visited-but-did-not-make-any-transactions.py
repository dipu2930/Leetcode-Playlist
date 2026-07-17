import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(visits)
    no_of_transaction=df[~df["visit_id"].isin(transactions["visit_id"])]
    res=no_of_transaction.groupby("customer_id").size().reset_index(name="count_no_trans")
    return res
    