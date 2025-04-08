from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, ConfigDict, Field, field_validator

class UUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str = Field(..., description='')
    password: str = Field(..., description='')