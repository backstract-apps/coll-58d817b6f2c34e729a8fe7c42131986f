from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:str = raw_data.id
    full_name:str = raw_data.full_name
    email:str = raw_data.email
    password_hash:str = raw_data.password_hash
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at
    role:str = raw_data.role


    record_to_be_added = {'id': id, 'full_name': full_name, 'email': email, 'password_hash': password_hash, 'created_at': created_at, 'updated_at': updated_at, 'role': role}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    full_name:str = raw_data.full_name
    email:str = raw_data.email
    password_hash:str = raw_data.password_hash
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'full_name': full_name, 'email': email, 'password_hash': password_hash, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def post_user(db: Session):
    res = {
    }
    return res

async def post_profiles(db: Session, raw_data: schemas.PostProfiles):
    id:int = raw_data.id
    user_id:int = raw_data.user_id
    full_name:str = raw_data.full_name
    phone_number:int = raw_data.phone_number
    address:str = raw_data.address


    
    from datetime import datetime

    try:
        created_at: datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'created_at': created_at, 'updated_at': created_at, 'address': address, 'phone_number': phone_number, 'full_name': full_name, 'user_id': user_id, 'id': id}
    new_profiles = models.Profiles(**record_to_be_added)
    db.add(new_profiles)
    db.commit()
    db.refresh(new_profiles)
    profiles_record = new_profiles.to_dict()

    res = {
        'profiles_record': profiles_record,
    }
    return res

async def post_leads(db: Session, raw_data: schemas.PostLeads):
    id:int = raw_data.id
    user_id:int = raw_data.user_id
    source_type:str = raw_data.source_type
    full_name:str = raw_data.full_name
    phone_number:int = raw_data.phone_number
    address:str = raw_data.address
    email:str = raw_data.email
    message:str = raw_data.message


    
    from datetime import datetime

    try:
        created_at: datetime = datetime.now()
        updated_at: datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'user_id': user_id, 'source_type': source_type, 'created_at': created_at, 'updated_at': updated_at, 'full_name': full_name, 'email': email, 'phone_number': phone_number, 'address': address, 'message': message}
    new_leads = models.Leads(**record_to_be_added)
    db.add(new_leads)
    db.commit()
    db.refresh(new_leads)
    leads = new_leads.to_dict()

    res = {
        'leads': leads,
    }
    return res

async def post_attachments(db: Session, raw_data: schemas.PostAttachments):
    id:int = raw_data.id
    lead_id:int = raw_data.lead_id
    file_url:str = raw_data.file_url
    file_name:str = raw_data.file_name


    
    from datetime import datetime

    try:
        created_at: datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'lead_id': lead_id, 'file_url': file_url, 'file_name': file_name, 'created_at': created_at}
    new_attachments = models.Attachments(**record_to_be_added)
    db.add(new_attachments)
    db.commit()
    db.refresh(new_attachments)
    attachments = new_attachments.to_dict()

    res = {
        'attachments': attachments,
    }
    return res

async def post_addresses(db: Session, raw_data: schemas.PostAddresses):
    id:int = raw_data.id
    lead_id:int = raw_data.lead_id
    street:str = raw_data.street
    city:str = raw_data.city
    state:str = raw_data.state
    postal_code:str = raw_data.postal_code
    country:str = raw_data.country


    
    from datetime import datetime

    try:
        created_at: datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'lead_id': lead_id, 'street': street, 'city': city, 'state': state, 'postal_code': postal_code, 'country': country, 'created_at': created_at}
    new_addresses = models.Addresses(**record_to_be_added)
    db.add(new_addresses)
    db.commit()
    db.refresh(new_addresses)
    addresses = new_addresses.to_dict()

    res = {
        'addresses': addresses,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    email:str = raw_data.email
    password_hash:str = raw_data.password_hash


    record_to_be_added = {'email': email, 'password_hash': password_hash}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    login = new_users.to_dict()



    try:
        jwttoken = jwt.decode(
            password_hash,
            '75330ca8788202471d15f43fb39e6004f2df82959e54ad7fae014b70bb3d08e8',
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        jwttoken = 'Token has expired.'
    except jwt.InvalidTokenError:
        jwttoken = 'Invalid token.'

    res = {
        'login': login,
        'jwttoken': jwttoken,
    }
    return res

