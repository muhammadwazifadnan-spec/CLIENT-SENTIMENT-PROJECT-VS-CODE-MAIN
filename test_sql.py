import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

driver = os.getenv("SQLSERVER_DRIVER")
server = os.getenv("SQLSERVER_SERVER")
database = os.getenv("SQLSERVER_DATABASE")
username = os.getenv("SQLSERVER_USERNAME")
password = os.getenv("SQLSERVER_PASSWORD")
trust_cert = os.getenv("SQLSERVER_TRUST_CERTIFICATE", "yes")

conn_str = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    f"TrustServerCertificate={trust_cert};"
)

print("SERVER =", server)
print("DATABASE =", database)
print("USERNAME =", username)
print("DRIVER =", driver)

print("Trying to connect...")
conn = pyodbc.connect(conn_str)
print("Connected successfully!")
conn.close()