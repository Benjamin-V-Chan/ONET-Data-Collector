import csv
from .OnetWebService import OnetWebService
from .utils import get_user_input, check_for_error

def keyword_search(username, password, keywords, output_path):
    onet_ws = OnetWebService(username, password)

    vinfo = onet_ws.call('about')
    check_for_error(vinfo)
    print("Connected to O*NET Web Services version " + str(vinfo['api_version']))

    with open(output_path, 'w', newline='') as csvfile:
        fieldnames = ['Keyword', 'Job Code', 'Job Title', 'SOC Code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for keyword in keywords:
            print(f"Performing keyword search for: {keyword}")
            kwresults = onet_ws.call('online/search', ('keyword', keyword), ('end', 50))
            check_for_error(kwresults)

            if 'occupation' in kwresults and len(kwresults['occupation']) > 0:
                for occ in kwresults['occupation']:
                    job_code = occ['code']
                    soc_code = job_code.split('-')[0]  # Extract SOC code (first 2 digits of job code)
                    writer.writerow({'Keyword': keyword, 'Job Code': job_code, 'Job Title': occ['title'], 'SOC Code': soc_code})

    print("Keyword search completed successfully.")