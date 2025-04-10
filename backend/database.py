#psql -U [user] -d [database]
#Database connection included in environment.yml and done manually in conda through export DATABASE_URL="postgresql://Dayton:931554@localhost:5432/calendarapp_db"
#can confirm with $echo $DATABASE_URL 

from sqlalchemy import create_engine
import os

# Get the database URL from the environment variable
database_url = os.getenv("DATABASE_URL")

# Create a connection to the database
engine = create_engine(database_url)

# Test the connection
try:
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Error: {e}")
