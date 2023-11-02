from pydantic import BaseModel



class RegisterRequest(BaseModel):
    name: str
    password:str
    email: str
    hcaptchaToken: str

class RegisterSuccessResponse(BaseModel):
    Status: str = "Success"

class RegisterErrorResponse(BaseModel):
    Status: str = "Error"
    Details: str

class LoginRequest(BaseModel):
    login: str
    password: str
    hcaptchaToken: str