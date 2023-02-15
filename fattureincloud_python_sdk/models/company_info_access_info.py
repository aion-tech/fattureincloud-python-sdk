# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool
from fattureincloud_python_sdk.models.permissions import Permissions
from fattureincloud_python_sdk.models.user_company_role import UserCompanyRole


class CompanyInfoAccessInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    role: Optional[UserCompanyRole] = None
    permissions: Optional[Permissions] = None
    through_accountant: Optional[StrictBool] = None
    __properties = ["role", "permissions", "through_accountant"]

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
    def from_json(cls, json_str: str) -> CompanyInfoAccessInfo:
        """Create an instance of CompanyInfoAccessInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict["permissions"] = self.permissions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyInfoAccessInfo:
        """Create an instance of CompanyInfoAccessInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CompanyInfoAccessInfo.parse_obj(obj)

        _obj = CompanyInfoAccessInfo.parse_obj(
            {
                "role": obj.get("role"),
                "permissions": Permissions.from_dict(obj.get("permissions"))
                if obj.get("permissions") is not None
                else None,
                "through_accountant": obj.get("through_accountant")
                if obj.get("through_accountant") is not None
                else None,
            }
        )
        return _obj