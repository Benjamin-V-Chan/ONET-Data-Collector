import json
import pandas as pd

def condense_job_details(input_json_path, output_csv_path):
    with open(input_json_path, 'r') as f:
        job_details = json.load(f)

    condensed_data = []

    for job in job_details:
        occupation = job['occupation']
        tasks = job.get('tasks', {}).get('task', [])
        technology_skills = job.get('technology_skills', {}).get('category', [])
        tools_used = job.get('tools_used', {}).get('category', [])
        knowledge = job.get('knowledge', {}).get('element', [])
        skills = job.get('skills', {}).get('element', [])
        abilities = job.get('abilities', {}).get('element', [])
        work_activities = job.get('work_activities', {}).get('element', [])
        detailed_work_activities = job.get('detailed_work_activities', {}).get('activity', [])
        work_context = job.get('work_context', {}).get('element', [])
        job_zone = job.get('job_zone', {})
        education = job.get('education', {}).get('level_required', {}).get('category', [])
        interests = job.get('interests', {}).get('element', [])
        work_styles = job.get('work_styles', {}).get('element', [])
        work_values = job.get('work_values', {}).get('element', [])
        related_occupations = job.get('related_occupations', {}).get('occupation', [])
        additional_information = job.get('additional_information', {}).get('source', [])

        job_data = {
            'occupation_code': occupation.get('code', ''),
            'occupation_title': occupation.get('title', ''),
            'description': occupation.get('description', ''),
            'bright_outlook': occupation.get('tags', {}).get('bright_outlook', False),
            'green': occupation.get('tags', {}).get('green', False),
            'tasks': '; '.join([task['statement'] for task in tasks]),
            'technology_skills': '; '.join([tech['title']['name'] for tech in technology_skills]),
            'tools_used': '; '.join([tool['title']['name'] for tool in tools_used]),
            'knowledge': '; '.join([k['name'] for k in knowledge]),
            'skills': '; '.join([skill['name'] for skill in skills]),
            'abilities': '; '.join([ability['name'] for ability in abilities]),
            'work_activities': '; '.join([activity['name'] for activity in work_activities]),
            'detailed_work_activities': '; '.join([dwa['name'] for dwa in detailed_work_activities]),
            'work_context': '; '.join([context['name'] for context in work_context]),
            'job_zone': job_zone.get('title', ''),
            'education': '; '.join([edu['name'] for edu in education]),
            'interests': '; '.join([interest['name'] for interest in interests]),
            'work_styles': '; '.join([style['name'] for style in work_styles]),
            'work_values': '; '.join([value['name'] for value in work_values]),
            'related_occupations': '; '.join([occ['title'] for occ in related_occupations]),
            'additional_information': '; '.join([info['name'] for info in additional_information]),
        }

        condensed_data.append(job_data)

    df = pd.DataFrame(condensed_data)
    df.to_csv(output_csv_path, index=False)