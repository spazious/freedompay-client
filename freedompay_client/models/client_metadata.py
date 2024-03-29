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

class ClientMetadata(BaseModel):
    """
    ClientMetadata
    """
    application_name: Optional[StrictStr] = Field(None, alias="applicationName")
    application_version: Optional[StrictStr] = Field(None, alias="applicationVersion")
    workstation_id: Optional[StrictStr] = Field(None, alias="workstationId")
    application_user: Optional[StrictStr] = Field(None, alias="applicationUser")
    environment: Optional[StrictStr] = None
    library: Optional[StrictStr] = None
    library_version: Optional[StrictStr] = Field(None, alias="libraryVersion")
    security_library: Optional[StrictStr] = Field(None, alias="securityLibrary")
    security_library_version: Optional[StrictStr] = Field(None, alias="securityLibraryVersion")
    test_run: Optional[StrictStr] = Field(None, alias="testRun")
    test_case: Optional[StrictStr] = Field(None, alias="testCase")
    poi_device_identifier: Optional[StrictStr] = Field(None, alias="poiDeviceIdentifier")
    selling_system_name: Optional[StrictStr] = Field(None, alias="sellingSystemName")
    selling_system_version: Optional[StrictStr] = Field(None, alias="sellingSystemVersion")
    selling_middleware_name: Optional[StrictStr] = Field(None, alias="sellingMiddlewareName")
    selling_middleware_version: Optional[StrictStr] = Field(None, alias="sellingMiddlewareVersion")
    __properties = ["applicationName", "applicationVersion", "workstationId", "applicationUser", "environment", "library", "libraryVersion", "securityLibrary", "securityLibraryVersion", "testRun", "testCase", "poiDeviceIdentifier", "sellingSystemName", "sellingSystemVersion", "sellingMiddlewareName", "sellingMiddlewareVersion"]

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
    def from_json(cls, json_str: str) -> ClientMetadata:
        """Create an instance of ClientMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientMetadata:
        """Create an instance of ClientMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientMetadata.parse_obj(obj)

        _obj = ClientMetadata.parse_obj({
            "application_name": obj.get("applicationName"),
            "application_version": obj.get("applicationVersion"),
            "workstation_id": obj.get("workstationId"),
            "application_user": obj.get("applicationUser"),
            "environment": obj.get("environment"),
            "library": obj.get("library"),
            "library_version": obj.get("libraryVersion"),
            "security_library": obj.get("securityLibrary"),
            "security_library_version": obj.get("securityLibraryVersion"),
            "test_run": obj.get("testRun"),
            "test_case": obj.get("testCase"),
            "poi_device_identifier": obj.get("poiDeviceIdentifier"),
            "selling_system_name": obj.get("sellingSystemName"),
            "selling_system_version": obj.get("sellingSystemVersion"),
            "selling_middleware_name": obj.get("sellingMiddlewareName"),
            "selling_middleware_version": obj.get("sellingMiddlewareVersion")
        })
        return _obj


