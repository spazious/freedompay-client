# RestaurantData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**food_subtotal** | **str** |  | [optional] 
**beverage_subtotal** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.restaurant_data import RestaurantData

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantData from a JSON string
restaurant_data_instance = RestaurantData.from_json(json)
# print the JSON string representation of the object
print RestaurantData.to_json()

# convert the object into a dict
restaurant_data_dict = restaurant_data_instance.to_dict()
# create an instance of RestaurantData from a dict
restaurant_data_form_dict = restaurant_data.from_dict(restaurant_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


