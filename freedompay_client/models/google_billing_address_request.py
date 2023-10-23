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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class GoogleBillingAddressRequest(BaseModel):
    """
    GoogleBillingAddressRequest
    """
    format: Optional[StrictStr] = Field(None, alias="Format")
    is_required: Optional[StrictBool] = Field(None, alias="IsRequired")
    is_phone_number_required: Optional[StrictBool] = Field(None, alias="IsPhoneNumberRequired")
    __properties = ["Format", "IsRequired", "IsPhoneNumberRequired"]

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Min', 'Full'):
            raise ValueError("must be one of enum values ('Unknown', 'Min', 'Full')")
        return value

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
    def from_json(cls, json_str: str) -> GoogleBillingAddressRequest:
        """Create an instance of GoogleBillingAddressRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoogleBillingAddressRequest:
        """Create an instance of GoogleBillingAddressRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GoogleBillingAddressRequest.parse_obj(obj)

        _obj = GoogleBillingAddressRequest.parse_obj({
            "format": obj.get("Format"),
            "is_required": obj.get("IsRequired"),
            "is_phone_number_required": obj.get("IsPhoneNumberRequired")
        })
        return _obj


