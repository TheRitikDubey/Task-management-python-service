from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schemas import ProjectBase, ProjectCreate, ProjectResponse
from app.models.models import Project, Task

router = APIRouter(prefix="/projects", tags=["projects"])


# Version 1 controllers
@router.post("/", response_model=ProjectBase, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectBase, user_id: int, db: Session = Depends(get_db)):
    db_project = Project(title=project.name, description=project.description, user_id=user_id, project_owner_name=project.project_owner_name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.post("/add", response_model=ProjectBase, status_code=status.HTTP_201_CREATED)
def add_project(project: ProjectCreate, db: Session = Depends(get_db)):
    # logger.info(f"Adding project with name: {project.name}, owner: {project.project_owner_name}, user_id: {project.user_id}, description: {project.description}")
    db_project = Project(
        name=project.name,
        description=project.description,
        user_id=project.user_id,
        project_owner_name=project.project_owner_name
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
