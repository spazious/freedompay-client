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

class DiscountService(BaseModel):
    """
    DiscountService
    """
    scenario_code: Optional[StrictStr] = Field(None, alias="scenarioCode")
    options: Optional[StrictStr] = None
    run: Optional[StrictStr] = None
    __properties = ["scenarioCode", "options", "run"]

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
    def from_json(cls, json_str: str) -> DiscountService:
        """Create an instance of DiscountService from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscountService:
        """Create an instance of DiscountService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscountService.parse_obj(obj)

        _obj = DiscountService.parse_obj({
            "scenario_code": obj.get("scenarioCode"),
            "options": obj.get("options"),
            "run": obj.get("run")
        })
        return _obj


