import datetime as dt
from dates import req_dates

today = dt.date.today()

for date in req_dates:
	if date == str(today):
		# Run Script