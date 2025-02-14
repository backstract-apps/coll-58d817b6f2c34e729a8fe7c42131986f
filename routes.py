from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user')
async def post_user(db: Session = Depends(get_db)):
    try:
        return await service.post_user(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/profiles')
async def post_profiles(raw_data: schemas.PostProfiles, db: Session = Depends(get_db)):
    try:
        return await service.post_profiles(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/leads')
async def post_leads(raw_data: schemas.PostLeads, db: Session = Depends(get_db)):
    try:
        return await service.post_leads(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/attachments')
async def post_attachments(raw_data: schemas.PostAttachments, db: Session = Depends(get_db)):
    try:
        return await service.post_attachments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/addresses')
async def post_addresses(raw_data: schemas.PostAddresses, db: Session = Depends(get_db)):
    try:
        return await service.post_addresses(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

