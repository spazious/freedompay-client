# VendProductList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**List[VendProduct]**](VendProduct.md) |  | [optional] 
**options** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.vend_product_list import VendProductList

# TODO update the JSON string below
json = "{}"
# create an instance of VendProductList from a JSON string
vend_product_list_instance = VendProductList.from_json(json)
# print the JSON string representation of the object
print VendProductList.to_json()

# convert the object into a dict
vend_product_list_dict = vend_product_list_instance.to_dict()
# create an instance of VendProductList from a dict
vend_product_list_form_dict = vend_product_list.from_dict(vend_product_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


