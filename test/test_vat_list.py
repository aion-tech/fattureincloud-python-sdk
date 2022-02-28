"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.13
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import json
import sys
import unittest

import fattureincloud_python_sdk
from fattureincloud_python_sdk.model.vat_item import VatItem
from functions import json_serial
globals()['VatItem'] = VatItem
from fattureincloud_python_sdk.model.vat_list import VatList


class TestVatList(unittest.TestCase):
    """VatList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVatList(self):
        """Test VatList"""
        model = VatList( 
            vat_item=VatItem(
                amount_net=100.0,
                amount_vat=22.0
            )
        )
        expected_json = "{\"vat_item\": {\"amount_net\": 100.0, \"amount_vat\": 22.0}}"
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json


if __name__ == '__main__':
    unittest.main()
