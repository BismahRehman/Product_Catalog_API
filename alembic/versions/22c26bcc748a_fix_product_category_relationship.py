"""fix product-category relationship

Revision ID: 22c26bcc748a
Revises: c631ba237d92
Create Date: 2026-03-04 17:26:03.564372
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '22c26bcc748a'
down_revision = 'c631ba237d92'
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Upgrade schema."""
    # Add foreign key from Product.category_id → Category.id
    with op.batch_alter_table("product") as batch_op:
        batch_op.create_foreign_key(
            "fk_product_category",  # constraint name
            "category",             # target table
            ["category_id"],        # source columns
            ["id"]                  # target columns
        )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop foreign key
    with op.batch_alter_table("product") as batch_op:
        batch_op.drop_constraint("fk_product_category", type_="foreignkey")