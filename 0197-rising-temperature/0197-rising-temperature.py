import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate",inplace=True)
    date_diff=weather["recordDate"].diff().dt.days
    temp_diff=weather["temperature"].diff()
    rising_temp=weather[(date_diff==1)&(temp_diff>0)]
    return rising_temp[['id']]
    