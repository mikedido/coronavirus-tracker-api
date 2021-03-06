import csv
import requests as r
import json
from datetime import datetime, timedelta
import pandas
from io import StringIO

class Request_CSV:
    """
    Request the csv data    
    """
    def __init__(self):
        self.date = (datetime.now() - timedelta(days=1)).strftime('%m-%d-%Y')

    def execute(self, url):
        data = r.get(url)
        if 200 == data.status_code :
            return csv.reader(data.text.splitlines(), delimiter=';')
            #return pandas.read_csv(url, delimiter=";", encoding='utf-8')


class Request_data_hospital(Request_CSV):

    URL ="https://static.data.gouv.fr/resources/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/20210201-192042/covid-hospit-incid-reg-2021-02-01-19h20.csv"

    def get_daily(self):
        return super().execute(self.URL)
    
    def get_total(self):
        return super().execute(self.URL)


class Request_data(Request_CSV):
    #URL = "https://static.data.gouv.fr/resources/donnees-relatives-a-lepidemie-de-covid-19-en-france-vue-densemble/20210202-153109/synthese-fra.csv"
    URL = 'https://www.data.gouv.fr/fr/datasets/r/2cfa819d-7b5e-4a4f-8f79-bf413ebb0cbf'

    def get_data(self):
        return super().execute(self.URL)



class Request_data_vaccination(Request_CSV):
 
    #URL = "https://www.data.gouv.fr/fr/datasets/r/5cb21a85-b0b0-4a65-a249-806a040ec37"
    URL = "https://www.data.gouv.fr/fr/datasets/r/5cb21a85-b0b0-4a65-a249-806a040ec372"
    URL = "https://static.data.gouv.fr/resources/lieux-de-vaccination-contre-la-covid-19/20210222-100509/centres-vaccination.csv"

    def get_location(self):
        return super().execute(self.URL)

class Request_data_depistage(Request_data):

    URL = "https://www.data.gouv.fr/fr/datasets/r/c5178417-ac0e-4953-844c-7c7258b018a6"

    def get_data(self):
        return super().execute(self.URL)


#test main 


#for row in Request_data_vaccination().get_location():
#    print(row)

#for row in Request_data_depistage().get_data():
    #print(row)