# VolumeSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** | A serial number generated by the system when the volume snapshot is created. The serial number is unique across all arrays. | 
**volume_serial_number** | **str** | The serial number of the volume this volume snapshot is created from. | 
**created_at** | **int** | The volume snapshot creation time. Measured in milliseconds since the UNIX epoch. | 
**consistency_id** | **str** | Volume snapshots with the same consistency_id are crash consistency. | 
**destroyed** | **bool** | True if the volume snapshot has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed volume snapshot is permanently eradicated. | [optional] 
**time_remaining** | **int** | The amount of time left until the destroyed volume snapshot is permanently eradicated. Measured in milliseconds. | [optional] 
**size** | **int** | The virtual size of the volume snapshot. Measured in bytes. | 
**tenant** | [**TenantRef**](TenantRef.md) |  | 
**tenant_space** | [**TenantSpaceRef**](TenantSpaceRef.md) |  | 
**snapshot** | [**SnapshotRef**](SnapshotRef.md) |  | 
**volume** | [**VolumeRef**](VolumeRef.md) |  | [optional] 
**protection_policy** | [**ProtectionPolicyRef**](ProtectionPolicyRef.md) |  | [optional] 
**placement_group** | [**PlacementGroupRef**](PlacementGroupRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

