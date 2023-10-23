# ClientMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** |  | [optional] 
**application_version** | **str** |  | [optional] 
**workstation_id** | **str** |  | [optional] 
**application_user** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**library** | **str** |  | [optional] 
**library_version** | **str** |  | [optional] 
**security_library** | **str** |  | [optional] 
**security_library_version** | **str** |  | [optional] 
**test_run** | **str** |  | [optional] 
**test_case** | **str** |  | [optional] 
**poi_device_identifier** | **str** |  | [optional] 
**selling_system_name** | **str** |  | [optional] 
**selling_system_version** | **str** |  | [optional] 
**selling_middleware_name** | **str** |  | [optional] 
**selling_middleware_version** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.client_metadata import ClientMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClientMetadata from a JSON string
client_metadata_instance = ClientMetadata.from_json(json)
# print the JSON string representation of the object
print ClientMetadata.to_json()

# convert the object into a dict
client_metadata_dict = client_metadata_instance.to_dict()
# create an instance of ClientMetadata from a dict
client_metadata_form_dict = client_metadata.from_dict(client_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


