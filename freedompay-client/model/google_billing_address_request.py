# coding: utf-8

"""
    Hosted Payment Controls API Documentation v1.5

    The API for Hosted Payment Controls. To access the swagger.json file open the following link: https://hpc.uat.freedompay.com/api/swagger/docs/v1.5  # noqa: E501

    The version of the OpenAPI document: v1.5
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from freedompay-client import schemas  # noqa: F401


class GoogleBillingAddressRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class Format(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Unknown": "UNKNOWN",
                        "Min": "MIN",
                        "Full": "FULL",
                    }
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("Unknown")
                
                @schemas.classproperty
                def MIN(cls):
                    return cls("Min")
                
                @schemas.classproperty
                def FULL(cls):
                    return cls("Full")
            IsRequired = schemas.BoolSchema
            IsPhoneNumberRequired = schemas.BoolSchema
            __annotations__ = {
                "Format": Format,
                "IsRequired": IsRequired,
                "IsPhoneNumberRequired": IsPhoneNumberRequired,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Format"]) -> MetaOapg.properties.Format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsRequired"]) -> MetaOapg.properties.IsRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsPhoneNumberRequired"]) -> MetaOapg.properties.IsPhoneNumberRequired: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Format", "IsRequired", "IsPhoneNumberRequired", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Format"]) -> typing.Union[MetaOapg.properties.Format, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsRequired"]) -> typing.Union[MetaOapg.properties.IsRequired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsPhoneNumberRequired"]) -> typing.Union[MetaOapg.properties.IsPhoneNumberRequired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Format", "IsRequired", "IsPhoneNumberRequired", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Format: typing.Union[MetaOapg.properties.Format, str, schemas.Unset] = schemas.unset,
        IsRequired: typing.Union[MetaOapg.properties.IsRequired, bool, schemas.Unset] = schemas.unset,
        IsPhoneNumberRequired: typing.Union[MetaOapg.properties.IsPhoneNumberRequired, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoogleBillingAddressRequest':
        return super().__new__(
            cls,
            *args,
            Format=Format,
            IsRequired=IsRequired,
            IsPhoneNumberRequired=IsPhoneNumberRequired,
            _configuration=_configuration,
            **kwargs,
        )
