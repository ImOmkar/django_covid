## trackercovid19 
![Image of Yaktocat](https://res.cloudinary.com/dwltrduan/image/upload/v1587307228/Screenshot_190_j9gnqv.png)

## COVID DATA API

## Installation:

#### From GitHub:
  * Clone this repo. 
  
#### Also available in django project site:
    pip install covid
    
    django-admin startproject 'project_name'
 
 #### move to project directory and run:
 
    python manage.py migrate
    
    python manage.py runserver
 
    python manage.py startapp 'app_name'
    
    
## Installation:
#### Also available in pypi. github link - (https://github.com/ahmednafies/covid):
    pip install covid-data-api
    

## How to use:

#### Initialising the instance/api:
```
from covid import Covid

covid = Covid()
```

#### Method 1: Get stats:
Get the latest total stats for all confirmed, deaths and recovered till the latest date available.
```
confirmed = covid.get_total_confirmed_cases()

recovered = covid.get_total_recovered()

deaths = covid.get_total_deaths()

active = covid.get_total_active_cases()
```
#### Method 2: Get records for all the countries:
```
data = covid.get_data()
```
#### Method 4: Filter by Country:
To find all the countries availabe, plese use show_all_available_countries api.
```
india_cases = covid.get_status_by_country_name("India")
```
#### Method 6: Show all available Countries:
```
countries = covid.list_countries()
```
  
