"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.10
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fattureincloud_python_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from fattureincloud_python_sdk.exceptions import ApiAttributeError


def lazy_import():
    from fattureincloud_python_sdk.model.email_data_default_sender_email import EmailDataDefaultSenderEmail
    from fattureincloud_python_sdk.model.sender_email import SenderEmail
    globals()['EmailDataDefaultSenderEmail'] = EmailDataDefaultSenderEmail
    globals()['SenderEmail'] = SenderEmail


class EmailData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'recipient_email': (str, none_type),  # noqa: E501
            'default_sender_email': (EmailDataDefaultSenderEmail, none_type),  # noqa: E501
            'sender_emails_list': ([SenderEmail], none_type),  # noqa: E501
            'cc_email': (str, none_type),  # noqa: E501
            'subject': (str, none_type),  # noqa: E501
            'body': (str, none_type),  # noqa: E501
            'document_exists': (bool, none_type),  # noqa: E501
            'delivery_note_exists': (bool, none_type),  # noqa: E501
            'attachment_exists': (bool, none_type),  # noqa: E501
            'accompanying_invoice_exists': (bool, none_type),  # noqa: E501
            'default_attach_pdf': (bool, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'recipient_email': 'recipient_email',  # noqa: E501
        'default_sender_email': 'default_sender_email',  # noqa: E501
        'sender_emails_list': 'sender_emails_list',  # noqa: E501
        'cc_email': 'cc_email',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'body': 'body',  # noqa: E501
        'document_exists': 'document_exists',  # noqa: E501
        'delivery_note_exists': 'delivery_note_exists',  # noqa: E501
        'attachment_exists': 'attachment_exists',  # noqa: E501
        'accompanying_invoice_exists': 'accompanying_invoice_exists',  # noqa: E501
        'default_attach_pdf': 'default_attach_pdf',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EmailData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            recipient_email (str): Recipient's email. [optional]  # noqa: E501
            default_sender_email (EmailDataDefaultSenderEmail): [optional]  # noqa: E501
            sender_emails_list ([SenderEmail]): List of all emails from which the document can be sent. [optional]  # noqa: E501
            cc_email (str): By default is the logged company email. This is the email address to which a copy will be sent.. [optional]  # noqa: E501
            subject (str): Email subject. [optional]  # noqa: E501
            body (str): Email body. [optional]  # noqa: E501
            document_exists (bool): If the document is not a delivery note, this flag will be set to true. [optional]  # noqa: E501
            delivery_note_exists (bool): If the document is a delivery note, this flag will be set to true. [optional]  # noqa: E501
            attachment_exists (bool): If the document has one or more attachments, this flag will be set to true. [optional]  # noqa: E501
            accompanying_invoice_exists (bool): If an accompanying invoice exists, this flag will be set to true. [optional]  # noqa: E501
            default_attach_pdf (bool): If a pdf is attached, this flag will be set to true. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EmailData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            recipient_email (str): Recipient's email. [optional]  # noqa: E501
            default_sender_email (EmailDataDefaultSenderEmail): [optional]  # noqa: E501
            sender_emails_list ([SenderEmail]): List of all emails from which the document can be sent. [optional]  # noqa: E501
            cc_email (str): By default is the logged company email. This is the email address to which a copy will be sent.. [optional]  # noqa: E501
            subject (str): Email subject. [optional]  # noqa: E501
            body (str): Email body. [optional]  # noqa: E501
            document_exists (bool): If the document is not a delivery note, this flag will be set to true. [optional]  # noqa: E501
            delivery_note_exists (bool): If the document is a delivery note, this flag will be set to true. [optional]  # noqa: E501
            attachment_exists (bool): If the document has one or more attachments, this flag will be set to true. [optional]  # noqa: E501
            accompanying_invoice_exists (bool): If an accompanying invoice exists, this flag will be set to true. [optional]  # noqa: E501
            default_attach_pdf (bool): If a pdf is attached, this flag will be set to true. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")