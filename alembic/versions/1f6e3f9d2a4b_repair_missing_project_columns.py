"""Repair missing project columns

Revision ID: 1f6e3f9d2a4b
Revises: 8bf7e1029b19
Create Date: 2026-05-06 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "1f6e3f9d2a4b"
down_revision: Union[str, None] = "8bf7e1029b19"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE projects ADD COLUMN IF NOT EXISTS project_owner_id INTEGER")
    op.execute("ALTER TABLE projects ADD COLUMN IF NOT EXISTS project_owner_name VARCHAR")
    op.execute("ALTER TABLE projects ADD COLUMN IF NOT EXISTS project_users VARCHAR")
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_projects_project_owner_id "
        "ON projects (project_owner_id)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_projects_project_owner_id")
    op.execute("ALTER TABLE projects DROP COLUMN IF EXISTS project_users")
    op.execute("ALTER TABLE projects DROP COLUMN IF EXISTS project_owner_name")
    op.execute("ALTER TABLE projects DROP COLUMN IF EXISTS project_owner_id")
