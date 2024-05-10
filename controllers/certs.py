# https://firebase.google.com/docs/admin/setup?hl=es#python
# https://firebase.google.com/docs/database/admin/start?hl=es#python
import os
import firebase_admin

from dotenv import load_dotenv

from firebase_admin import credentials
from firebase_admin import db

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from models.certifications_model import CertificationModel

load_dotenv()

workerId        = os.getenv("ID_WORKER")
credentialsPath = os.getenv("CREDENTIALS_PATH")
dbUrl           = os.getenv("FIREBASE_DB_URL")

# Fetch the service account key JSON file contents
creds   = credentials.Certificate( credentialsPath )

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(creds, {
    'databaseURL': dbUrl,
    'databaseAuthVariableOverride': {
        'uid': workerId
    }
})
# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/certs')

router  = APIRouter()

@router.get("/certs")
def getCertifications():
    certsInFirebase = ref.get()
    return JSONResponse(certsInFirebase)

@router.get("/cert/{id}")
def getCertification(id):
    certificationFound = ref.order_by_child("id").equal_to(id).get()
    return JSONResponse(certificationFound)


@router.post("/certs")
def createCertifications(certifications: CertificationModel):
    if not certifications.is_valid():
        raise HTTPException(status_code=400, detail="The certification data is not valid")

    result = ref.push().set({
            'name'      : certifications.name,
            'platform'  : certifications.platform,
            'date'      : certifications.date,
            'id'        : certifications.id,
            'category'  : certifications.category,
            'imageUrl'  : certifications.imageUrl
    })
    return JSONResponse(f"Certification: {certifications.name} created")