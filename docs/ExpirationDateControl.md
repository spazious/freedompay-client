# ExpirationDateControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_type** | **str** |  | [optional] 
**placeholder_type** | **str** |  | [optional] 
**validation_type** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.expiration_date_control import ExpirationDateControl

# TODO update the JSON string below
json = "{}"
# create an instance of ExpirationDateControl from a JSON string
expiration_date_control_instance = ExpirationDateControl.from_json(json)
# print the JSON string representation of the object
print ExpirationDateControl.to_json()

# convert the object into a dict
expiration_date_control_dict = expiration_date_control_instance.to_dict()
# create an instance of ExpirationDateControl from a dict
expiration_date_control_form_dict = expiration_date_control.from_dict(expiration_date_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


