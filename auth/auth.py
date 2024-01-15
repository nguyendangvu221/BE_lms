# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
# from pydantic import BaseModel
# from datetime import datetime, timedelta
# from jose import JWSError,jwt
# from passlib.context import CryptContext

# app = FastAPI()

# SECRET_KEY = "f207117bd929ddd463522627c505b2d3d26a5094946e018a92ecf700c401e14e"
# ALGORTHIM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 120

# fake_db = {
#     "tim": {
#         "username": " tim",
#         "full_name" : "Tim Ruscica",
#         "email":"tim@gmail.com",
#         "hashed_password":"",
#         "disabled":False
#     }
# }

# class Token(BaseModel):
#     access_token:str
#     token_type: str

# class TokenData(BaseModel):
#     username:str or None = None

# class User(BaseModel):
#     username: str
#     email: str = None
#     full_name: str = None
#     disable: bool = None

# class UserInDB(User):
#     hashed_password : str

# pwd_context = CryptContext(schemes=['bcrypt'], depreacted = 'auto')
# oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password,hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username:str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def authenticate_user(fake_db, username:str, password:str):
#     user = get_user(fake_db,username)
#     if not user:
#         return False
#     if not verify_password(password,user.hashed_password):
#         return False
#     return user

# def create_access_token(data:dict, expires_delta:timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes = 15)
#     to_encode.update({"exp":expire})
#     encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORTHIM)
#     return encoded_jwt
# async def get_current_user(token:str = Depends(oauth_2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail = "Could not validate credentials",
#         headers={"WWW-Authenticate":"Bearer"}
#     )
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORTHIM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username = username)
#     except JWSError:
#         raise credentials_exception
#     user = get_user(fake_db, username = token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disable:
#         raise HTTPException(status_code = 400, detail = "Inactive user")
#     return current_user

# @app.post("/token",response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_db,form_data.username,form_data.password)
#     if not user:
#         raise HTTPException(status_code = 400, detail = "Incorrect username or password")
#     access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data = {"sub":user.username}, expires_delta = access_token_expires
#     )
#     return {"access_token":access_token, "token_type":"bearer"}

# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user

# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id":1,"owner":current_user.username}]

# pwd = get_password_hash("123456")
# print(pwd)
