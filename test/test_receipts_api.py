"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import datetime
import functions
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import RESTResponse
from fattureincloud_python_sdk.api.receipts_api import ReceiptsApi
from fattureincloud_python_sdk.model.create_receipt_response import CreateReceiptResponse
from fattureincloud_python_sdk.model.get_receipt_pre_create_info_response import GetReceiptPreCreateInfoResponse
from fattureincloud_python_sdk.model.get_receipt_response import GetReceiptResponse
from fattureincloud_python_sdk.model.get_receipts_monthly_totals_response import GetReceiptsMonthlyTotalsResponse
from fattureincloud_python_sdk.model.list_receipts_response import ListReceiptsResponse
from fattureincloud_python_sdk.model.modify_receipt_response import ModifyReceiptResponse
from fattureincloud_python_sdk.model.monthly_total import MonthlyTotal
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.receipt import Receipt
from fattureincloud_python_sdk.model.receipt_items_list_item import ReceiptItemsListItem
from fattureincloud_python_sdk.model.receipt_pre_create_info import ReceiptPreCreateInfo
from fattureincloud_python_sdk.model.receipt_type import ReceiptType
from fattureincloud_python_sdk.model.vat_type import VatType  # noqa: E501


class TestReceiptsApi(unittest.TestCase):
    """ReceiptsApi unit test stubs"""

    def setUp(self):
        self.api = ReceiptsApi()

    def tearDown(self):
        pass

    def test_create_receipt(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "date": "2022-01-01", "number": 3.14, "numeration": "numeration_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_gross": 3.14, "use_gross_prices": false, "type": "till_receipt", "description": "description_example", "rc_center": "rc_center_example", "created_at": "created_at_example", "updated_at": "updated_at_example", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "items_list": [{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}]}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreateReceiptResponse(data = Receipt( id=2, date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(), number=3.14, numeration="numeration_example", amount_net=3.14, amount_vat=3.14, amount_gross=3.14, use_gross_prices=False, type=ReceiptType("till_receipt"), description="description_example", rc_center="rc_center_example", created_at="created_at_example", updated_at="updated_at_example", payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), items_list=[ ReceiptItemsListItem( id=3, amount_net=3.14, amount_gross=3.14, category="category_example", vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ) ) ] ) )
        actual = self.api.create_receipt(2)
        actual.data.id = 2
        assert actual == expected

    def test_delete_receipt(self):
        resp = {
            'status': 200,
            'data': b'{}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.DELETE = unittest.mock.MagicMock(return_value = mock_resp)
        actual = self.api.delete_receipt(2, 12345)
        assert actual == None

    def test_get_receipt(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "date": "2022-01-01", "number": 3.14, "numeration": "numeration_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_gross": 3.14, "use_gross_prices": false, "type": "till_receipt", "description": "description_example", "rc_center": "rc_center_example", "created_at": "created_at_example", "updated_at": "updated_at_example", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "items_list": [{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}]}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetReceiptResponse(data = Receipt( id=2, date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(), number=3.14, numeration="numeration_example", amount_net=3.14, amount_vat=3.14, amount_gross=3.14, use_gross_prices=False, type=ReceiptType("till_receipt"), description="description_example", rc_center="rc_center_example", created_at="created_at_example", updated_at="updated_at_example", payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), items_list=[ ReceiptItemsListItem( id=3, amount_net=3.14, amount_gross=3.14, category="category_example", vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ) ) ] ) )
        actual = self.api.get_receipt(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_get_receipt_pre_create_info(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"numerations_list": ["a/", "b/"], "rc_centers_list": ["bg", "mi"], "payment_accounts_list": [{"id": 1, "name": "bank"}], "categories_list": ["cat5", "cat6"], "vat_types_list": [{"value": 22.0}]}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetReceiptPreCreateInfoResponse( data=ReceiptPreCreateInfo( numerations_list=[ "a/", "b/" ], rc_centers_list=[ "bg", "mi" ], payment_accounts_list=[ PaymentAccount( id=1, name="bank" ) ], categories_list=[ "cat5", "cat6" ], vat_types_list=[ VatType( value=22.0 ) ] ) )
        actual = self.api.get_receipt_pre_create_info(2)
        assert actual == expected

    def test_get_receipts_monthly_totals(self):
        resp = {
            'status': 200,
            'data': b'{"data": [{"net": 1000.0, "gross": 1220.0, "count": 10.0}, {"net": 1500.0, "gross": 1730.0, "count": 15.0}]}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetReceiptsMonthlyTotalsResponse( data=[ MonthlyTotal( net=1000.0, gross=1220.0, count=10.0 ), MonthlyTotal( net=1500.0, gross=1730.0, count=15.0 ) ] )
        actual = self.api.get_receipts_monthly_totals(2, "till_receipt", "2022")
        assert actual == expected

    def test_list_receipts(self):
        resp = {
            'status': 200,
            'data': b'{"data": [{"id": 1, "date": "2022-01-01", "number": 3.14, "numeration": "numeration_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_gross": 3.14, "use_gross_prices": false, "type": "till_receipt", "description": "description_example", "rc_center": "rc_center_example", "created_at": "created_at_example", "updated_at": "updated_at_example", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "items_list": [{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}]}]}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ListReceiptsResponse(data = [Receipt( id=2, date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(), number=3.14, numeration="numeration_example", amount_net=3.14, amount_vat=3.14, amount_gross=3.14, use_gross_prices=False, type=ReceiptType("till_receipt"), description="description_example", rc_center="rc_center_example", created_at="created_at_example", updated_at="updated_at_example", payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), items_list=[ ReceiptItemsListItem( id=3, amount_net=3.14, amount_gross=3.14, category="category_example", vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ) ) ] ) ] )
        actual = self.api.list_receipts(2)
        actual.data[0].id = 2
        assert actual == expected

    def test_modify_receipt(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "date": "2022-01-01", "number": 3.14, "numeration": "numeration_example", "amount_net": 3.14, "amount_vat": 3.14, "amount_gross": 3.14, "use_gross_prices": false, "type": "till_receipt", "description": "description_example", "rc_center": "rc_center_example", "created_at": "created_at_example", "updated_at": "updated_at_example", "payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "items_list": [{"id": 3, "amount_net": 3.14, "amount_gross": 3.14, "category": "category_example", "vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}}]}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyReceiptResponse(data = Receipt( id=2, date=datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date(), number=3.14, numeration="numeration_example", amount_net=3.14, amount_vat=3.14, amount_gross=3.14, use_gross_prices=False, type=ReceiptType("till_receipt"), description="description_example", rc_center="rc_center_example", created_at="created_at_example", updated_at="updated_at_example", payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), items_list=[ ReceiptItemsListItem( id=3, amount_net=3.14, amount_gross=3.14, category="category_example", vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ) ) ] ) )
        actual = self.api.modify_receipt(2, 12345)
        actual.data.id = 2
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
