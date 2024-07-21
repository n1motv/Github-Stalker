import requests
from fpdf import FPDF
import os
import pickle
import sys  

class GitHubProfileReport:
    def __init__(self, user_url):
        self.user_url = user_url
        self.username = self.user_url.split('/')[-1] 
        self.api_url = 'https://api.github.com/users/' + self.username
        self.repo_url = self.api_url + '/repos'
        self.projects_file = f"{self.username}_projects.pkl" 
        self.previous_projects = self.load_previous_projects()

    def fetch_projects(self):
        response = requests.get(self.repo_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def load_previous_projects(self):
        if os.path.exists(self.projects_file):
            with open(self.projects_file, 'rb') as file:
                return pickle.load(file)
        else:
            return {}

    def save_projects(self, projects):
        with open(self.projects_file, 'wb') as file:
            pickle.dump(projects, file)

    def generate_pdf(self, projects, file_name):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        for project in projects:
            pdf.cell(200, 10, txt=project['name'], ln=True)
        pdf.output(file_name)  

    def check_for_new_projects(self):
        current_projects = {proj['name']: proj for proj in self.fetch_projects()}
        new_projects = {name: proj for name, proj in current_projects.items() if name not in self.previous_projects}
        self.save_projects(current_projects)
        return new_projects, current_projects.values()

    def update_report(self):
        new_projects, all_projects = self.check_for_new_projects()
        file_name = f"{self.username}_report.pdf"  
        if new_projects:
            print("New projects found: ", list(new_projects.keys()))
            self.generate_pdf(all_projects, file_name)
            print(f"Updated report generated as {file_name}.")
        else:
            print("No new projects found.")
            if not os.path.exists(file_name):
                self.generate_pdf(all_projects, file_name)
                print(f"Initial report generated as {file_name}.")
            else:
                print(f"No updates needed. Current report is up-to-date as {file_name}.")

# Usage
if len(sys.argv) < 2:
    print("Usage: python script_name.py <github_url>")
else:
    github_url = sys.argv[1]  
    report = GitHubProfileReport(github_url)
    report.update_report()
