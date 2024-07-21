import json
import csv

def full_details_to_csv(json_path, csv_path):
    with open(json_path, 'r') as infile:
        job_details = json.load(infile)

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Job Code', 'Job Title', 'Description', 'Tasks', 'Skills', 'Tools', 'Technology']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for job in job_details:
            writer.writerow({
                'Job Code': job.get('code'),
                'Job Title': job.get('title'),
                'Description': job.get('description'),
                'Tasks': '; '.join(task.get('task') for task in job.get('tasks', [])),
                'Skills': '; '.join(skill.get('description') for skill in job.get('skills', [])),
                'Tools': '; '.join(tool.get('description') for tool in job.get('tools', [])),
                'Technology': '; '.join(tech.get('description') for tech in job.get('technology', []))
            })

    print(f"Job details converted to CSV and saved to {csv_path}")