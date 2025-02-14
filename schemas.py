from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    full_name: str
    email: str
    password_hash: str
    created_at: datetime.time
    updated_at: datetime.time
    role: str


class ReadUsers(BaseModel):
    id: int
    full_name: str
    email: str
    password_hash: str
    created_at: datetime.time
    updated_at: datetime.time
    role: str
    class Config:
        from_attributes = True


class Leads(BaseModel):
    id: int
    user_id: int
    source_type: str
    created_at: datetime.time
    updated_at: datetime.time
    full_name: str
    email: str
    phone_number: int
    address: str
    message: str


class ReadLeads(BaseModel):
    id: int
    user_id: int
    source_type: str
    created_at: datetime.time
    updated_at: datetime.time
    full_name: str
    email: str
    phone_number: int
    address: str
    message: str
    class Config:
        from_attributes = True


class Attachments(BaseModel):
    id: int
    lead_id: int
    file_url: str
    file_name: str
    created_at: datetime.time


class ReadAttachments(BaseModel):
    id: int
    lead_id: int
    file_url: str
    file_name: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class Addresses(BaseModel):
    id: int
    lead_id: int
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    created_at: datetime.time


class ReadAddresses(BaseModel):
    id: int
    lead_id: int
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class Profiles(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone_number: int
    address: str
    created_at: datetime.time
    updated_at: datetime.time


class ReadProfiles(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone_number: int
    address: str
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    full_name: str
    email: str
    password_hash: str
    created_at: str
    updated_at: str
    role: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    full_name: str
    email: str
    password_hash: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True



class PostProfiles(BaseModel):
    id: int
    user_id: int
    full_name: str
    phone_number: int
    address: str

    class Config:
        from_attributes = True



class PostLeads(BaseModel):
    id: int
    user_id: int
    source_type: str
    full_name: str
    phone_number: int
    address: str
    email: str
    message: str

    class Config:
        from_attributes = True



class PostAttachments(BaseModel):
    id: int
    lead_id: int
    file_url: str
    file_name: str

    class Config:
        from_attributes = True



class PostAddresses(BaseModel):
    id: int
    lead_id: int
    street: str
    city: str
    state: str
    postal_code: str
    country: str

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str
    password_hash: str

    class Config:
        from_attributes = True

