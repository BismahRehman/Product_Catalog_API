# from alembic import op
# import sqlalchemy as sa
#
# def upgrade():
#     with op.batch_alter_table("category") as batch_op:
#         batch_op.alter_column(
#             "name",
#             existing_type=sa.String(),
#             nullable=False
#         )