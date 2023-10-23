# SecurityCodeControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_type** | **str** |  | [optional] 
**mask_type** | **str** |  | [optional] 
**placeholder_type** | **str** |  | [optional] 
**validation_type** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.security_code_control import SecurityCodeControl

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityCodeControl from a JSON string
security_code_control_instance = SecurityCodeControl.from_json(json)
# print the JSON string representation of the object
print SecurityCodeControl.to_json()

# convert the object into a dict
security_code_control_dict = security_code_control_instance.to_dict()
# create an instance of SecurityCodeControl from a dict
security_code_control_form_dict = security_code_control.from_dict(security_code_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


