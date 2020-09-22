#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("openpaymentsdata.cms.gov", None)
# username="madhu@multipliersolutions.in",
                 # password="M@dhu2606"

# Example authenticated client (needed for non-public datasets):
client = Socrata("openpaymentsdata.cms.gov",
                 "VrkfYDAK6euW3JthRHOzaFABi",
                 )

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# https://data.cityofchicago.org/resource/f7f2-ggz5.json?limit=100&limit=100&limit=100&offset=100
results = client.get("cghb-i8te", limit=200000)
print(results)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df)