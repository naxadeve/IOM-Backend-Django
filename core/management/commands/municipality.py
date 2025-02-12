from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Province, District, Municipality

from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):
    help = 'load province data from province.xlsx file'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path)
        upper_range = len(df)

        print("Wait Data is being Loaded")

        try:
            municipality = [
                Municipality(
                    district=District.objects.get(code=(df['District_id'][row])),
                    name=df['Name'][row],
                    hlcit_code=df['HLCIT_CODE'][row],

                ) for row in range(0, upper_range)

            ]

            municipality_data = Municipality.objects.bulk_create(municipality)

            if municipality_data:
                self.stdout.write('Successfully  updated data ..')

        except Exception as e:
            print(e)

