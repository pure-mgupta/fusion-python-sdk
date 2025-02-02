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

class VolumeSnapshot(ResourceMetadata):
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
        'serial_number': 'str',
        'volume_serial_number': 'str',
        'created_at': 'int',
        'consistency_id': 'str',
        'destroyed': 'bool',
        'time_remaining': 'int',
        'size': 'int',
        'tenant': 'TenantRef',
        'tenant_space': 'TenantSpaceRef',
        'snapshot': 'SnapshotRef',
        'volume': 'VolumeRef',
        'protection_policy': 'ProtectionPolicyRef',
        'placement_group': 'PlacementGroupRef'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'serial_number': 'serial_number',
        'volume_serial_number': 'volume_serial_number',
        'created_at': 'created_at',
        'consistency_id': 'consistency_id',
        'destroyed': 'destroyed',
        'time_remaining': 'time_remaining',
        'size': 'size',
        'tenant': 'tenant',
        'tenant_space': 'tenant_space',
        'snapshot': 'snapshot',
        'volume': 'volume',
        'protection_policy': 'protection_policy',
        'placement_group': 'placement_group'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, serial_number=None, volume_serial_number=None, created_at=None, consistency_id=None, destroyed=None, time_remaining=None, size=None, tenant=None, tenant_space=None, snapshot=None, volume=None, protection_policy=None, placement_group=None, *args, **kwargs):  # noqa: E501
        """VolumeSnapshot - a model defined in Swagger"""  # noqa: E501
        self._serial_number = None
        self._volume_serial_number = None
        self._created_at = None
        self._consistency_id = None
        self._destroyed = None
        self._time_remaining = None
        self._size = None
        self._tenant = None
        self._tenant_space = None
        self._snapshot = None
        self._volume = None
        self._protection_policy = None
        self._placement_group = None
        self.discriminator = None
        self.serial_number = serial_number
        self.volume_serial_number = volume_serial_number
        self.created_at = created_at
        self.consistency_id = consistency_id
        if destroyed is not None:
            self.destroyed = destroyed
        if time_remaining is not None:
            self.time_remaining = time_remaining
        self.size = size
        self.tenant = tenant
        self.tenant_space = tenant_space
        self.snapshot = snapshot
        if volume is not None:
            self.volume = volume
        if protection_policy is not None:
            self.protection_policy = protection_policy
        self.placement_group = placement_group
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def serial_number(self):
        """Gets the serial_number of this VolumeSnapshot.  # noqa: E501

        A serial number generated by the system when the volume snapshot is created. The serial number is unique across all arrays.  # noqa: E501

        :return: The serial_number of this VolumeSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this VolumeSnapshot.

        A serial number generated by the system when the volume snapshot is created. The serial number is unique across all arrays.  # noqa: E501

        :param serial_number: The serial_number of this VolumeSnapshot.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def volume_serial_number(self):
        """Gets the volume_serial_number of this VolumeSnapshot.  # noqa: E501

        The serial number of the volume this volume snapshot is created from.  # noqa: E501

        :return: The volume_serial_number of this VolumeSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._volume_serial_number

    @volume_serial_number.setter
    def volume_serial_number(self, volume_serial_number):
        """Sets the volume_serial_number of this VolumeSnapshot.

        The serial number of the volume this volume snapshot is created from.  # noqa: E501

        :param volume_serial_number: The volume_serial_number of this VolumeSnapshot.  # noqa: E501
        :type: str
        """
        if volume_serial_number is None:
            raise ValueError("Invalid value for `volume_serial_number`, must not be `None`")  # noqa: E501

        self._volume_serial_number = volume_serial_number

    @property
    def created_at(self):
        """Gets the created_at of this VolumeSnapshot.  # noqa: E501

        The volume snapshot creation time. Measured in milliseconds since the UNIX epoch.  # noqa: E501

        :return: The created_at of this VolumeSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VolumeSnapshot.

        The volume snapshot creation time. Measured in milliseconds since the UNIX epoch.  # noqa: E501

        :param created_at: The created_at of this VolumeSnapshot.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def consistency_id(self):
        """Gets the consistency_id of this VolumeSnapshot.  # noqa: E501

        Volume snapshots with the same consistency_id are crash consistency.  # noqa: E501

        :return: The consistency_id of this VolumeSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._consistency_id

    @consistency_id.setter
    def consistency_id(self, consistency_id):
        """Sets the consistency_id of this VolumeSnapshot.

        Volume snapshots with the same consistency_id are crash consistency.  # noqa: E501

        :param consistency_id: The consistency_id of this VolumeSnapshot.  # noqa: E501
        :type: str
        """
        if consistency_id is None:
            raise ValueError("Invalid value for `consistency_id`, must not be `None`")  # noqa: E501

        self._consistency_id = consistency_id

    @property
    def destroyed(self):
        """Gets the destroyed of this VolumeSnapshot.  # noqa: E501

        True if the volume snapshot has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed volume snapshot is permanently eradicated.  # noqa: E501

        :return: The destroyed of this VolumeSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """Sets the destroyed of this VolumeSnapshot.

        True if the volume snapshot has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed volume snapshot is permanently eradicated.  # noqa: E501

        :param destroyed: The destroyed of this VolumeSnapshot.  # noqa: E501
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def time_remaining(self):
        """Gets the time_remaining of this VolumeSnapshot.  # noqa: E501

        The amount of time left until the destroyed volume snapshot is permanently eradicated. Measured in milliseconds.  # noqa: E501

        :return: The time_remaining of this VolumeSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this VolumeSnapshot.

        The amount of time left until the destroyed volume snapshot is permanently eradicated. Measured in milliseconds.  # noqa: E501

        :param time_remaining: The time_remaining of this VolumeSnapshot.  # noqa: E501
        :type: int
        """

        self._time_remaining = time_remaining

    @property
    def size(self):
        """Gets the size of this VolumeSnapshot.  # noqa: E501

        The virtual size of the volume snapshot. Measured in bytes.  # noqa: E501

        :return: The size of this VolumeSnapshot.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeSnapshot.

        The virtual size of the volume snapshot. Measured in bytes.  # noqa: E501

        :param size: The size of this VolumeSnapshot.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def tenant(self):
        """Gets the tenant of this VolumeSnapshot.  # noqa: E501


        :return: The tenant of this VolumeSnapshot.  # noqa: E501
        :rtype: TenantRef
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VolumeSnapshot.


        :param tenant: The tenant of this VolumeSnapshot.  # noqa: E501
        :type: TenantRef
        """
        if tenant is None:
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def tenant_space(self):
        """Gets the tenant_space of this VolumeSnapshot.  # noqa: E501


        :return: The tenant_space of this VolumeSnapshot.  # noqa: E501
        :rtype: TenantSpaceRef
        """
        return self._tenant_space

    @tenant_space.setter
    def tenant_space(self, tenant_space):
        """Sets the tenant_space of this VolumeSnapshot.


        :param tenant_space: The tenant_space of this VolumeSnapshot.  # noqa: E501
        :type: TenantSpaceRef
        """
        if tenant_space is None:
            raise ValueError("Invalid value for `tenant_space`, must not be `None`")  # noqa: E501

        self._tenant_space = tenant_space

    @property
    def snapshot(self):
        """Gets the snapshot of this VolumeSnapshot.  # noqa: E501


        :return: The snapshot of this VolumeSnapshot.  # noqa: E501
        :rtype: SnapshotRef
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this VolumeSnapshot.


        :param snapshot: The snapshot of this VolumeSnapshot.  # noqa: E501
        :type: SnapshotRef
        """
        if snapshot is None:
            raise ValueError("Invalid value for `snapshot`, must not be `None`")  # noqa: E501

        self._snapshot = snapshot

    @property
    def volume(self):
        """Gets the volume of this VolumeSnapshot.  # noqa: E501


        :return: The volume of this VolumeSnapshot.  # noqa: E501
        :rtype: VolumeRef
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this VolumeSnapshot.


        :param volume: The volume of this VolumeSnapshot.  # noqa: E501
        :type: VolumeRef
        """

        self._volume = volume

    @property
    def protection_policy(self):
        """Gets the protection_policy of this VolumeSnapshot.  # noqa: E501


        :return: The protection_policy of this VolumeSnapshot.  # noqa: E501
        :rtype: ProtectionPolicyRef
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this VolumeSnapshot.


        :param protection_policy: The protection_policy of this VolumeSnapshot.  # noqa: E501
        :type: ProtectionPolicyRef
        """

        self._protection_policy = protection_policy

    @property
    def placement_group(self):
        """Gets the placement_group of this VolumeSnapshot.  # noqa: E501


        :return: The placement_group of this VolumeSnapshot.  # noqa: E501
        :rtype: PlacementGroupRef
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this VolumeSnapshot.


        :param placement_group: The placement_group of this VolumeSnapshot.  # noqa: E501
        :type: PlacementGroupRef
        """
        if placement_group is None:
            raise ValueError("Invalid value for `placement_group`, must not be `None`")  # noqa: E501

        self._placement_group = placement_group

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
        if issubclass(VolumeSnapshot, dict):
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
        if not isinstance(other, VolumeSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
