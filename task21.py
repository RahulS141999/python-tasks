#.env
GITLAB_API_KEY = glpat-Xnoq6CBYDbNt1aQahrCe
GITLAB_BASE_URL = https://gitlab.com/


#main.py
# Use Fastapi with uvicorn to create separate  REST API  to access group project, repo & files using gitlab module
import uvicorn
import os
import logging
import gitlab
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

load_dotenv()
gitlab_base_url = os.getenv("GITLAB_BASE_URL")
gitlab_api_key = os.getenv("GITLAB_API_KEY")
gl = gitlab.Gitlab(url=gitlab_base_url, private_token=gitlab_api_key)
gl.auth()
logging.basicConfig(filename='task21/access_project.log', level=logging.NOTSET,
                    format='%(asctime)s -  %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/group/{group_id}/projects")
def get_group_projects(group_id: int):
    try:
        group = gl.groups.get(group_id)
        projects = group.projects.list(all=True)
        logger.info(
            f"accessing projects/repo for group {group_id}: {projects}")
        return {"projects": [project.name for project in projects]}
    except Exception as e:
        logger.error(f" error accessing projects from gitlab: {str(e)}")
        return JSONResponse(status_code=500, content={"message ": "internal server error"})


@app.get("/group/{group_id}/project/{project_id}")
def get_project_details(group_id: int, project_id: int):
    try:
        project = gl.projects.get(project_id)
        project_info = {
            "name": project.name,
            "description": project.description,
            "visibility" : project.visbility,
            "last_activity" : project.last_activity_at,
            "web_url" : project.web_url,
        }
        logger.info(f"retrieved project details from gitlab for {project_id}: {project_info}")
        return project_info

    except Exception as e:
        logger.error(f"error retrieving project details")
        return JSONResponse(status_code=404, content={"message ": "project not found"})

# import uvicorn main:app --host 0.0.0.0 --port 8002


uvicorn.run(app=app, host="0.0.0.0", port=8003)


'''@app.get("/group/{group_id}/project/{project_id}/repositories/")
def get_project_repositories(group_id: int, project_id: int):
    try:
        group = gl.groups.get(group_id)
        projects = group.projects.list(all=True)
        projects = gl.projects.get(project_id)
     #   files = projects.files.get(file_path= 'file2.txt', ref= 'main') 
     #   print(files)
        repositories = projects.repositories.list(all=True)
#     print(repositories)
        logger.info(f"accessing projects for {project_id}: {repositories}")
        return {"repositories": [repo.name for repo in repositories]}
    except Exception as e:
        logger.error(f" error accessing repos from gitlab: {str(e)}")
        return JSONResponse(status_code=500, content={"message": "internal server error"})'''
