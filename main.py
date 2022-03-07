from GoogleNews import GoogleNews

import pandas as pd
from datetime import datetime, timedelta
from pytz import timezone

#GET A PERIOD OF TIME
est = timezone('EST')
today = datetime.now(est)
yesterday = today - timedelta(days=1)

print("Today's date:", today)
print("Yesterday's  date:", yesterday)

#SET THE DATE RANGE
googlenews=GoogleNews(start=yesterday.strftime("%m-%d-%Y"),end=today.strftime("%m-%d-%Y"))
#SET THE LANGUAGE
googlenews.set_lang('en')
#SET THE TOPIC
googlenews.search('Breaking News')
#GET THE NEWS
result=googlenews.result()
#CONVERT THE RESULT TO A PANDAS DATAFRAME
df=pd.DataFrame(result)

print(df)