# coding: utf-8

"""
    Hosted Payment Controls API Documentation v1.5

    The API for Hosted Payment Controls. To access the swagger.json file open the following link: https://hpc.uat.freedompay.com/api/swagger/docs/v1.5

    The version of the OpenAPI document: v1.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AdminService(BaseModel):
    """
    AdminService
    """
    service_type: Optional[StrictStr] = Field(None, alias="serviceType")
    term_caps: Optional[StrictStr] = Field(None, alias="termCaps")
    run: Optional[StrictStr] = None
    __properties = ["serviceType", "termCaps", "run"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AdminService:
        """Create an instance of AdminService from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdminService:
        """Create an instance of AdminService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdminService.parse_obj(obj)

        _obj = AdminService.parse_obj({
            "service_type": obj.get("serviceType"),
            "term_caps": obj.get("termCaps"),
            "run": obj.get("run")
        })
        return _obj


