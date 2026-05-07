from fastapi import APIRouter, Depends, HTTPException, logger, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schemas import ProjectBase, ProjectCreate, ProjectResponse
from app.models.models import Project, ProjectUser
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/projects", tags=["projects"])


# Version 1 controllers

# Get all projects for a user
@router.get("/user", response_model=list[ProjectResponse])
def get_projects(user_id: int, db: Session = Depends(get_db)):
    try:
        projects = db.query(Project).join(ProjectUser, Project.id == ProjectUser.project_id).filter(ProjectUser.user_id == user_id).all()
        return projects
    except Exception as e:
        logger.error(f"Failed to get projects for user_id {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve projects")



@router.post("/add", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def add_project(project: ProjectCreate, db: Session = Depends(get_db)):
    logger.info(f"Adding project: {project.title}, user_id: {project.user_id}")
    try:
        db_project = Project(
            title=project.title,
            description=project.description,
            user_id=project.user_id,
            project_owner_name=project.project_owner_name
        )
        db.add(db_project)
        db.flush()

        db.add(ProjectUser(project_id=db_project.id, user_id=project.user_id))

        db.commit()
        db.refresh(db_project)
        return db_project

    except Exception as e:
        db.rollback()
        logger.error(f"Failed to add project: {e}")
        raise HTTPException(status_code=500, detail="Failed to create project")