"""
Takes a database file with a column labelled 'address' or 'Address' and returns a new database file
with two new columns, 'Latitude' and 'Longitude'.
"""

import pandas as pd
from geopy.geocoders import ArcGIS


class GeocoderAdd(object):

    def __init__(self, file):
        self.file = file            # Unopened CSV File given
        self.database = None        # Initial database
        self.geocoded = None        # Eventual return database

    def _check_database(self):      # Checks if db has a column labelled 'address' or 'Address'
        try:
            self.database = pd.read_csv(self.file)
        except Exception:           # Make sure file is a .csv file
            return False
        else:
            if "Address" in self.database.columns or "address" in self.database.columns \
             or "ADDRESS" in self.database.columns:
                return True
            else:
                return False            # DB does not have the correct field, return error

    def transform_database(self):   # Runs geocoding and returns geocoded database
        if self._check_database():
            df = self.database
            arc = ArcGIS()

            try:
                df["Coordinates"] = df["Address"].apply(arc.geocode)
            except KeyError:
                return False
            else:
                df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
                df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)

                self.geocoded = df


