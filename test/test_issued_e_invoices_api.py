"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import RESTResponse
import functions
from fattureincloud_python_sdk.api.issued_e_invoices_api import IssuedEInvoicesApi
from fattureincloud_python_sdk.models.send_e_invoice_response import (
    SendEInvoiceResponse,
)
from fattureincloud_python_sdk.models.send_e_invoice_response_data import (
    SendEInvoiceResponseData,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response import (
    VerifyEInvoiceXmlResponse,
)
from fattureincloud_python_sdk.models.verify_e_invoice_xml_response_data import (
    VerifyEInvoiceXmlResponseData,
)
from fattureincloud_python_sdk.models.get_e_invoice_rejection_reason_response import (
    GetEInvoiceRejectionReasonResponse,
)
from fattureincloud_python_sdk.models.e_invoice_rejection_reason import (
    EInvoiceRejectionReason,
)


class TestIssuedEInvoicesApi(unittest.TestCase):
    """IssuedEInvoicesApi unit test stubs"""

    def setUp(self):
        self.api = IssuedEInvoicesApi()

    def tearDown(self):
        pass

    def test_send_e_invoice(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"name": "msg", "date": "2022-01-01"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.post_request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = SendEInvoiceResponse(
            data=SendEInvoiceResponseData(name="msg2", date="2022-01-01")
        )
        actual = self.api.send_e_invoice(2, 1234)
        actual.data.name = "msg2"
        assert actual == expected

    def test_verify_e_invoice_xml(self):
        resp = {"status": 200, "data": b'{"data": {"success": true}}', "reason": "OK"}

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.get_request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = VerifyEInvoiceXmlResponse(
            data=VerifyEInvoiceXmlResponseData(success=True)
        )
        actual = self.api.verify_e_invoice_xml(2, 1234)
        assert actual == expected

    def test_get_e_invoice_rejection_reason(self):
        resp = {
            "status": 200,
            "data": b'{"data": {"reason": "invalid date"}}',
            "reason": "OK",
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value=None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value=None)

        self.api.api_client.rest_client.get_request = unittest.mock.MagicMock(
            return_value=mock_resp
        )
        expected = GetEInvoiceRejectionReasonResponse(
            data=EInvoiceRejectionReason(reason="invalid date")
        )
        actual = self.api.get_e_invoice_rejection_reason(2, 1234)
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
