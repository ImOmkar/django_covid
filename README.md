# django_covid
COVID-19 DATA API
This package makes COVID-19 data available through python API. All the data are directy taken from the CSSEGISandData-covi19 with the below mentioned data sources. There are several methods to extract the statistics and counts for the coutry or province.

Installation:
Also available in pypi:
covid-data-api

How to user:
Initialising the instance/api:
from covid.api import CovId19Data

api = CovId19Data(force=False)
If force = True, every time object is instantiated new data is downloaded. Otherwise data will be refreshed after 24 hrs.

Method 1: Get stats:
Get the latest total stats for all confirmed, deaths and recovered till the latest date available.

res = api.get_stats()
Method 2: Get records for all the countries:
res = api.get_all_records_by_country()
Method 3: Get records for all the state/Province:
res = api.get_all_records_by_provinces()
Method 4: Filter by Country:
To find all the countries availabe, plese use show_all_available_countries api.

res = api.filter_by_country("ireland")
Method 5: Filter by Province/State:
To find all the countries availabe, plese use show_all_available_regions api.

res = api.filter_by_province("British Columbia")
Method 6: Show all available Countries:
res = api.show_available_countries()
Method 7: Show all valiable Province/State:
res = api.show_available_regions()
Method 8: Get history data for a given Country:
res = api.get_history_by_country("ireland")
Shows all the country metrics confirmed, recovered and deaths for the dates till the latest date.

Method 9: Get history data for a given State/Province:
res = api.get_history_by_province("British Columbia")
Shows all the state/province metrics confirmed, recovered and deaths for the dates till the latest date.

Data Sources:
All used data sources CSSEGISandData-covi19.

Support and Maintenance:
Please raise an issues with issues of this git repo. This is not actively supported, however anyone with the interest can solve the raised issues.

Copying and License
Terms and conditions of the data provider:
CSSEGISandData-covi19
