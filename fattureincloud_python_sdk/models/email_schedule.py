# coding: utf-8

"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 500.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.

    The version of the OpenAPI document: 2.0.30
    Contact: info@fattureincloud.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from fattureincloud_python_sdk.models.email_schedule_include import EmailScheduleInclude


class EmailSchedule(BaseModel):
    """
    EmailSchedule
    """

    sender_id: Optional[StrictInt] = Field(
        None,
        description="Email sender id [required if **sender_email** is not specified]",
    )
    sender_email: Optional[StrictStr] = Field(
        None,
        description="Email sender address [required if **sender_id** is not specified]",
    )
    recipient_email: Optional[StrictStr] = Field(
        None, description="Email recipient emails [comma separated]"
    )
    subject: Optional[StrictStr] = Field(None, description="Email subject")
    body: Optional[StrictStr] = Field(
        None, description="Email body [HTML Escaped] [max size 50KiB]"
    )
    include: Optional[EmailScheduleInclude] = None
    attach_pdf: Optional[StrictBool] = Field(
        None, description="Attach the pdf of the document"
    )
    send_copy: Optional[StrictBool] = Field(
        None,
        description="Send a copy of the email to the **cc_email** specified by **Get email data**",
    )
    __properties = [
        "sender_id",
        "sender_email",
        "recipient_email",
        "subject",
        "body",
        "include",
        "attach_pdf",
        "send_copy",
    ]

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
    def from_json(cls, json_str: str) -> EmailSchedule:
        """Create an instance of EmailSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of include
        if self.include:
            _dict["include"] = self.include.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmailSchedule:
        """Create an instance of EmailSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmailSchedule.parse_obj(obj)

        _obj = EmailSchedule.parse_obj(
            {
                "sender_id": obj.get("sender_id")
                if obj.get("sender_id") is not None
                else None,
                "sender_email": obj.get("sender_email")
                if obj.get("sender_email") is not None
                else None,
                "recipient_email": obj.get("recipient_email")
                if obj.get("recipient_email") is not None
                else None,
                "subject": obj.get("subject")
                if obj.get("subject") is not None
                else None,
                "body": obj.get("body") if obj.get("body") is not None else None,
                "include": EmailScheduleInclude.from_dict(obj.get("include"))
                if obj.get("include") is not None
                else None,
                "attach_pdf": obj.get("attach_pdf")
                if obj.get("attach_pdf") is not None
                else None,
                "send_copy": obj.get("send_copy")
                if obj.get("send_copy") is not None
                else None,
            }
        )
        return _obj
