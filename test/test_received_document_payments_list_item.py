"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""

import json
import sys
import unittest
import datetime
import fattureincloud_python_sdk
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.received_document_payments_list_item_payment_terms import ReceivedDocumentPaymentsListItemPaymentTerms
globals()['PaymentAccount'] = PaymentAccount
globals()['ReceivedDocumentPaymentsListItemPaymentTerms'] = ReceivedDocumentPaymentsListItemPaymentTerms
from fattureincloud_python_sdk.model.received_document_payments_list_item import ReceivedDocumentPaymentsListItem


class TestReceivedDocumentPaymentsListItem(unittest.TestCase):
    """ReceivedDocumentPaymentsListItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReceivedDocumentPaymentsListItem(self):
        """Test ReceivedDocumentPaymentsListItem"""
        model = ReceivedDocumentPaymentsListItem(
            id=1,
            amount=10.0,
            due_date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(),
            paid_date_date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(),
            status="ok",
            payment_account=PaymentAccount(
                id=1,
                name="bank"
            )
        )
        expected_json = '{"id": 1, "amount": 10.0, "due_date": "2022-01-01", "paid_date_date": "2022-01-01", "status": "ok", "payment_account": {"id": 1, "name": "bank"}}'
        actual_json = json.dumps(model.to_dict(), default=json_serial)
        assert actual_json == expected_json

if __name__ == '__main__':
    unittest.main()
