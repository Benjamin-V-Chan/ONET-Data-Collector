import os
import json
import csv

def condense_job_details(json_input_path, csv_output_path):
    # Load job details from JSON file
    with open(json_input_path, 'r') as jsonfile:
        job_details = json.load(jsonfile)

    # Define the CSV columns
    columns = [
        'Job Code', 'Job Title', 'Description', 'Tasks', 'Technology Skills', 
        'Tools Used', 'Knowledge', 'Skills', 'Abilities', 'Work Activities', 
        'Work Context', 'Job Zone', 'Education', 'Interests', 'Work Styles'
    ]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)

    # Write the job details to a CSV file
    with open(csv_output_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

        for job_code, details in job_details.items():
            writer.writerow({
                'Job Code': job_code,
                'Job Title': details['occupation'].get('title', ''),
                'Description': details['occupation'].get('description', ''),
                'Tasks': ', '.join([task['statement'] for task in details.get('tasks', {}).get('task', [])]),
                'Technology Skills': ', '.join([tech['title']['name'] for tech in details.get('technology_skills', {}).get('category', [])]),
                'Tools Used': ', '.join([tool['title']['name'] for tool in details.get('tools_used', {}).get('category', [])]),
                'Knowledge': ', '.join([knowledge['name'] for knowledge in details.get('knowledge', {}).get('element', [])]),
                'Skills': ', '.join([skill['name'] for skill in details.get('skills', {}).get('element', [])]),
                'Abilities': ', '.join([ability['name'] for ability in details.get('abilities', {}).get('element', [])]),
                'Work Activities': ', '.join([activity['name'] for activity in details.get('work_activities', {}).get('element', [])]),
                'Work Context': ', '.join([context['name'] for context in details.get('work_context', {}).get('element', [])]),
                'Job Zone': details.get('job_zone', {}).get('title', ''),
                'Education': ', '.join([edu['name'] for edu in details.get('education', {}).get('level_required', {}).get('category', [])]),
                'Interests': ', '.join([interest['name'] for interest in details.get('interests', {}).get('element', [])]),
                'Work Styles': ', '.join([style['name'] for style in details.get('work_styles', {}).get('element', [])])
            })

    print(f"Condensed job details saved to {csv_output_path}")
