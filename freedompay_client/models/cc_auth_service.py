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

class CCAuthService(BaseModel):
    """
    CCAuthService
    """
    trans_type: Optional[StrictStr] = Field(None, alias="transType")
    cof_indicator: Optional[StrictStr] = Field(None, alias="cofIndicator")
    cof_compliance_data: Optional[StrictStr] = Field(None, alias="cofComplianceData")
    allow_partial: Optional[StrictStr] = Field(None, alias="allowPartial")
    return_balance: Optional[StrictStr] = Field(None, alias="returnBalance")
    auth_type: Optional[StrictStr] = Field(None, alias="authType")
    verbal_auth_code: Optional[StrictStr] = Field(None, alias="verbalAuthCode")
    ecom3ds: Optional[StrictStr] = None
    cavv: Optional[StrictStr] = None
    xid: Optional[StrictStr] = None
    orig_auth_amount: Optional[StrictStr] = Field(None, alias="origAuthAmount")
    enable_avs: Optional[StrictStr] = Field(None, alias="enableAVS")
    offline: Optional[StrictStr] = None
    offline_code: Optional[StrictStr] = Field(None, alias="offlineCode")
    estimated: Optional[StrictStr] = None
    installment_number: Optional[StrictStr] = Field(None, alias="installmentNumber")
    installment_count: Optional[StrictStr] = Field(None, alias="installmentCount")
    auth3dsformat: Optional[StrictStr] = None
    auth3dsjson: Optional[StrictStr] = None
    sca_exemptions: Optional[StrictStr] = Field(None, alias="scaExemptions")
    sca_upgrade: Optional[StrictStr] = Field(None, alias="scaUpgrade")
    request_par: Optional[StrictStr] = Field(None, alias="requestPar")
    bill_payment: Optional[StrictStr] = Field(None, alias="billPayment")
    recurring: Optional[StrictStr] = None
    commerce_indicator: Optional[StrictStr] = Field(None, alias="commerceIndicator")
    partial_payment_id: Optional[StrictStr] = Field(None, alias="partialPaymentId")
    last_payment_flag: Optional[StrictStr] = Field(None, alias="lastPaymentFlag")
    industry_datatype: Optional[StrictStr] = Field(None, alias="industryDatatype")
    run: Optional[StrictStr] = None
    __properties = ["transType", "cofIndicator", "cofComplianceData", "allowPartial", "returnBalance", "authType", "verbalAuthCode", "ecom3ds", "cavv", "xid", "origAuthAmount", "enableAVS", "offline", "offlineCode", "estimated", "installmentNumber", "installmentCount", "auth3dsformat", "auth3dsjson", "scaExemptions", "scaUpgrade", "requestPar", "billPayment", "recurring", "commerceIndicator", "partialPaymentId", "lastPaymentFlag", "industryDatatype", "run"]

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
    def from_json(cls, json_str: str) -> CCAuthService:
        """Create an instance of CCAuthService from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CCAuthService:
        """Create an instance of CCAuthService from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CCAuthService.parse_obj(obj)

        _obj = CCAuthService.parse_obj({
            "trans_type": obj.get("transType"),
            "cof_indicator": obj.get("cofIndicator"),
            "cof_compliance_data": obj.get("cofComplianceData"),
            "allow_partial": obj.get("allowPartial"),
            "return_balance": obj.get("returnBalance"),
            "auth_type": obj.get("authType"),
            "verbal_auth_code": obj.get("verbalAuthCode"),
            "ecom3ds": obj.get("ecom3ds"),
            "cavv": obj.get("cavv"),
            "xid": obj.get("xid"),
            "orig_auth_amount": obj.get("origAuthAmount"),
            "enable_avs": obj.get("enableAVS"),
            "offline": obj.get("offline"),
            "offline_code": obj.get("offlineCode"),
            "estimated": obj.get("estimated"),
            "installment_number": obj.get("installmentNumber"),
            "installment_count": obj.get("installmentCount"),
            "auth3dsformat": obj.get("auth3dsformat"),
            "auth3dsjson": obj.get("auth3dsjson"),
            "sca_exemptions": obj.get("scaExemptions"),
            "sca_upgrade": obj.get("scaUpgrade"),
            "request_par": obj.get("requestPar"),
            "bill_payment": obj.get("billPayment"),
            "recurring": obj.get("recurring"),
            "commerce_indicator": obj.get("commerceIndicator"),
            "partial_payment_id": obj.get("partialPaymentId"),
            "last_payment_flag": obj.get("lastPaymentFlag"),
            "industry_datatype": obj.get("industryDatatype"),
            "run": obj.get("run")
        })
        return _obj


