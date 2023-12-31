from sqlmodel import Session,select
from app.models.issues import Issue
from app.models.projects import Project
from app.models.projects_to_users import ProjectUserLink

from app.models.users import User
from app.schemas.issues import IssueIn
from ..database.database import engine
from app.utils.api import bad_request_error, not_found_error, unauthorized_request_error

async def user_has_right_to_project(project_id:int,user_id:int):
    with Session(engine) as session:
        project_statement = select(Project).join(ProjectUserLink).where(Project.id == project_id,ProjectUserLink.user_id == user_id)
        project = session.exec(project_statement).first()
        return project
    

async def get_project_issues(project_id:int,current_user:User):
    project = await user_has_right_to_project(project_id,current_user.id)
    if not project:
        raise not_found_error()
    with Session(engine) as session:
        statement = select(Issue,User).outerjoin(User,Issue.assignee_id == User.id).where(Issue.project_id == project_id).order_by(Issue.updated_at.desc())
        result = session.exec(statement)
        issues = []
        for issue,user in result:
            issues.append({**issue.model_dump(),"assignee":user})
        return issues


async def create_issue(project_id:int,issue_args:IssueIn,current_user:User):
    project = await user_has_right_to_project(project_id,current_user.id)
    if not project:
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
    
async def update_issue(project_id:int,issue_id:int,issue_args:IssueIn,current_user:User):
    project = await user_has_right_to_project(project_id,current_user.id)
    if not project:
        raise not_found_error() 
    with Session(engine) as session:
        issue = session.exec(select(Issue).where(Issue.id == issue_id)).first() 
        if not issue or issue.project_id != project_id:
            raise not_found_error()
        if issue_args.assignee_id and issue.assignee_id != issue_args.assignee_id:
            project = await user_has_right_to_project(project_id,issue_args.assignee_id)
            if not project:
                raise bad_request_error("assignee doesn't have access to this project")
            issue.name = issue_args.name
            issue.description = issue_args.description
            issue.due_date = issue_args.due_date
            issue.status = issue_args.status
            issue.priority = issue_args.priority
            issue.assignee_id = issue_args.assignee_id
            session.add(issue)
            session.refresh(issue)
            return issue
    
async def delete_issue(project_id:int,issue_id:int,current_user:User):
    project = await user_has_right_to_project(project_id,current_user.id)
    if not project:
        raise not_found_error() 
    if project.admin_id != current_user.id:
        raise unauthorized_request_error("Only Project Admin Can Delete Issues")
    with Session(engine) as session:
        issue = session.exec(select(Issue).where(Issue.id == issue_id)).first() 
        if not issue or issue.project_id != project_id:
            raise not_found_error()
        session.delete(issue)
        session.commit()
        return