#.env
GITLAB_API_KEY = glpat-Xnoq6CBYDbNt1aQahrCe
GITLAB_BASE_URL = https://gitlab.com/
#GITLAB_PRIVATE_TOKEN = glpat-Xnoq6CBYDbNt1aQahrCe


#main.py
import os
import gitlab
import uvicorn
import logging
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

gitlab_base_url = os.getenv("GITLAB_BASE_URL")
gitlab_api_key = os.getenv("GITLAB_API_KEY")

gl = gitlab.Gitlab(url=gitlab_base_url, private_token=gitlab_api_key)
gl.auth()

app = FastAPI()

logging.basicConfig(filename='app.log', level=logging.NOTSET,
                    format='%(asctime)s -  %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#defining pydantic model
class  ProjectCreateRequest(BaseModel):
    name: str

class  FileCreateRequest(BaseModel):
    project_id: int
    file_name: str

class  FileUpdateRequest(BaseModel):
    project_id: int
    file_name: str
    content: str

# project creation

@app.post("/create_project/")
async def create_gitlab_projects(request: ProjectCreateRequest):
    try:
        project = gl.projects.create({"name": request.name})
        logger.info(f"new gitlab project '{request.name}' created succesfully")
        return {"message": f"project {request.name} created successfully"}
    except Exception as e:
        logger.error(f" error creating gitlab project: {str(e)}")
        return {"error": f"Error creating project {str(e)}"}

# file creation

@app.post("/create_file/")
async def create_gitlab_file(request: FileCreateRequest):
    try:
        project = gl.projects.get(request.project_id)
        content = "Joey doesn't share food!"
        branch = "main"

        logger.info(f"new file {request.file_name} is created in {request.project_id}")
        project.files.create({"file_path": request.file_name, "branch": branch, "content": content,
                             "commit_message": "files created and added successfully."})
        return {"message": f"file {request.file_name} created and committed successfully"}
        
    except Exception as e:
        logger.error(f" error creating gitlab project: {str(e)}")
        return {"error": f"Error creating file: {str(e)}"}
         


# update file by putting/modfying new data
@app.put("/update_file/")
async def update_gitlab_file(request: FileUpdateRequest):
    try:
        project = gl.projects.get(request.project_id)
        content = "Joey doesn't share food! but sometimes he does"
        branch = "main"

        logger.info(f"Attempting to update content of file '{request.file_name}' in project '{request.project_id}'")
        file = project.files.get(file_path=request.file_name, ref=branch)
        file.content = request.content
        file.save(branch=branch, commit_message="updated file content")
        return {f"message: file content updated and committed successfully"}
    except Exception as e:
        logger.error(f"error is there while creating file")
        return {"error": f"Error while updating file {str(e)}"}
uvicorn.run(app=app, host="0.0.0.0", port=8001)  # type: ignore




'''import os
import gitlab
import uvicorn
import logging
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

gitlab_base_url = os.getenv("GITLAB_BASE_URL")
gitlab_api_key = os.getenv("GITLAB_API_KEY")

gl = gitlab.Gitlab(url=gitlab_base_url, private_token=gitlab_api_key)
gl.auth()

app = FastAPI()

logging.basicConfig(filename='app.log', level=logging.NOTSET,
                    format='%(asctime)s -  %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# project creation

@app.post("/create_project/{project_name}")
async def create_gitlab_projects(project_name: str):
    try:
        project = gl.projects.create({"name": project_name})
        logger.info(f"new gitlab project '{project_name}' created succesfully")
        return {"message": f"project {project_name} created successfully"}
    except Exception as e:
        logger.error(f" error creating gitlab project: {str(e)}")
        return {"error": f"Error creating project {str(e)}"}

# file creation

@app.post("/create_project/{project_id}/{file_name}")
async def create_gitlab_file(project_id: int, file_name: str):
    try:
        project = gl.projects.get(project_id)
        content = "Joey doesn't share food!"
        branch = "main"

        logger.info(f"new file {file_name} is created in {project_id}")
        project.files.create({"file_path": file_name, "branch": branch, "content": content,
                             "commit_message": "files created and added successfully."})
        return {"message": f"file {file_name} created and committed successfully"}
        
    except Exception as e:
        logger.error(f" error creating gitlab project: {str(e)}")
        return {"error": f"Error creating file: {str(e)}"}
         


# update file by putting/modfying new data
@app.put("/update_file/{project_id}/{file_name}")
async def update_gitlab_file(project_id: int, file_name: str):
    try:
        project = gl.projects.get(project_id)
        content = "Joey doesn't share food! but sometimes he does"
        branch = "main"

        logger.info(f"Attempting to update content of file '{file_name}' in project '{project_id}'")
        file = project.files.get(file_path=file_name, ref=branch)
        file.content = content
        file.save(branch=branch, commit_message="updated file content")
        return {f"message: file content updated and committed successfully"}
    except Exception as e:
        logger.error(f"error is there while creating file")
        return {"error": f"Error while updating file {str(e)}"}
uvicorn.run(app=app, host="0.0.0.0", port=8001)  # type: ignore'''
