#index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo App</title>
</head>

<body>
    <h1>ToDo App</h1>
    <form method="post" action="/add/task">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="description">Description:</label><br>
        <textarea id="description" name="description"></textarea><br>
        <input type="submit" value="Add Task">
    </form>
    <h2>Tasks:</h2>
    <ul>
        %for task in tasks %
        <li><strong>{{task.title}}</strong> - {{task.description }}</li>
        % endfor %
    </ul>
</body>

</html>


#main.py
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Task(BaseModel):
    title: str
    description: str


tasks = []


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


@app.get("/add_task/")
async def add_task(task: Task):
    tasks.append(task)
    return {"message": "task added successfully"}


@app.get("/get_tasks/")
async def get_task():
    return tasks

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="127.0.0.1", port=8001)
