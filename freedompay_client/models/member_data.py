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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from freedompay_client.models.user_defined_field import UserDefinedField

class MemberData(BaseModel):
    """
    MemberData
    """
    enrollment_date: Optional[StrictStr] = Field(None, alias="enrollmentDate")
    is_new_member: Optional[StrictStr] = Field(None, alias="isNewMember")
    member_identification: Optional[StrictStr] = Field(None, alias="memberIdentification")
    member_identification_type: Optional[StrictStr] = Field(None, alias="memberIdentificationType")
    id: Optional[StrictStr] = None
    street1: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber")
    level: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    additional_data: Optional[StrictStr] = Field(None, alias="additionalData")
    additional_data_type: Optional[StrictStr] = Field(None, alias="additionalDataType")
    properties: Optional[conlist(UserDefinedField)] = None
    __properties = ["enrollmentDate", "isNewMember", "memberIdentification", "memberIdentificationType", "id", "street1", "street2", "city", "state", "country", "postalCode", "phoneNumber", "level", "status", "additionalData", "additionalDataType", "properties"]

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
    def from_json(cls, json_str: str) -> MemberData:
        """Create an instance of MemberData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item in self.properties:
                if _item:
                    _items.append(_item.to_dict())
            _dict['properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MemberData:
        """Create an instance of MemberData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MemberData.parse_obj(obj)

        _obj = MemberData.parse_obj({
            "enrollment_date": obj.get("enrollmentDate"),
            "is_new_member": obj.get("isNewMember"),
            "member_identification": obj.get("memberIdentification"),
            "member_identification_type": obj.get("memberIdentificationType"),
            "id": obj.get("id"),
            "street1": obj.get("street1"),
            "street2": obj.get("street2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "postal_code": obj.get("postalCode"),
            "phone_number": obj.get("phoneNumber"),
            "level": obj.get("level"),
            "status": obj.get("status"),
            "additional_data": obj.get("additionalData"),
            "additional_data_type": obj.get("additionalDataType"),
            "properties": [UserDefinedField.from_dict(_item) for _item in obj.get("properties")] if obj.get("properties") is not None else None
        })
        return _obj

