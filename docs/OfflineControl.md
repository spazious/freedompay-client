# OfflineControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtk** | **str** |  | [optional] 
**retry_count** | **str** |  | [optional] 
**internal_ffw** | **str** |  | [optional] 
**saf_request_id** | **str** |  | [optional] 
**saf_system_id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.offline_control import OfflineControl

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineControl from a JSON string
offline_control_instance = OfflineControl.from_json(json)
# print the JSON string representation of the object
print OfflineControl.to_json()

# convert the object into a dict
offline_control_dict = offline_control_instance.to_dict()
# create an instance of OfflineControl from a dict
offline_control_form_dict = offline_control.from_dict(offline_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


