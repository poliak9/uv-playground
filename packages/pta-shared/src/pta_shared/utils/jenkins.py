
from pydantic import BaseModel

class JenkinsBuild(BaseModel):
    id: str

def get_build(id:str) -> JenkinsBuild:
    return JenkinsBuild(id=id)

