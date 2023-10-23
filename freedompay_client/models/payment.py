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
from freedompay_client.models.tender_type import TenderType

class Payment(BaseModel):
    """
    Payment
    """
    trans_type: Optional[StrictStr] = Field(None, alias="transType")
    pos_tender_type: Optional[TenderType] = Field(None, alias="posTenderType")
    brand: Optional[StrictStr] = None
    card_type: Optional[StrictStr] = Field(None, alias="cardType")
    entry_mode: Optional[StrictStr] = Field(None, alias="entryMode")
    amount: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = Field(None, alias="currencyCode")
    offline: Optional[StrictStr] = None
    request_id: Optional[StrictStr] = Field(None, alias="requestId")
    __properties = ["transType", "posTenderType", "brand", "cardType", "entryMode", "amount", "currencyCode", "offline", "requestId"]

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
    def from_json(cls, json_str: str) -> Payment:
        """Create an instance of Payment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pos_tender_type
        if self.pos_tender_type:
            _dict['posTenderType'] = self.pos_tender_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Payment:
        """Create an instance of Payment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Payment.parse_obj(obj)

        _obj = Payment.parse_obj({
            "trans_type": obj.get("transType"),
            "pos_tender_type": TenderType.from_dict(obj.get("posTenderType")) if obj.get("posTenderType") is not None else None,
            "brand": obj.get("brand"),
            "card_type": obj.get("cardType"),
            "entry_mode": obj.get("entryMode"),
            "amount": obj.get("amount"),
            "currency_code": obj.get("currencyCode"),
            "offline": obj.get("offline"),
            "request_id": obj.get("requestId")
        })
        return _obj


