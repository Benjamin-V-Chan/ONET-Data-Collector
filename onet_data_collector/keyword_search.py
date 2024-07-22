import os
import csv
from onet_data_collector.OnetWebService import OnetWebService
from onet_data_collector.utils import check_for_error
import pandas as pd

def keyword_search(username, password, keyword):
    # Initialize O*NET Web Service
    onet_ws = OnetWebService(username, password)
    
    vinfo = onet_ws.call('about')
    check_for_error(vinfo)
    print("Connected to O*NET Web Services version " + str(vinfo['api_version']))
    print("")

    results = []

    print(f"Performing keyword search for: {keyword}")
    kwresults = onet_ws.call('online/search', ('keyword', keyword), ('end', 50))
    check_for_error(kwresults)

    if 'occupation' in kwresults and len(kwresults['occupation']) > 0:
        for occ in kwresults['occupation']:
            job_code = occ['code']
            job_title = occ['title']
            soc_code = job_code.split('-')[0]  # Extract SOC code (first 2 digits of job code)
            results.append({'Keyword': keyword, 'Job Code': job_code, 'Job Title': job_title, 'SOC Code': soc_code})

    # Convert the results to a DataFrame
    df = pd.DataFrame(results)
    return df