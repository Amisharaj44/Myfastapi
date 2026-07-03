from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  database_hostname: str
  database_password :str
  database_name:str
  database_username: str
  secret_key : str
  algorithm:str
  database_port:str
  access_token_expire_minutes:int


  class Config:
    env_file = ".env"



settings = Settings()


print("=" * 50)
print("HOSTNAME:", settings.database_hostname)
print("DATABASE:", settings.database_name)
print("USERNAME:", settings.database_username)
print("=" * 50)

settings = Settings()

print("HOSTNAME:", settings.database_hostname)
print("DATABASE:", settings.database_name)
print("USERNAME:", settings.database_username)
