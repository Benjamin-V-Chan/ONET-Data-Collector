import json
import csv
from .OnetWebService import OnetWebService
from .utils import check_for_error

def fetch_job_details(username, password, input_csv_path, output_json_path):
    onet_ws = OnetWebService(username, password)
    details = []

    with open(input_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_code = row['Job Code']
            print(f"Fetching details for: {job_code}")
            job_details = onet_ws.call(f'online/occupations/{job_code}/details')
            check_for_error(job_details)
            details.append(job_details)

    with open(output_json_path, 'w') as jsonfile:
        json.dump(details, jsonfile, indent=2)