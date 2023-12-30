from sqlmodel import Session,select
from app.models.issues import Issue
from app.models.projects import Project
from app.models.projects_to_users import ProjectUserLink

from app.models.users import User
from app.schemas.issues import CreateIssue
from ..database.database import engine
from app.utils.api import bad_request_error, not_found_error

async def user_has_right_to_project(project_id:int,user_id:int):
    with Session(engine) as session:
        project_statement = select(Project).join(ProjectUserLink).where(Project.id == project_id,ProjectUserLink.user_id == user_id)
        project = session.exec(project_statement).first()
        return project != None
    

async def get_project_issues(project_id:int,current_user:User):
    has_access = await user_has_right_to_project(project_id,current_user.id)
    if not has_access:
        raise not_found_error()
    with Session(engine) as session:
        statement = select(Issue).where(Issue.project_id == project_id)
        result = session.exec(statement).all()
        return result


async def create_issue(project_id:int,issue_args:CreateIssue,current_user:User):
    has_access = await user_has_right_to_project(project_id,current_user.id)
    if not has_access:
        raise not_found_error()
    if issue_args.assignee_id:
        assignee_access = await user_has_right_to_project(project_id, issue_args.assignee_id)
        if not assignee_access:
            raise bad_request_error("Assignee doesn't have access to this project")
    with Session(engine) as session:
        issue = Issue(name=issue_args.name,description=issue_args.description,priority=issue_args.priority,status=issue_args.status,assignee_id=issue_args.assignee_id,project_id=project_id,due_date=issue_args.due_date)
        session.add(issue)
        session.commit()
        session.refresh(issue)
        # IDK why if I removed it it doesn't work
        issue.assignee = issue.assignee
        return issue