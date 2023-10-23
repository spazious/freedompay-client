# VendProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**unit_price** | **str** |  | [optional] 
**max_qty** | **str** |  | [optional] 
**options** | **str** |  | [optional] 
**price_code** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.vend_product import VendProduct

# TODO update the JSON string below
json = "{}"
# create an instance of VendProduct from a JSON string
vend_product_instance = VendProduct.from_json(json)
# print the JSON string representation of the object
print VendProduct.to_json()

# convert the object into a dict
vend_product_dict = vend_product_instance.to_dict()
# create an instance of VendProduct from a dict
vend_product_form_dict = vend_product.from_dict(vend_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


