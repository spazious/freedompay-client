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

class AutoRentalData(BaseModel):
    """
    AutoRentalData
    """
    expected_duration: Optional[StrictStr] = Field(None, alias="expectedDuration")
    agreement_number: Optional[StrictStr] = Field(None, alias="agreementNumber")
    checkout_date: Optional[StrictStr] = Field(None, alias="checkoutDate")
    checkin_date: Optional[StrictStr] = Field(None, alias="checkinDate")
    rental_rate: Optional[StrictStr] = Field(None, alias="rentalRate")
    rental_rate_unit: Optional[StrictStr] = Field(None, alias="rentalRateUnit")
    rental_class_id: Optional[StrictStr] = Field(None, alias="rentalClassId")
    no_show: Optional[StrictStr] = Field(None, alias="noShow")
    renter_name: Optional[StrictStr] = Field(None, alias="renterName")
    return_location_id: Optional[StrictStr] = Field(None, alias="returnLocationId")
    return_city: Optional[StrictStr] = Field(None, alias="returnCity")
    return_state: Optional[StrictStr] = Field(None, alias="returnState")
    return_country: Optional[StrictStr] = Field(None, alias="returnCountry")
    extra_charge_types: Optional[StrictStr] = Field(None, alias="extraChargeTypes")
    extra_charge_total: Optional[StrictStr] = Field(None, alias="extraChargeTotal")
    extra_charge_notified: Optional[StrictStr] = Field(None, alias="extraChargeNotified")
    __properties = ["expectedDuration", "agreementNumber", "checkoutDate", "checkinDate", "rentalRate", "rentalRateUnit", "rentalClassId", "noShow", "renterName", "returnLocationId", "returnCity", "returnState", "returnCountry", "extraChargeTypes", "extraChargeTotal", "extraChargeNotified"]

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
    def from_json(cls, json_str: str) -> AutoRentalData:
        """Create an instance of AutoRentalData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AutoRentalData:
        """Create an instance of AutoRentalData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutoRentalData.parse_obj(obj)

        _obj = AutoRentalData.parse_obj({
            "expected_duration": obj.get("expectedDuration"),
            "agreement_number": obj.get("agreementNumber"),
            "checkout_date": obj.get("checkoutDate"),
            "checkin_date": obj.get("checkinDate"),
            "rental_rate": obj.get("rentalRate"),
            "rental_rate_unit": obj.get("rentalRateUnit"),
            "rental_class_id": obj.get("rentalClassId"),
            "no_show": obj.get("noShow"),
            "renter_name": obj.get("renterName"),
            "return_location_id": obj.get("returnLocationId"),
            "return_city": obj.get("returnCity"),
            "return_state": obj.get("returnState"),
            "return_country": obj.get("returnCountry"),
            "extra_charge_types": obj.get("extraChargeTypes"),
            "extra_charge_total": obj.get("extraChargeTotal"),
            "extra_charge_notified": obj.get("extraChargeNotified")
        })
        return _obj


