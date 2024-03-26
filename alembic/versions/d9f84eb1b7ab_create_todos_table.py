"""create todos table

Revision ID: d9f84eb1b7ab
Revises: 
Create Date: 2024-03-25 13:20:12.160587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9f84eb1b7ab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.execute("""
     create table todos(
         id bigserial primary key,
         name text,
         completed boolean not null default false
     )
     """)

def downgrade():
     op.execute("drop table todos;")
