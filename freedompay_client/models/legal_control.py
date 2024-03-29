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

class LegalControl(BaseModel):
    """
    LegalControl
    """
    hide_checkbox: Optional[StrictBool] = Field(None, alias="HideCheckbox")
    text_type: Optional[StrictStr] = Field(None, alias="TextType")
    __properties = ["HideCheckbox", "TextType"]

    @validator('text_type')
    def text_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'DynamicWithCheckbox', 'DynamicWithoutCheckbox', 'DynamicThirdPartyWithCheckbox', 'DynamicThirdPartyWithoutCheckbox'):
            raise ValueError("must be one of enum values ('Unknown', 'DynamicWithCheckbox', 'DynamicWithoutCheckbox', 'DynamicThirdPartyWithCheckbox', 'DynamicThirdPartyWithoutCheckbox')")
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
    def from_json(cls, json_str: str) -> LegalControl:
        """Create an instance of LegalControl from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LegalControl:
        """Create an instance of LegalControl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LegalControl.parse_obj(obj)

        _obj = LegalControl.parse_obj({
            "hide_checkbox": obj.get("HideCheckbox"),
            "text_type": obj.get("TextType")
        })
        return _obj


