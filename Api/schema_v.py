"""Validation functions and schemas for input fields"""
from marshmallow import Schema, fields, validate, ValidationError
import re


def validate_name(data):
    """validate name method"""
    name_re = re.fullmatch(re.compile(r"^\w+$"),data)
    if not name_re:
        raise ValidationError("Visible characters only")
    elif len(data) <= 2:
        raise ValidationError("name too short")

def validate_email(email):
    if not email or len(email) < 5:
        raise ValidationError ("Email is too short")
    email_re = re.compile(r"(^[.A-Za-z0-9_+-]+@[A-Za-z]+\.[.A-Za-z-]+$)")
    your_email = re.fullmatch(email_re, email)
    if not your_email:
        raise ValidationError("Invalid email format")

def validate_password(password):
    """validate password method"""
    if len(password) < 6:
        raise ValidationError("password must be more than 6 characters")
    elif not re.search(r'[a-z]+',password):
        raise ValidationError("Have atleast one small letter")
    elif not re.search (r'[A-Z]+',password):
        raise ValidationError("Have atleast one capital letter")
    elif not re.search(r'\W+',password):
        raise ValidationError("Have atleast one special character")
    else:
        password_re = re.fullmatch(re.compile(r"^\S+$"),password)
        if not password_re:
            raise ValidationError('no spaces allowed in password')

def validate_phone(phone_number):
    """validate phone_number method"""
    if len(phone_number) < 8:
        raise ValidationError("phonenumber must be more than 8 characters")
    phone_re = re.fullmatch(re.compile(r'^\D$'),phone_number)
    if phone_re:
        raise ValidationError("enter numbers")

class UserSchema(Schema):
    """user input schema """
    name = fields.Str(validate=validate_name, required=True)
    username = fields.Str(validate=validate_name, required=True)
    email = fields.Str(validate=validate_email, required=True)
    phone_number = fields.Str(validate=validate_phone, required=True)
    password = fields.Str(validate=validate_password, required=True)
    confirmpassword = fields.Str(validate=validate_password, required=True)
Userschema = UserSchema()

class DriverSchema(Schema):
    """driver input schema"""
    name = fields.Str(validate=validate_name, required=True)
    username = fields.Str(validate=validate_name, required=True)
    email = fields.Str(validate=validate_email, required=True)
    car = fields.Bool(required=True)
    phone_number = fields.Str(validate=validate_phone, required=True)
    password = fields.Str(validate=validate_password, required=True)
    confirmpassword = fields.Str(validate=validate_password, required=True)
driverschema = DriverSchema(Schema)

class RideSchema(Schema):
    "ride input schema"
    location = fields.Str(validate=validate_name, required=True)
    destination = fields.Str(validate=validate_name, required=True)

rideschema = RideSchema()

class RequestStatus(Schema):
    "request status schema"
    status = fields.Bool(required=True)

requeststatus = RequestStatus()
