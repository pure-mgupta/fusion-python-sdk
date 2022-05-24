# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StorageEndpointIscsiDiscoveryInterfacePost(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'str',
        'gateway': 'str',
        'network_interface_groups': 'list[str]'
    }

    attribute_map = {
        'address': 'address',
        'gateway': 'gateway',
        'network_interface_groups': 'network_interface_groups'
    }

    def __init__(self, address=None, gateway=None, network_interface_groups=None):  # noqa: E501
        """StorageEndpointIscsiDiscoveryInterfacePost - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._gateway = None
        self._network_interface_groups = None
        self.discriminator = None
        self.address = address
        if gateway is not None:
            self.gateway = gateway
        if network_interface_groups is not None:
            self.network_interface_groups = network_interface_groups

    @property
    def address(self):
        """Gets the address of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501

        The IPv4 address for this interface.  # noqa: E501

        :return: The address of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StorageEndpointIscsiDiscoveryInterfacePost.

        The IPv4 address for this interface.  # noqa: E501

        :param address: The address of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def gateway(self):
        """Gets the gateway of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501

        The IPv4 address of the gateway through which this interface will communicate with the network.  # noqa: E501

        :return: The gateway of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this StorageEndpointIscsiDiscoveryInterfacePost.

        The IPv4 address of the gateway through which this interface will communicate with the network.  # noqa: E501

        :param gateway: The gateway of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def network_interface_groups(self):
        """Gets the network_interface_groups of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501


        :return: The network_interface_groups of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_interface_groups

    @network_interface_groups.setter
    def network_interface_groups(self, network_interface_groups):
        """Sets the network_interface_groups of this StorageEndpointIscsiDiscoveryInterfacePost.


        :param network_interface_groups: The network_interface_groups of this StorageEndpointIscsiDiscoveryInterfacePost.  # noqa: E501
        :type: list[str]
        """

        self._network_interface_groups = network_interface_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StorageEndpointIscsiDiscoveryInterfacePost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StorageEndpointIscsiDiscoveryInterfacePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
