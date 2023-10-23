# OrderDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_total** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**order_number** | **str** |  | [optional] 
**order_description** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.order_details import OrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetails from a JSON string
order_details_instance = OrderDetails.from_json(json)
# print the JSON string representation of the object
print OrderDetails.to_json()

# convert the object into a dict
order_details_dict = order_details_instance.to_dict()
# create an instance of OrderDetails from a dict
order_details_form_dict = order_details.from_dict(order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


