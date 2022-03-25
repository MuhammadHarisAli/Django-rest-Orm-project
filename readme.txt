# using sqlite as a default database

# if you are using postgres follow this link
https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django

# params to use in list api
[
    'group_by_fields'

    'filter_end_date_field'
    'filter_start_date'
    'filter_exact_date'
    'filter_channel'
    'filter_country'
    'filter_os'
    'filter_impressions'
    'filter_clicks'
    'filter_installs'
    'filter_spend'
    'filter_revenue'

    'order_by'
    'select_fields'
]


# to upload csv data to test use command on project level
python manage.py shell < uplaodcsvdata.py

#Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
# url 1 example
http://localhost:8000/api/dataset/search/?group_by_fields=impressions&group_by_fields=clicks&filter_end_date_field=2017-06-01&order_by=-clicks&select_fields=channel&select_fields=country


#Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
# url 2 example
http://localhost:8000/api/dataset/search/?select_fields=date&filter_os=ios&filter_start_date=2017-05-01&filter_end_date_field=2017-05-31&group_by_fields=installs&order_by=date


#Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
# url 3 example
http://localhost:8000/api/dataset/search/?select_fields=os&filter_country=US&filter_exact_date=2017-06-01&group_by_fields=revenue&order_by=-revenue


#Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
# url 4 example
http://localhost:8000/api/dataset/search/?group_by_fields=CPI&group_by_fields=spend&order_by=-CPI&select_fields=channel&filter_country=CA
