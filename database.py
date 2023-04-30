from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://5jvxqwm3a8dxt2kpnq2w:pscale_pw_mFAJD6jf4eVGyGnPCrUAadhUrKukDlOiPrRXV6B6CjQ@us-west.connect.psdb.cloud/wiffleball?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_player_info():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Players"))
    player_info = []
    for row in result.all():
      player_info.append(dict(row._mapping))
    return player_info

