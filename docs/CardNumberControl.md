# CardNumberControl


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_type** | **str** |  | [optional] 
**mask_type** | **str** |  | [optional] 
**placeholder_type** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.card_number_control import CardNumberControl

# TODO update the JSON string below
json = "{}"
# create an instance of CardNumberControl from a JSON string
card_number_control_instance = CardNumberControl.from_json(json)
# print the JSON string representation of the object
print CardNumberControl.to_json()

# convert the object into a dict
card_number_control_dict = card_number_control_instance.to_dict()
# create an instance of CardNumberControl from a dict
card_number_control_form_dict = card_number_control.from_dict(card_number_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


