from marshmallow import Schema, fields, validate, ValidationError
import re

def validate_name(data):
    name_re = re.fullmatch(re.compile(r"^\w+$"),data)
    if not name_re:
        raise ValidationError("Visisble charecters only", status_code=400)
    elif len(data) <= 2:
        raise ValidationError("name too short")
    

def validate_password(password):
    if len(password) < 6:
        raise ValidationError("password must be more than 6 characters")
    elif not re.search('[a-z]+',password):
        raise ValidatioError("Have atleast one small letter")
    elif not re.search ('[A-Z]+',password):
        raise alidationError("Have atleast one capital letter")
    elif not re.search('\W+',password):
        raise ValidationError("Have atleast one special character")
    else:
        password_re =re.fullmatch(re.compile(r"^\S+$"),password)
        if not password_re:
            raise ValidationError('no spaces allowed in password')

def validate_phone(phone_number):
    if len(phone_number) < 8:
        raise ValidationError("phonenumber must be more than 8 characters")
    phone_re=re.fullmatch(re.compile('^\D$'),phone_number)
    if phone_re:
        raise ValidationError("enter numbers")


# Class user schema
class UserSchema(Schema):
    name = fields.Str(validate=validate_name, required=True)
    username = fields.Str(validate=validate_name, required=True)
    password = fields.Str(validate=validate_password, required=True) 
    confirmpassword = fields.Str(validate=validate_password, required=True)
Userschema = UserSchema()

class DriverSchema(Schema):
    name = fields.Str(validate=validate_name, required=True)
    username = fields.Str(validate=validate_name, required=True)
    car = fields.Str(validate=validate_name, required=True)
    phone_number = fields.Str(validate=validate_phone, required=True)
    password = fields.Str(validate=validate_password, required=True) 
    confirmpassword = fields.Str(validate=validate_password, required=True)
driverschema = DriverSchema(Schema)


class RideSchema(Schema):
    location = fields.Str(validate=validate_name, required=True)
    destination = fields.Str(validate=validate_name, required=True)

rideschema = RideSchema()

