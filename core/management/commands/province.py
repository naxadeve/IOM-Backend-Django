from django.core.management.base import BaseCommand
import pandas as pd
from core.models import Province, District
from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):
    help = 'load province data from province.xlsx file'

    # def add_arguments(self, parser):
    #     parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        # path = kwargs['path']
        # df = pd.read_csv(path)
        # upper_range = len(df)

        province_dummy = Province.objects.all()
        try:
            for i in province_dummy:
                province_update = Province.objects.filter(id=i.province_id).update(boundary=i.geom_char)

            if province_update:
                self.stdout.write('Successfully  updated data ..')

        except Exception as e:
            print(e)
