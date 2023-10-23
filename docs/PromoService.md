# PromoService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**scenario_code** | **str** |  | [optional] 
**program_code** | **str** |  | [optional] 
**quick_promo** | **str** |  | [optional] 
**force_code** | **str** |  | [optional] 
**force_message** | **str** |  | [optional] 
**validation_code** | **str** |  | [optional] 
**run** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.promo_service import PromoService

# TODO update the JSON string below
json = "{}"
# create an instance of PromoService from a JSON string
promo_service_instance = PromoService.from_json(json)
# print the JSON string representation of the object
print PromoService.to_json()

# convert the object into a dict
promo_service_dict = promo_service_instance.to_dict()
# create an instance of PromoService from a dict
promo_service_form_dict = promo_service.from_dict(promo_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


