from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, ConfigDict, Field, field_validator

class UUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    phone_number: str = Field(..., description='Номер телефона должен начинаться с +')


    @field_validator('phone_number')
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{1,15}$', value):
            raise ValueError('Номер телефона должен начинатьсяс + и содержать от 1 до 15 цифер')
        return value