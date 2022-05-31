from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '515de44af042'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("messages")
    op.add_column("messages", sa.Column("msg_id", sa.Integer(), primary_key=True, nullable=False))
    op.add_column("messages", sa.Column("message", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("messages")
    pass
