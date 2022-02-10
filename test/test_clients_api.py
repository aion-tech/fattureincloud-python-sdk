"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import unittest
import unittest.mock
import functions
import fattureincloud_python_sdk
from fattureincloud_python_sdk.rest import RESTResponse
from functions import json_serial
from functions import create_from_json
from fattureincloud_python_sdk.api.clients_api import ClientsApi
from fattureincloud_python_sdk.model.client import Client
from fattureincloud_python_sdk.model.client_type import ClientType
from fattureincloud_python_sdk.model.default_payment_terms_type import DefaultPaymentTermsType
from fattureincloud_python_sdk.model.payment_account import PaymentAccount
from fattureincloud_python_sdk.model.payment_account_type import PaymentAccountType
from fattureincloud_python_sdk.model.payment_method import PaymentMethod
from fattureincloud_python_sdk.model.payment_method_details import PaymentMethodDetails
from fattureincloud_python_sdk.model.payment_method_type import PaymentMethodType
from fattureincloud_python_sdk.model.vat_type import VatType
from fattureincloud_python_sdk.model.create_client_response import CreateClientResponse
from fattureincloud_python_sdk.model.get_client_response import GetClientResponse
from fattureincloud_python_sdk.model.list_clients_response import ListClientsResponse
from fattureincloud_python_sdk.model.modify_client_response import ModifyClientResponse


