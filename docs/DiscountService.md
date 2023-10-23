# DiscountService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_code** | **str** |  | [optional] 
**options** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.discount_service import DiscountService

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountService from a JSON string
discount_service_instance = DiscountService.from_json(json)
# print the JSON string representation of the object
print DiscountService.to_json()

# convert the object into a dict
discount_service_dict = discount_service_instance.to_dict()
# create an instance of DiscountService from a dict
discount_service_form_dict = discount_service.from_dict(discount_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


