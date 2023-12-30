from sqlmodel import Session
from app.database.database import engine
from app.models.projects import Project
from app.models.users import User
from app.schemas.projects import CreateProject


async def create_project(project_args:CreateProject,admin:User):
    with Session(engine) as session:
        project = Project(name=project_args.name,description=project_args.description,admin_id=admin.id,collaborators=[admin])
        session.add(project)
        session.commit()
        
        session.refresh(project)
    return project