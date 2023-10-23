# PostalCodeControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_type** | **str** |  | [optional] 
**placeholder_type** | **str** |  | [optional] 
**validation_type** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.postal_code_control import PostalCodeControl

# TODO update the JSON string below
json = "{}"
# create an instance of PostalCodeControl from a JSON string
postal_code_control_instance = PostalCodeControl.from_json(json)
# print the JSON string representation of the object
print PostalCodeControl.to_json()

# convert the object into a dict
postal_code_control_dict = postal_code_control_instance.to_dict()
# create an instance of PostalCodeControl from a dict
postal_code_control_form_dict = postal_code_control.from_dict(postal_code_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


