# LegalControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hide_checkbox** | **bool** |  | [optional] 
**text_type** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.legal_control import LegalControl

# TODO update the JSON string below
json = "{}"
# create an instance of LegalControl from a JSON string
legal_control_instance = LegalControl.from_json(json)
# print the JSON string representation of the object
print LegalControl.to_json()

# convert the object into a dict
legal_control_dict = legal_control_instance.to_dict()
# create an instance of LegalControl from a dict
legal_control_form_dict = legal_control.from_dict(legal_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


