import sqlalchemy as sa

engine = sa.create_engine("sqlite:///database.db")
connection = engine.connect()

metadata = sa.MetaData()

measure_table = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("station", sa.String),
    sa.Column("date", sa.Date),
    sa.Column("precip", sa.Float),
    sa.Column("tobs", sa.Integer)
)

stations_table = sa.Table(
    "stations",
    metadata,
    sa.Column("station_id", sa.Integer, primary_key=True),
    sa.Column("station", sa.String),
    sa.Column("latitude", sa.String),
    sa.Column("longitude", sa.String),
    sa.Column("elevation", sa.String),
    sa.Column("name", sa.String),
    sa.Column("country", sa.String),
    sa.Column("state", sa.String)
)

metadata.create_all(engine)
