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
from freedompay_client.models.consumer_authentication import ConsumerAuthentication
from freedompay_client.models.google_billing_address_request import GoogleBillingAddressRequest
from freedompay_client.models.legal_control import LegalControl

class GooglePayInitRequest(BaseModel):
    """
    GooglePayInitRequest
    """
    billing_address: Optional[GoogleBillingAddressRequest] = Field(None, alias="BillingAddress")
    button_color: Optional[StrictStr] = Field(None, alias="ButtonColor")
    button_type: Optional[StrictStr] = Field(None, alias="ButtonType")
    button_size_mode: Optional[StrictStr] = Field(None, alias="ButtonSizeMode")
    consumer_authentication: Optional[ConsumerAuthentication] = Field(None, alias="ConsumerAuthentication")
    currency_code: Optional[StrictStr] = Field(None, alias="CurrencyCode")
    is_email_required: Optional[StrictBool] = Field(None, alias="IsEmailRequired")
    response_type: Optional[StrictStr] = Field(None, alias="ResponseType")
    total_price: Optional[StrictStr] = Field(None, alias="TotalPrice")
    culture_code: Optional[StrictStr] = Field(None, alias="CultureCode")
    es_key: Optional[StrictStr] = Field(None, alias="EsKey")
    legal: Optional[LegalControl] = Field(None, alias="Legal")
    store_id: Optional[StrictStr] = Field(None, alias="StoreId")
    styles: Optional[StrictStr] = Field(None, alias="Styles")
    terminal_id: Optional[StrictStr] = Field(None, alias="TerminalId")
    validation_message_type: Optional[StrictStr] = Field(None, alias="ValidationMessageType")
    reference_id: Optional[StrictStr] = Field(None, alias="ReferenceId")
    __properties = ["BillingAddress", "ButtonColor", "ButtonType", "ButtonSizeMode", "ConsumerAuthentication", "CurrencyCode", "IsEmailRequired", "ResponseType", "TotalPrice", "CultureCode", "EsKey", "Legal", "StoreId", "Styles", "TerminalId", "ValidationMessageType", "ReferenceId"]

    @validator('button_color')
    def button_color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Black', 'White'):
            raise ValueError("must be one of enum values ('Unknown', 'Black', 'White')")
        return value

    @validator('button_type')
    def button_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Icon', 'Buy', 'Checkout', 'Donate', 'Order', 'Pay', 'Plain', 'Subscribe', 'Book'):
            raise ValueError("must be one of enum values ('Unknown', 'Icon', 'Buy', 'Checkout', 'Donate', 'Order', 'Pay', 'Plain', 'Subscribe', 'Book')")
        return value

    @validator('button_size_mode')
    def button_size_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Static', 'Fill'):
            raise ValueError("must be one of enum values ('Static', 'Fill')")
        return value

    @validator('response_type')
    def response_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Dictionary', 'Raw'):
            raise ValueError("must be one of enum values ('Unknown', 'Dictionary', 'Raw')")
        return value

    @validator('validation_message_type')
    def validation_message_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'None', 'Feedback', 'Tooltip'):
            raise ValueError("must be one of enum values ('Unknown', 'None', 'Feedback', 'Tooltip')")
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
    def from_json(cls, json_str: str) -> GooglePayInitRequest:
        """Create an instance of GooglePayInitRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['BillingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consumer_authentication
        if self.consumer_authentication:
            _dict['ConsumerAuthentication'] = self.consumer_authentication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legal
        if self.legal:
            _dict['Legal'] = self.legal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GooglePayInitRequest:
        """Create an instance of GooglePayInitRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GooglePayInitRequest.parse_obj(obj)

        _obj = GooglePayInitRequest.parse_obj({
            "billing_address": GoogleBillingAddressRequest.from_dict(obj.get("BillingAddress")) if obj.get("BillingAddress") is not None else None,
            "button_color": obj.get("ButtonColor"),
            "button_type": obj.get("ButtonType"),
            "button_size_mode": obj.get("ButtonSizeMode"),
            "consumer_authentication": ConsumerAuthentication.from_dict(obj.get("ConsumerAuthentication")) if obj.get("ConsumerAuthentication") is not None else None,
            "currency_code": obj.get("CurrencyCode"),
            "is_email_required": obj.get("IsEmailRequired"),
            "response_type": obj.get("ResponseType"),
            "total_price": obj.get("TotalPrice"),
            "culture_code": obj.get("CultureCode"),
            "es_key": obj.get("EsKey"),
            "legal": LegalControl.from_dict(obj.get("Legal")) if obj.get("Legal") is not None else None,
            "store_id": obj.get("StoreId"),
            "styles": obj.get("Styles"),
            "terminal_id": obj.get("TerminalId"),
            "validation_message_type": obj.get("ValidationMessageType"),
            "reference_id": obj.get("ReferenceId")
        })
        return _obj


