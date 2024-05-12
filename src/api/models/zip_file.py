from fastapi import UploadFile
from pydantic import BaseModel

class ZipUpload(BaseModel):
    """"""

    file: UploadFile