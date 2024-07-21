# GitHub Stalker - Automated GitHub Profile Tracking

GitHub Stalker is a Python script designed to automatically generate PDF reports detailing the projects of a GitHub user. It tracks profile activities and identifies newly added projects, helping you stay updated with the developments in any specified GitHub profile.

## Features
- **Dynamic Project Extraction**: Leverages the GitHub API to fetch project details from a specified user profile.
- **New Project Detection**: Compares current projects with previously fetched ones to detect and report new additions.
- **PDF Report Generation**: Creates a comprehensive PDF report listing all projects, highlighting new ones if detected.
- **Automated Tracking**: Ideal for regular execution, this tool can serve as a monitoring system for project updates or additions.
## Usage
**To use this script**:

1- Ensure you have Python and the necessary libraries (requests, fpdf) installed.
2- Run the script via the command line with the target GitHub profile URL as an argument:

```bash
python github_stalker.py github_url
```
Replace github_url with the actual GitHub profile URL you wish to track.

## Installation

1-Clone this repository:
```bash
git clone https://github.com/yourusername/github-stalker.git
```
2-Install the required dependencies:
```bash
pip install requests fpdf
```
**Enjoy tracking GitHub profiles with ease and efficiency using GitHub Stalker!**