class TestClientsApi(unittest.TestCase):
    """ClientsApi unit test stubs"""

    def setUp(self):
        configuration = fattureincloud_python_sdk.Configuration(
            host = "https://api-v2.fattureincloud.it"
        )
        configuration.access_token = 'a/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWYiOiJ6OG1HVmRBbThnTVFpcWd6ZU9ybEZaZWg4SDViSmQ5eSJ9.lXdhLBK1QrvjOWw6sguylp2R0NPmKS6D2DUa9ez69uk'
        self.api = ClientsApi(fattureincloud_python_sdk.ApiClient(configuration))

    def tearDown(self):
        pass

    def test_create_client(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms": 30, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.POST = unittest.mock.MagicMock(return_value = mock_resp)
        expected = CreateClientResponse(data = Client( id=2, code="123", name="Rossi S.r.l.", type=ClientType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", default_vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), default_payment_terms=30, default_payment_terms_type=DefaultPaymentTermsType("standard"), default_payment_method=PaymentMethod( id=1, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example", ), bank_name="bank_name_example", bank_iban="bank_iban_example", bank_swift_code="bank_swift_code_example", shipping_address="shipping_address_example", e_invoice=False, ei_code="ei_code_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.create_client(2)
        actual.data.id = 2
        assert actual == expected

    def test_delete_client(self):
        pass

    def test_get_client(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms": 30, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = GetClientResponse(data = Client( id=2, code="123", name="Rossi S.r.l.", type=ClientType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", default_vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), default_payment_terms=30, default_payment_terms_type=DefaultPaymentTermsType("standard"), default_payment_method=PaymentMethod( id=1, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example", ), bank_name="bank_name_example", bank_iban="bank_iban_example", bank_swift_code="bank_swift_code_example", shipping_address="shipping_address_example", e_invoice=False, ei_code="ei_code_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.get_client(2, 12345)
        actual.data.id = 2
        assert actual == expected

    def test_list_clients(self):
        resp = {
            'status': 200,
            'data': b'{"data": [{"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms": 30, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}, {"id": 2, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms": 30, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}]}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.GET = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ListClientsResponse(data = [Client( id=2, code="123", name="Rossi S.r.l.", type=ClientType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", default_vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), default_payment_terms=30, default_payment_terms_type=DefaultPaymentTermsType("standard"), default_payment_method=PaymentMethod( id=1, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example", ), bank_name="bank_name_example", bank_iban="bank_iban_example", bank_swift_code="bank_swift_code_example", shipping_address="shipping_address_example", e_invoice=False, ei_code="ei_code_example", created_at="created_at_example", updated_at="updated_at_example" ),Client( id=2, code="123", name="Rossi S.r.l.", type=ClientType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", default_vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), default_payment_terms=30, default_payment_terms_type=DefaultPaymentTermsType("standard"), default_payment_method=PaymentMethod( id=1, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example", ), bank_name="bank_name_example", bank_iban="bank_iban_example", bank_swift_code="bank_swift_code_example", shipping_address="shipping_address_example", e_invoice=False, ei_code="ei_code_example", created_at="created_at_example", updated_at="updated_at_example" )] )
        actual = self.api.list_clients(2)
        actual.data[0].id = 2
        assert actual == expected

    def test_modify_client(self):
        resp = {
            'status': 200,
            'data': b'{"data": {"id": 1, "code": "123", "name": "Rossi S.r.l.", "type": "company", "first_name": "first_name_example", "last_name": "last_name_example", "contact_person": "contact_person_example", "vat_number": "IT01234567890", "tax_code": "RSSMRA44A12E890Q", "address_street": "Via dei tigli, 12", "address_postal_code": "24010", "address_city": "Bergamo", "address_province": "BG", "address_extra": "address_extra_example", "country": "Italia", "email": "mario.rossi@example.it", "certified_email": "mario.rossi@pec.example.it", "phone": "phone_example", "fax": "fax_example", "notes": "notes_example", "default_vat": {"id": 1, "value": 22.0, "description": "Non imponibile art. 123", "notes": "IVA non imponibile ai sensi dell articolo 123, comma 2", "e_invoice": true, "ei_type": "2", "ei_description": "ei_description_example", "is_disabled": true}, "default_payment_terms": 30, "default_payment_terms_type": "standard", "default_payment_method": {"id": 1, "name": "name_example", "type": "standard", "is_default": true, "default_payment_account": {"id": 1, "name": "Conto Banca Intesa", "type": "standard", "iban": "iban_example", "sia": "sia_example", "cuc": "cuc_example", "virtual": true}, "details": [{"title": "title_example", "description": "description_example"}], "bank_iban": "bank_iban_example", "bank_name": "bank_name_example", "bank_beneficiary": "bank_beneficiary_example", "ei_payment_method": "ei_payment_method_example"}, "bank_name": "bank_name_example", "bank_iban": "bank_iban_example", "bank_swift_code": "bank_swift_code_example", "shipping_address": "shipping_address_example", "e_invoice": false, "ei_code": "ei_code_example", "created_at": "created_at_example", "updated_at": "updated_at_example"}}',
            'reason': "OK"
        }

        mock_resp = RESTResponse(functions.Dict2Class(resp))
        mock_resp.getheader = unittest.mock.MagicMock(return_value = None)
        mock_resp.getheaders = unittest.mock.MagicMock(return_value = None)

        self.api.api_client.rest_client.PUT = unittest.mock.MagicMock(return_value = mock_resp)
        expected = ModifyClientResponse(data = Client( id=2, code="123", name="Rossi S.r.l.", type=ClientType("company"), first_name="first_name_example", last_name="last_name_example", contact_person="contact_person_example", vat_number="IT01234567890", tax_code="RSSMRA44A12E890Q", address_street="Via dei tigli, 12", address_postal_code="24010", address_city="Bergamo", address_province="BG", address_extra="address_extra_example", country="Italia", email="mario.rossi@example.it", certified_email="mario.rossi@pec.example.it", phone="phone_example", fax="fax_example", notes="notes_example", default_vat=VatType( id=1, value=22.0, description="Non imponibile art. 123", notes="IVA non imponibile ai sensi dell articolo 123, comma 2", e_invoice=True, ei_type="2", ei_description="ei_description_example", is_disabled=True, ), default_payment_terms=30, default_payment_terms_type=DefaultPaymentTermsType("standard"), default_payment_method=PaymentMethod( id=1, name="name_example", type=PaymentMethodType("standard"), is_default=True, default_payment_account=PaymentAccount( id=1, name="Conto Banca Intesa", type=PaymentAccountType("standard"), iban="iban_example", sia="sia_example", cuc="cuc_example", virtual=True, ), details=[ PaymentMethodDetails( title="title_example", description="description_example", ), ], bank_iban="bank_iban_example", bank_name="bank_name_example", bank_beneficiary="bank_beneficiary_example", ei_payment_method="ei_payment_method_example", ), bank_name="bank_name_example", bank_iban="bank_iban_example", bank_swift_code="bank_swift_code_example", shipping_address="shipping_address_example", e_invoice=False, ei_code="ei_code_example", created_at="created_at_example", updated_at="updated_at_example" ) )
        actual = self.api.modify_client(2, 12345)
        actual.data.id = 2
        assert actual == expected


if __name__ == '__main__':
    unittest.main()
