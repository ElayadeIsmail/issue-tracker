from sqlmodel import Session,select
from app.models.issues import Issue
from app.models.projects import Project
from app.models.projects_to_users import ProjectUserLink

from app.models.users import User
from ..database.database import engine
from app.utils.api import not_found_error

async def get_project_issues(project_id:int,current_user:User):
    with Session(engine) as session:
        project_statement = select(Project).where(Project.id == project_id,ProjectUserLink.user_id == current_user.id)
        project = session.exec(project_statement).first()
        if project is None:
            raise not_found_error()
        issues = session.exec(select(Issue,User).join(User)).all()
        result = []
        for issue, assignee in issues:
            result.append({"issue":issue,"assignee":assignee})
        return result
    