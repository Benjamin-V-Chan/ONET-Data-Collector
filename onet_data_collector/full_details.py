import os
import json
import csv

def generate_full_details_csv(input_json_path, output_csv_path):
    # Load job details from JSON file
    with open(input_json_path, 'r') as f:
        job_details = json.load(f)

    # Define the CSV columns
    columns = [
        'Job Code', 'Job Title', 'Job Description', 'Tasks', 'Technology Skills', 'Tools Used',
        'Knowledge', 'Skills', 'Abilities', 'Work Activities', 'Work Context', 'Job Zone',
        'Education', 'Interests', 'Work Styles', 'Work Values', 'Related Occupations', 'Wages', 'Employment'
    ]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

    # Write the job details to a CSV file
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        for code, details in job_details.items():
            writer.writerow({
                'Job Code': code,
                'Job Title': details.get('title', ''),
                'Job Description': details.get('description', ''),
                'Tasks': ', '.join(details.get('tasks', [])),
                'Technology Skills': ', '.join(details.get('technology_skills', [])),
                'Tools Used': ', '.join(details.get('tools_used', [])),
                'Knowledge': ', '.join(details.get('knowledge', [])),
                'Skills': ', '.join(details.get('skills', [])),
                'Abilities': ', '.join(details.get('abilities', [])),
                'Work Activities': ', '.join(details.get('work_activities', [])),
                'Work Context': ', '.join(details.get('work_context', [])),
                'Job Zone': details.get('job_zone', ''),
                'Education': details.get('education', ''),
                'Interests': ', '.join(details.get('interests', [])),
                'Work Styles': ', '.join(details.get('work_styles', [])),
                'Work Values': ', '.join(details.get('work_values', [])),
                'Related Occupations': ', '.join(details.get('related_occupations', [])),
                'Wages': details.get('wages', ''),
                'Employment': details.get('employment', '')
            })
    print(f"Full job details saved to {output_csv_path}")