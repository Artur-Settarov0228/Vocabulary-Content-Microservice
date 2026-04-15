"""convert_uuid_to_int

Revision ID: 1bb6973d1bf2
Revises: 
Create Date: 2026-04-15 10:54:11.465511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bb6973d1bf2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # 1. Eski PK ni o'chirish
    op.execute('ALTER TABLE vocabulary DROP CONSTRAINT IF EXISTS vocabulary_pkey CASCADE')

    # 2. Sequence yaratish (raqamlarni generatsiya qilish uchun)
    op.execute('CREATE SEQUENCE IF NOT EXISTS vocabulary_word_id_seq')

    # 3. word_id ni Integer ga o'tkazish va sequence ni bog'lash
    op.execute('ALTER TABLE vocabulary ALTER COLUMN word_id TYPE INTEGER USING nextval(\'vocabulary_word_id_seq\')')
    op.execute('ALTER TABLE vocabulary ALTER COLUMN word_id SET DEFAULT nextval(\'vocabulary_word_id_seq\')')
    
    # 4. Sequence ni ustunga biriktirish
    op.execute('ALTER SEQUENCE vocabulary_word_id_seq OWNED BY vocabulary.word_id')

    # 5. Primary Key-ni qayta qo'shish
    op.execute('ALTER TABLE vocabulary ADD PRIMARY KEY (word_id)')

def downgrade() -> None:
    # Orqaga qaytarish hozircha shart emas
    pass