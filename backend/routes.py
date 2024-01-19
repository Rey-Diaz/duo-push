"""
Copyright (c) 2023 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at https://developer.cisco.com/docs/licenses.
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from fastapi import APIRouter, Request, Depends, HTTPException
from pydantic import BaseModel
from logrr import logger_manager
from duo_app import duo_authenticator

router = APIRouter()


class UserRequest(BaseModel):
    username: str
    fullname: str
    email: str
    status: str
    devices: list

@router.post("/authenticate/")
async def authenticate(user_request: UserRequest):
    try:
        # Access individual fields from the UserRequest model
        username = user_request.username
        email = user_request.email

        # Your authentication logic here, using the extracted data
        duo_authenticator.authenticate_user(email)

        # Simulate authentication result for demonstration purposes
        result = "Authentication successful for user: " + username

        # Return the result as a JSON response
        return {"output": result}
    except Exception as e:
        # Log and handle the error
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/")
def users():
    try:
        logger_manager.console.print('[orange1]Fetching users...[/orange1]')
        result = duo_authenticator.fetch_users()
        return {"output": result}
    except Exception as e:
        # Log and handle the error
        logger_manager.console.print(f"[red]Error: {e}[/red]")
        raise HTTPException(status_code=500, detail=str(e))
