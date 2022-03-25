import csv
from api.models import DataSetModel

from django.conf import settings
path_to_upload_data_from_csv =str(settings.BASE_DIR) + '/dataset.csv'


count = 0
with open(path_to_upload_data_from_csv) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    if count == 0:
        count = count + 1
        continue
    DataSetModel.objects.create(
        date=row[0],
        channel =row[1],
        country =row[2],
        os =row[3],
        impressions =row[4],
        clicks =row[5],
        installs =row[6],
        spend =row[7],
        revenue=row[8]
    )
