from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base

class WayfindingDirectory(Base):
    __tablename__ = "wayfinding_directory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    office_location = Column(String(255), nullable=False)
    telephone_number = Column(String(20), nullable=False)
    room_number = Column(String(50), nullable=False)
    department = Column(String(255), nullable=False)
    last_modified = Column(DateTime, default=func.now(), onupdate=func.now())
