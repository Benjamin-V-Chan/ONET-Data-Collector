import json
from .OnetWebService import OnetWebService
from .utils import check_for_error

def fetch_job_details(job_codes, username, password, output_path):
    onet_ws = OnetWebService(username, password)
    vinfo = onet_ws.call('about')
    check_for_error(vinfo)
    print("Connected to O*NET Web Services version " + str(vinfo['api_version']))
    print("")

    job_details = []

    for job_code in job_codes:
        print(f"Fetching details for job code: {job_code}")
        details = onet_ws.call(f'online/occupations/{job_code}/details')
        check_for_error(details)
        job_details.append(details)

    with open(output_path, 'w') as outfile:
        json.dump(job_details, outfile, indent=4)

    print(f"Job details fetched and saved to {output_path}")