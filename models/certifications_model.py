from pydantic import BaseModel, Field
from datetime import datetime

class CertificationModel(BaseModel):
    name        : str
    platform    : str
    date        : str
    id          : str
    category    : str
    imageUrl    : str
    createdAt   : datetime = Field(default_factory=datetime.utcnow)
    updatedAt   : datetime = Field(default_factory=datetime.utcnow)

    def is_valid(self):
        if self.name is None:
            raise ValueError("No name is provided")
        if self.platform is None:
            raise ValueError("No platform is provided")
        if self.date is None:
            raise ValueError("No date is provided")
        if self.id is None:
            raise ValueError("No id is provided")
        if self.imageUrl is None:
            raise ValueError("No image url is provided")
        return True