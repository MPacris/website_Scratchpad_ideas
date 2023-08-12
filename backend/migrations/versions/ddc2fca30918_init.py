"""Init

Revision ID: ddc2fca30918
Revises: 
Create Date: 2023-02-07 10:28:00.117464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddc2fca30918'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    songs = op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('artist', sa.String(length=255), nullable=False),
    sa.Column('album', sa.String(length=255), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('genre', sa.String(length=255), nullable=False),
    sa.Column('running_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # Seeding data
    op.bulk_insert(songs, 
    [
        {
            "title": "Napoleon Solo",
            "artist": "At The Drive-In",
            "album": "In / Casino / Out",
            "release_date": "1998-08-18",
            "genre": "Post-Hardcore",
            "running_time": 288
        },
        {
            "title": "Bonnie Hill",
            "artist": "Jungle",
            "album": "Loving in Stereo",
            "release_date": "2021-08-13",
            "genre": "Neo Soul/Funk",
            "running_time": 191
        },
        {
            "title": "Sweetness",
            "artist": "Jimmy Eat World",
            "album": "Bleed American",
            "release_date": "2001-04-24",
            "genre": "Alternative/Indie",
            "running_time": 220
        }
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    # ### end Alembic commands ###
