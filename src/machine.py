from pydantic import BaseModel, Field, field_validator
import subprocess
import logging


class Machine(BaseModel):
    name: str = Field(..., min_length=1, max_length=8)
    os: str
    cpu: int = Field(..., gt=0)
    ram: int = Field(..., gt=0)


    @field_validator("name")
    def validate_name(cls, v):
         if len(v) > 8:
              raise ValueError ("name must be 8 characters")
         if len(v) < 1:
              raise ValueError("name must be not empty")
         return v


    @field_validator("os")
    def validate_os(cls, v):
        allowed = ["ubuntu", "centos", "windows"]
        if v.lower() not in allowed:
            raise ValueError("OS must be ubuntu, centos, or windows")
        return v.lower()


    @field_validator("cpu")
    def validate_cpu(cls, v):
        if v <= 0 and v > 64:
            raise ValueError("cpu must be a positive number")
        return v


    @field_validator("ram")
    def validate_ram(cls, v):
        if v <= 0 and v > 32:
            raise ValueError("ram must be a positive number")
        return v





