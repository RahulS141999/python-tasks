#.env
GITLAB_API_KEY =  glpat-Xnoq6CBYDbNt1aQahrCe
GITLAB_URL = https://gitlab.com
PROJECT_ID = 47012248

branches.py

import gitlab
import os
from dotenv import load_dotenv

load_dotenv()  # load_dotenv()

# load all the variables in the .env file

gitlab_url = os.getenv('GITLAB_URL')
api_key = os.getenv('GITLAB_API_KEY')
project_id = int(os.getenv('PROJECT_ID'))  # type: ignore

gl = gitlab.Gitlab(gitlab_url, private_token=api_key)
'''def list_branch(project_id):
    project = gl.projects.get(project_id)
    branches = project.branches.list()

    for branch in branches:
        print(branch.name)


def delete_branch(project_id, branch_name):
    project = gl.projects.get(project_id)
    branch = project.branches.get(branch_name)
    branch.delete()
    print(f"deleted branch: {branch_name}")


project_id = '47012248'
print("list branches: ")
list_branch(project_id)

branch_to_delete = 'branch1'
delete_branch(project_id, branch_to_delete)'''


def list_project_branches():
    try:
        project = gl.projects.get(project_id)
        branches = project.branches.list()

        for branch in branches:
            print(branch.name)
    except Exception as e:
        print(f" error: failed to get project. {e}")


def delete_project_branch(branch_name):
    try:
        project = gl.projects.get(project_id)

        project.branches.delete(branch_name)
        print(f"deleted branch: {branch_name}")
    except Exception as e:
        print(f"Error failed to delete branch. {e}")


list_project_branches()
branch_name = input("Enter the branch name to delete: ")

try:
    delete_project_branch(branch_name)
except Exception as e:
    print(f"failed to delete branch. {e}")
