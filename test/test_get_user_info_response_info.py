"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.get_user_info_response_info import GetUserInfoResponseInfo
from fattureincloud_python_sdk.model.user import User
from fattureincloud_python_sdk.model.get_user_info_response_email_confirmation_state import GetUserInfoResponseEmailConfirmationState


class TestGetUserInfoResponseInfo(unittest.TestCase):
    """GetUserInfoResponseInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetUserInfoResponseInfo(self):
        """Test GetUserInfoResponseInfo"""
        model = GetUserInfoResponseInfo(
            need_password_change=False
        )
        expected_json = "{\"need_password_change\": false}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
