from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_player_info():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Players"))
    player_info = []
    for row in result.all():
      player_info.append(dict(row._mapping))
    return player_info

