# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.27
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from fattureincloud_python_sdk.models.payment_account import PaymentAccount
from fattureincloud_python_sdk.models.vat_type import VatType


class ReceiptPreCreateInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    numerations: Optional[Dict[str, Dict[str, StrictInt]]] = None
    numerations_list: Optional[conlist(StrictStr)] = Field(
        None, description="List of series used in the past."
    )
    rc_centers_list: Optional[conlist(StrictStr)] = Field(
        None, description="List of revenue centers used in the past."
    )
    payment_accounts_list: Optional[conlist(PaymentAccount)] = Field(
        None, description="User payment accounts list."
    )
    categories_list: Optional[conlist(StrictStr)] = Field(
        None, description="List of categories used in the past."
    )
    vat_types_list: Optional[conlist(VatType)] = Field(
        None,
        description="List of user vat types with the default 22%, 10%, 4% and 0% vats.",
    )
    __properties = [
        "numerations",
        "numerations_list",
        "rc_centers_list",
        "payment_accounts_list",
        "categories_list",
        "vat_types_list",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ReceiptPreCreateInfo:
        """Create an instance of ReceiptPreCreateInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in payment_accounts_list (list)
        _items = []
        if self.payment_accounts_list:
            for _item in self.payment_accounts_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["payment_accounts_list"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vat_types_list (list)
        _items = []
        if self.vat_types_list:
            for _item in self.vat_types_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["vat_types_list"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReceiptPreCreateInfo:
        """Create an instance of ReceiptPreCreateInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReceiptPreCreateInfo.parse_obj(obj)

        _obj = ReceiptPreCreateInfo.parse_obj(
            {
                "numerations": obj.get("numerations"),
                "numerations_list": obj.get("numerations_list"),
                "rc_centers_list": obj.get("rc_centers_list"),
                "payment_accounts_list": [
                    PaymentAccount.from_dict(_item)
                    for _item in obj.get("payment_accounts_list")
                ]
                if obj.get("payment_accounts_list") is not None
                else None,
                "categories_list": obj.get("categories_list"),
                "vat_types_list": [
                    VatType.from_dict(_item) for _item in obj.get("vat_types_list")
                ]
                if obj.get("vat_types_list") is not None
                else None,
            }
        )
        return _obj
