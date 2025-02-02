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
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class Snapshot(ResourceMetadata):
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
        'tenant': 'TenantRef',
        'tenant_space': 'TenantSpaceRef',
        'volume_snapshots_link': 'str',
        'protection_policy': 'ProtectionPolicyRef',
        'time_remaining': 'int',
        'destroyed': 'bool'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'tenant': 'tenant',
        'tenant_space': 'tenant_space',
        'volume_snapshots_link': 'volume_snapshots_link',
        'protection_policy': 'protection_policy',
        'time_remaining': 'time_remaining',
        'destroyed': 'destroyed'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, tenant=None, tenant_space=None, volume_snapshots_link=None, protection_policy=None, time_remaining=None, destroyed=None, *args, **kwargs):  # noqa: E501
        """Snapshot - a model defined in Swagger"""  # noqa: E501
        self._tenant = None
        self._tenant_space = None
        self._volume_snapshots_link = None
        self._protection_policy = None
        self._time_remaining = None
        self._destroyed = None
        self.discriminator = None
        self.tenant = tenant
        self.tenant_space = tenant_space
        self.volume_snapshots_link = volume_snapshots_link
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if destroyed is not None:
            self.destroyed = destroyed
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def tenant(self):
        """Gets the tenant of this Snapshot.  # noqa: E501


        :return: The tenant of this Snapshot.  # noqa: E501
        :rtype: TenantRef
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this Snapshot.


        :param tenant: The tenant of this Snapshot.  # noqa: E501
        :type: TenantRef
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def tenant_space(self):
        """Gets the tenant_space of this Snapshot.  # noqa: E501


        :return: The tenant_space of this Snapshot.  # noqa: E501
        :rtype: TenantSpaceRef
        """
        return self._tenant_space

    @tenant_space.setter
    def tenant_space(self, tenant_space):
        """Sets the tenant_space of this Snapshot.


        :param tenant_space: The tenant_space of this Snapshot.  # noqa: E501
        :type: TenantSpaceRef
        """
        if tenant_space is None:
            raise ValueError("Invalid value for `tenant_space`, must not be `None`")  # noqa: E501

        self._tenant_space = tenant_space

    @property
    def volume_snapshots_link(self):
        """Gets the volume_snapshots_link of this Snapshot.  # noqa: E501

        The URI of volume snapshots in the snapshot.  # noqa: E501

        :return: The volume_snapshots_link of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._volume_snapshots_link

    @volume_snapshots_link.setter
    def volume_snapshots_link(self, volume_snapshots_link):
        """Sets the volume_snapshots_link of this Snapshot.

        The URI of volume snapshots in the snapshot.  # noqa: E501

        :param volume_snapshots_link: The volume_snapshots_link of this Snapshot.  # noqa: E501
        :type: str
        """
        if volume_snapshots_link is None:
            raise ValueError("Invalid value for `volume_snapshots_link`, must not be `None`")  # noqa: E501

        self._volume_snapshots_link = volume_snapshots_link

    @property
    def protection_policy(self):
        """Gets the protection_policy of this Snapshot.  # noqa: E501


        :return: The protection_policy of this Snapshot.  # noqa: E501
        :rtype: ProtectionPolicyRef
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this Snapshot.


        :param protection_policy: The protection_policy of this Snapshot.  # noqa: E501
        :type: ProtectionPolicyRef
        """

        self._protection_policy = protection_policy

    @property
    def time_remaining(self):
        """Gets the time_remaining of this Snapshot.  # noqa: E501

        The amount of time left until the destroyed snapshot is permanently eradicated. Measured in milliseconds. Before the time_remaining period has elapsed, the destroyed snapshot can be recovered by setting destroyed=false.  # noqa: E501

        :return: The time_remaining of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this Snapshot.

        The amount of time left until the destroyed snapshot is permanently eradicated. Measured in milliseconds. Before the time_remaining period has elapsed, the destroyed snapshot can be recovered by setting destroyed=false.  # noqa: E501

        :param time_remaining: The time_remaining of this Snapshot.  # noqa: E501
        :type: int
        """

        self._time_remaining = time_remaining

    @property
    def destroyed(self):
        """Gets the destroyed of this Snapshot.  # noqa: E501

        True if the snapshot has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed snapshot is permanently eradicated. Before the time_remaining period has elapsed, the destroyed snapshot can be recovered by setting destroyed=false. Once the time_remaining period has elapsed, the snapshot is permanently eradicated and can no longer be recovered.  # noqa: E501

        :return: The destroyed of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """Sets the destroyed of this Snapshot.

        True if the snapshot has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed snapshot is permanently eradicated. Before the time_remaining period has elapsed, the destroyed snapshot can be recovered by setting destroyed=false. Once the time_remaining period has elapsed, the snapshot is permanently eradicated and can no longer be recovered.  # noqa: E501

        :param destroyed: The destroyed of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._destroyed = destroyed

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
        if issubclass(Snapshot, dict):
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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
