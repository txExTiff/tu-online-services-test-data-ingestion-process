import requests
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import WayfindingDirectory
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:8073"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)





# Ensure tables are created
Base.metadata.create_all(bind=engine)

# Dependency: Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# JSON Feed URL
JSON_FEED_URL = "https://api.jsonbin.io/v3/b/67be26bead19ca34f811fa86"
HEADERS = {"X-Access-Key": "$2a$10$D47JHC.kzgai8FEYHsR6W.3TIfeQnT6JjFQzmvFj8YCRq6UX4gGV6"}

# Sync JSON feed to database
@app.post("/sync-wayfinding")
def sync_wayfinding_directory(db: Session = Depends(get_db)):
    response = requests.get(JSON_FEED_URL, headers=HEADERS)

    if response.status_code != 200:
        return {"error": "Failed to fetch data from source"}

    records = response.json().get("record", [])

    if not records:
        return {"error": "No records found in JSON feed"}

    for record in records:
        # Convert last_modified to datetime (ISO 8601)
        last_modified = datetime.datetime.strptime(record["last_modified"], "%Y-%m-%dT%H:%M:%SZ")

        # Check if record exists
        existing_record = db.query(WayfindingDirectory).filter(
            WayfindingDirectory.name == record["name"],
            WayfindingDirectory.office_location == record["office_location"]
        ).first()

        if existing_record:
            # Update existing record
            existing_record.telephone_number = record["telephone_number"]
            existing_record.room_number = record["room_number"]
            existing_record.department = record["department"]
            existing_record.last_modified = last_modified
        else:
            # Insert new record
            new_entry = WayfindingDirectory(
                name=record["name"],
                office_location=record["office_location"],
                telephone_number=record["telephone_number"],
                room_number=record["room_number"],
                department=record["department"],
                last_modified=last_modified
            )
            db.add(new_entry)

    db.commit()
    return {"message": f"{len(records)} records processed"}



@app.get("/wayfinding-directory")
def get_wayfinding_directory(db: Session = Depends(get_db)):
    records = db.query(WayfindingDirectory).all()
    return [
        {
            "name": record.name,
            "office_location": record.office_location,
            "telephone_number": record.telephone_number,
            "room_number": record.room_number,
            "department": record.department,
            "last_modified": record.last_modified.isoformat()
        }
        for record in records
    ]
