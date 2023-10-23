<a name="__pageTop"></a>
# freedompay-client.apis.tags.payments_api.PaymentsApi

All URIs are relative to *https://hpc.uat.freedompay.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_acknowledge**](#payments_acknowledge) | **post** /v1.5/payments/acknowledge | 
[**payments_post_v13**](#payments_post_v13) | **post** /v1.5/payments | 
[**payments_reverse**](#payments_reverse) | **post** /v1.5/payments/reverse | 

# **payments_acknowledge**
<a name="payments_acknowledge"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} payments_acknowledge(request)



### Example

```python
import freedompay-client
from freedompay-client.apis.tags import payments_api
from freedompay-client.model.acknowledge_request import AcknowledgeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Bearer ",
    }
    body = AcknowledgeRequest(
        pos_sync_attempt_num=1,
        pos_sync_id="pos_sync_id_example",
    )
    try:
        api_response = api_instance.payments_acknowledge(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_acknowledge: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcknowledgeRequest**](../../models/AcknowledgeRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcknowledgeRequest**](../../models/AcknowledgeRequest.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**AcknowledgeRequest**](../../models/AcknowledgeRequest.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**AcknowledgeRequest**](../../models/AcknowledgeRequest.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**AcknowledgeRequest**](../../models/AcknowledgeRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "Bearer "

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payments_acknowledge.ApiResponseFor200) | OK

#### payments_acknowledge.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **payments_post_v13**
<a name="payments_post_v13"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} payments_post_v13()



### Example

```python
import freedompay-client
from freedompay-client.apis.tags import payments_api
from freedompay-client.model.post_request import PostRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Bearer ",
    }
    try:
        api_response = api_instance.payments_post_v13(
            header_params=header_params,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_post_v13: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Bearer ",
    }
    body = dict(
        pos_sync_attempt_num=1,
        pos_sync_id="pos_sync_id_example",
        cc_auth="cc_auth_example",
        payment_key="00000000-0000-0000-0000-000000000000",
        request_message=RequestMessage(
            client_id="client_id_example",
            store_id="store_id_example",
            terminal_id="terminal_id_example",
            es_key="es_key_example",
            admin_service=AdminService(
                service_type="service_type_example",
                term_caps="term_caps_example",
                run="run_example",
            ),
            auto_rental_data=AutoRentalData(
                expected_duration="expected_duration_example",
                agreement_number="agreement_number_example",
                checkout_date="checkout_date_example",
                checkin_date="checkin_date_example",
                rental_rate="rental_rate_example",
                rental_rate_unit="rental_rate_unit_example",
                rental_class_id="rental_class_id_example",
                no_show="no_show_example",
                renter_name="renter_name_example",
                return_location_id="return_location_id_example",
                return_city="return_city_example",
                return_state="return_state_example",
                return_country="return_country_example",
                extra_charge_types="extra_charge_types_example",
                extra_charge_total="extra_charge_total_example",
                extra_charge_notified="extra_charge_notified_example",
            ),
            healthcare_data=HealthcareDataWeb(
                total_amount="total_amount_example",
                rx="rx_example",
                vision="vision_example",
                clinic="clinic_example",
                dental="dental_example",
            ),
            bill_to=BillTo(
                ip_address="ip_address_example",
                customer_id="customer_id_example",
                date_of_birth="date_of_birth_example",
                drivers_license_number="drivers_license_number_example",
                drivers_license_state="drivers_license_state_example",
                company="company_example",
                title="title_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                suffix="suffix_example",
                street1="street1_example",
                street2="street2_example",
                street3="street3_example",
                street4="street4_example",
                city="city_example",
                state="state_example",
                postal_code="postal_code_example",
                country="country_example",
                phone_number="phone_number_example",
                fax_number="fax_number_example",
                email="email_example",
                ssn="ssn_example",
            ),
            card=Card(
                account_number="account_number_example",
                account_type="account_type_example",
                card_type="card_type_example",
                token_subtype="token_subtype_example",
                subtype="subtype_example",
                issuer="issuer_example",
                cv_indicator="cv_indicator_example",
                cv_number="cv_number_example",
                expiration_month="expiration_month_example",
                expiration_year="expiration_year_example",
                issue_number="issue_number_example",
                name_on_card="name_on_card_example",
                start_month="start_month_example",
                start_year="start_year_example",
                service_restriction_code="service_restriction_code_example",
                pin_ksn="pin_ksn_example",
                pin_block="pin_block_example",
                voucher_number="voucher_number_example",
                expected_brand="expected_brand_example",
                pl_data1="pl_data1_example",
                pl_data2="pl_data2_example",
                _pass="_pass_example",
            ),
            cc_auth_service=CCAuthService(
                trans_type="trans_type_example",
                cof_indicator="cof_indicator_example",
                cof_compliance_data="cof_compliance_data_example",
                allow_partial="allow_partial_example",
                return_balance="return_balance_example",
                auth_type="auth_type_example",
                verbal_auth_code="verbal_auth_code_example",
                ecom3ds="ecom3ds_example",
                cavv="cavv_example",
                xid="xid_example",
                orig_auth_amount="orig_auth_amount_example",
                enable_avs="enable_avs_example",
                offline="offline_example",
                offline_code="offline_code_example",
                estimated="estimated_example",
                installment_number="installment_number_example",
                installment_count="installment_count_example",
                auth3dsformat="auth3dsformat_example",
                auth3dsjson="auth3dsjson_example",
                sca_exemptions="sca_exemptions_example",
                sca_upgrade="sca_upgrade_example",
                request_par="request_par_example",
                bill_payment="bill_payment_example",
                recurring="recurring_example",
                commerce_indicator="commerce_indicator_example",
                partial_payment_id="partial_payment_id_example",
                last_payment_flag="last_payment_flag_example",
                industry_datatype="industry_datatype_example",
                run="run_example",
            ),
            cc_capture_service=CCCaptureService(
                purchasing_level="purchasing_level_example",
                is_split_transaction="is_split_transaction_example",
                use_merchant_creds="use_merchant_creds_example",
                business_date="business_date_example",
                partial_payment_id="partial_payment_id_example",
                last_payment_flag="last_payment_flag_example",
                industry_datatype="industry_datatype_example",
                run="run_example",
            ),
            cc_credit_service=CCCreditService(
                trans_type="trans_type_example",
                offline="offline_example",
                offline_code="offline_code_example",
                return_balance="return_balance_example",
                business_date="business_date_example",
                bill_payment="bill_payment_example",
                recurring="recurring_example",
                commerce_indicator="commerce_indicator_example",
                partial_payment_id="partial_payment_id_example",
                last_payment_flag="last_payment_flag_example",
                industry_datatype="industry_datatype_example",
                run="run_example",
            ),
            cc_followup_service=CCFollowupService(
                run="run_example",
            ),
            dcc_service=DccService(
                bin="bin_example",
                amount="amount_example",
                run="run_example",
            ),
            dcc=DccInfo(
                enabled="enabled_example",
                exchange_rate="exchange_rate_example",
                foreign_amount="foreign_amount_example",
                foreign_currency="foreign_currency_example",
                host_data="host_data_example",
            ),
            check=Check(
                bank_transit_number="bank_transit_number_example",
                account_number="account_number_example",
                account_type="account_type_example",
                check_number="check_number_example",
                ach_accepted="ach_accepted_example",
                check_type="check_type_example",
                full_micr="full_micr_example",
                reader_status="reader_status_example",
            ),
            clerk_id="clerk_id_example",
            client_metadata=ClientMetadata(
                application_name="application_name_example",
                application_version="application_version_example",
                workstation_id="workstation_id_example",
                application_user="application_user_example",
                environment="environment_example",
                library="library_example",
                library_version="library_version_example",
                security_library="security_library_example",
                security_library_version="security_library_version_example",
                test_run="test_run_example",
                test_case="test_case_example",
                poi_device_identifier="poi_device_identifier_example",
                selling_system_name="selling_system_name_example",
                selling_system_version="selling_system_version_example",
                selling_middleware_name="selling_middleware_name_example",
                selling_middleware_version="selling_middleware_version_example",
            ),
            comments="comments_example",
            discount_service=DiscountService(
                scenario_code="scenario_code_example",
                options="options_example",
                run="run_example",
            ),
            efv_options=EfvOptions(
                options="options_example",
                force="force_example",
                force_code="force_code_example",
                force_message="force_message_example",
            ),
            fleet_data=FleetData(
                user_id="user_id_example",
                vehicle_id="vehicle_id_example",
                vehicle_tag="vehicle_tag_example",
                driver_id="driver_id_example",
                odo="odo_example",
                dl_num="dl_num_example",
                dl_state="dl_state_example",
                dl_name="dl_name_example",
                po_number="po_number_example",
                invoice_num="invoice_num_example",
                trip_num="trip_num_example",
                unit_num="unit_num_example",
                trailer_hours="trailer_hours_example",
                dob="dob_example",
                zip="zip_example",
                misc1="misc1_example",
                misc2="misc2_example",
                cash_back="cash_back_example",
                job_num="job_num_example",
                maint_id="maint_id_example",
                dept="dept_example",
                vin="vin_example",
                tractor_num="tractor_num_example",
                hubo="hubo_example",
                trailer_num="trailer_num_example",
                custom1="custom1_example",
                custom2="custom2_example",
            ),
            fraud_check_service=FraudCheckService(
                reference_id="reference_id_example",
                option="option_example",
                mode="mode_example",
                device_identifier="device_identifier_example",
                commerce_indicator="commerce_indicator_example",
                site_identifier="site_identifier_example",
                customer_since_date="customer_since_date_example",
                estimated_total_amount="estimated_total_amount_example",
                properties=[
                    UserDefinedField(
                        name="name_example",
                        value="value_example",
                    )
                ],
                run_risk_model="run_risk_model_example",
                order="order_example",
                void_threshold="void_threshold_example",
                auth_data="auth_data_example",
                captcha_data="captcha_data_example",
                fail_count="fail_count_example",
                failed_requests=[
                    "failed_requests_example"
                ],
                run="run_example",
            ),
            inquiry_service=InquiryService(
                verify_mode="verify_mode_example",
                fields="fields_example",
                authorized_user="authorized_user_example",
                run="run_example",
            ),
            hotel_data=HotelData(
                room_occupant_count="room_occupant_count_example",
                room_type="room_type_example",
                notes="notes_example",
,
                expected_duration="expected_duration_example",
                folio_number="folio_number_example",
                no_show="no_show_example",
                program_code="program_code_example",
                checkin_date="checkin_date_example",
                checkout_date="checkout_date_example",
                extra_charge_types="extra_charge_types_example",
                room_rate="room_rate_example",
                room_rate_unit="room_rate_unit_example",
                room_tax="room_tax_example",
                extra_charge_total="extra_charge_total_example",
                renter_name="renter_name_example",
            ),
            invoice_discount_detail=[
                EIDDetail(
                    discount_key="discount_key_example",
                    code="code_example",
                    qty="qty_example",
                    offset="offset_example",
                    total_amount="total_amount_example",
                )
            ],
            invoice_service=InvoiceService(
                trans_type="trans_type_example",
                run="run_example",
            ),
            invoice_header=InvoiceHeader(
                invoice_number="invoice_number_example",
                invoice_date="invoice_date_example",
                merchant_descriptor="merchant_descriptor_example",
                merchant_descriptor_contact="merchant_descriptor_contact_example",
                merchant_descriptor_url="merchant_descriptor_url_example",
                purchaser_code="purchaser_code_example",
                purchaser_order_date="purchaser_order_date_example",
                goods_indicator="goods_indicator_example",
                customer_po="customer_po_example",
                product_code_standard="product_code_standard_example",
                eid_indicator="eid_indicator_example",
            ),
            items=[
                Item(
                    discount_amount="discount_amount_example",
                    discount_flag="discount_flag_example",
                    tax_included_flag="tax_included_flag_example",
                    product_code="product_code_example",
                    product_upc="product_upc_example",
                    product_sku="product_sku_example",
                    product_name="product_name_example",
                    product_description="product_description_example",
                    product_make="product_make_example",
                    product_model="product_model_example",
                    product_part_number="product_part_number_example",
                    commodity_code="commodity_code_example",
                    product_year="product_year_example",
                    product_serial1="product_serial1_example",
                    product_serial2="product_serial2_example",
                    product_serial3="product_serial3_example",
                    customer_asset_id="customer_asset_id_example",
                    category="category_example",
                    sub_category="sub_category_example",
                    unit_price="unit_price_example",
                    quantity="quantity_example",
                    total_amount="total_amount_example",
                    tax_amount="tax_amount_example",
                    promo_code="promo_code_example",
                    freight_amount="freight_amount_example",
                    unit_of_measure="unit_of_measure_example",
                    sale_code="sale_code_example",
                    custom_format_id="custom_format_id_example",
                    custom1="custom1_example",
                    custom2="custom2_example",
                    custom3="custom3_example",
                    custom4="custom4_example",
                    custom5="custom5_example",
                    custom6="custom6_example",
                    custom7="custom7_example",
                    custom8="custom8_example",
                    custom9="custom9_example",
                    pay_alloc="pay_alloc_example",
                    alloc_code="alloc_code_example",
                    eid_indicator="eid_indicator_example",
                    orig_unit_price="orig_unit_price_example",
                    orig_total_amount="orig_total_amount_example",
,
                    tax_detail=[
                        TaxDetailItem(
                            type="type_example",
                            amount="amount_example",
                        )
                    ],
                    id="id_example",
                    tag="tag_example",
                )
            ],
            payments=[
                Payment(
                    trans_type="trans_type_example",
                    pos_tender_type=TenderType(
                        description="description_example",
                        id="id_example",
                    ),
                    brand="brand_example",
                    card_type="card_type_example",
                    entry_mode="entry_mode_example",
                    amount="amount_example",
                    currency_code="currency_code_example",
                    offline="offline_example",
                    request_id="request_id_example",
                )
            ],
            language="language_example",
            loyalty_service=LoyaltyService(
                card_type="card_type_example",
                card_number="card_number_example",
                app_id="app_id_example",
                id_block="id_block_example",
                id_ksn="id_ksn_example",
                run="run_example",
            ),
            request_incentives=RequestIncentives(
                system_id="system_id_example",
                incentives=[
                    IncentiveIncentive(
                        id="id_example",
                        presented="presented_example",
                        accepted="accepted_example",
                        tender_request_id="tender_request_id_example",
                    )
                ],
            ),
            merchant_defined_data=MerchantDefinedData(
                format_id="format_id_example",
                field1="field1_example",
                field2="field2_example",
                field3="field3_example",
                field4="field4_example",
                field5="field5_example",
                field6="field6_example",
                field7="field7_example",
                field8="field8_example",
                field9="field9_example",
                field10="field10_example",
                field11="field11_example",
                field12="field12_example",
                field13="field13_example",
                field14="field14_example",
                field15="field15_example",
                field16="field16_example",
                field17="field17_example",
                field18="field18_example",
                field19="field19_example",
                field20="field20_example",
            ),
            magic_cookie="magic_cookie_example",
            merchant_reference_code="merchant_reference_code_example",
            merchant_batch_id="merchant_batch_id_example",
            message_service=MessageService(),
            mobile_service=MobileService(
                feature_flags1="feature_flags1_example",
                feature_flags2="feature_flags2_example",
                function_code="function_code_example",
                check_id="check_id_example",
                accept_tip="accept_tip_example",
                open_tab="open_tab_example",
                payment_session_id="payment_session_id_example",
                mha_callback_key="mha_callback_key_example",
                qrseq="qrseq_example",
                bar_data="bar_data_example",
                bar_type="bar_type_example",
                confirm_pay_seq="confirm_pay_seq_example",
                pay_seq="pay_seq_example",
                applied_discount_amount="applied_discount_amount_example",
                run="run_example",
            ),
            network_data=NetworkData(
                network="network_example",
                stan="stan_example",
                aci="aci_example",
                tdcc="tdcc_example",
                pcode="pcode_example",
                vcode="vcode_example",
                downgrade_code="downgrade_code_example",
                cvc_error="cvc_error_example",
                data_error="data_error_example",
                auth_source="auth_source_example",
                response_code="response_code_example",
                product_id="product_id_example",
                program_id="program_id_example",
                merchant_advice="merchant_advice_example",
                service_option="service_option_example",
                fleet_prompts="fleet_prompts_example",
                custom_data=[
                    NetworkCustomData(
,
                        code="code_example",
                    )
                ],
                mac="mac_example",
                pos_seq_num="pos_seq_num_example",
                mac_key="mac_key_example",
                pin_key="pin_key_example",
                field_key="field_key_example",
                trans_date="trans_date_example",
                trans_time="trans_time_example",
                host_control_data="host_control_data_example",
            ),
            offline_control=OfflineControl(
                dtk="dtk_example",
                retry_count="retry_count_example",
                internal_ffw="internal_ffw_example",
                saf_request_id="saf_request_id_example",
                saf_system_id="saf_system_id_example",
            ),
            order_request_id="order_request_id_example",
            order_request_token="order_request_token_example",
            pos=Pos(
                register_number="register_number_example",
                entry_mode="entry_mode_example",
                track1="track1_example",
                track2="track2_example",
                track3="track3_example",
                track_ksn="track_ksn_example",
                sequence_number="sequence_number_example",
                card_present="card_present_example",
                track1e="track1e_example",
                track2e="track2e_example",
                track1len="track1len_example",
                track2len="track2len_example",
                tracke="tracke_example",
                enc_mode="enc_mode_example",
                msr_type="msr_type_example",
                payment_date="payment_date_example",
                chip_data="chip_data_example",
                issuer_script_results="issuer_script_results_example",
                caps="caps_example",
                fallback_reason="fallback_reason_example",
                sig_data="sig_data_example",
            ),
            promo_service=PromoService(
                options="options_example",
                action="action_example",
                scenario_code="scenario_code_example",
                program_code="program_code_example",
                quick_promo="quick_promo_example",
                force_code="force_code_example",
                force_message="force_message_example",
                validation_code="validation_code_example",
                run="run_example",
            ),
            purchase_totals=PurchaseTotals(
,
                currency="currency_example",
                discount_total="discount_total_example",
                duty_total="duty_total_example",
                freight_total="freight_total_example",
                tax_total="tax_total_example",
                tip_amount="tip_amount_example",
                debit_surcharge="debit_surcharge_example",
                cash_back_amount="cash_back_amount_example",
                overtender="overtender_example",
                invoice_total="invoice_total_example",
                service_charge="service_charge_example",
                eid_amount="eid_amount_example",
                charge_amount="charge_amount_example",
            ),
            restaurant_data=RestaurantData(
                food_subtotal="food_subtotal_example",
                beverage_subtotal="beverage_subtotal_example",
            ),
            response_flags="response_flags_example",
            session_key="session_key_example",
            session_service=SessionService(),
            ship_from=ShipFrom(
                company="company_example",
                title="title_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                suffix="suffix_example",
                street1="street1_example",
                street2="street2_example",
                street3="street3_example",
                street4="street4_example",
                city="city_example",
                state="state_example",
                postal_code="postal_code_example",
                country="country_example",
                phone_number="phone_number_example",
                fax_number="fax_number_example",
                email="email_example",
                ssn="ssn_example",
            ),
            ship_to=ShipTo(
                company="company_example",
                title="title_example",
                first_name="first_name_example",
                middle_name="middle_name_example",
                last_name="last_name_example",
                suffix="suffix_example",
                street1="street1_example",
                street2="street2_example",
                street3="street3_example",
                street4="street4_example",
                city="city_example",
                state="state_example",
                postal_code="postal_code_example",
                country="country_example",
                phone_number="phone_number_example",
                fax_number="fax_number_example",
                email="email_example",
                ssn="ssn_example",
                date_of_birth="date_of_birth_example",
                shipping_company="shipping_company_example",
                shipping_method="shipping_method_example",
                tracking_number="tracking_number_example",
            ),
            token_create_service=TokenCreateService(
                type="type_example",
                disable_verification="disable_verification_example",
                pos_data="pos_data_example",
                dyn_exp="dyn_exp_example",
                run="run_example",
            ),
            vend_control_service=VendControlService(
                products=VendProductList(
                    product=[
                        VendProduct(
                            id="id_example",
                            tag="tag_example",
                            product_code="product_code_example",
                            unit_of_measure="unit_of_measure_example",
                            unit_price="unit_price_example",
                            max_qty="max_qty_example",
                            options="options_example",
                            price_code="price_code_example",
                        )
                    ],
                    options="options_example",
                ),
            ),
            void_service=VoidService(
                reason="reason_example",
                offline="offline_example",
                offline_code="offline_code_example",
                run="run_example",
            ),
            tor_service=TORService(),
            eod_service=EodService(
                level="level_example",
                group_code="group_code_example",
                run="run_example",
            ),
            incentive_service=IncentiveService(
                system_id="system_id_example",
                consumer_identifier_type="consumer_identifier_type_example",
                consumer_identifier="consumer_identifier_example",
                additional_data="additional_data_example",
                additional_data_type="additional_data_type_example",
,
                trans_type="trans_type_example",
                run="run_example",
            ),
            member_data=MemberData(
                enrollment_date="enrollment_date_example",
                is_new_member="is_new_member_example",
                member_identification="member_identification_example",
                member_identification_type="member_identification_type_example",
                id="id_example",
                street1="street1_example",
                street2="street2_example",
                city="city_example",
                state="state_example",
                country="country_example",
                postal_code="postal_code_example",
                phone_number="phone_number_example",
                level="level_example",
                status="status_example",
                additional_data="additional_data_example",
                additional_data_type="additional_data_type_example",
,
            ),
        ),
        token_information=TokenInformation(
            token="token_example",
            expiration_month="expiration_month_example",
            expiration_year="expiration_year_example",
        ),
    )
    try:
        api_response = api_instance.payments_post_v13(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_post_v13: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PostRequest**](../../models/PostRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "Bearer "

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payments_post_v13.ApiResponseFor200) | OK

#### payments_post_v13.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **payments_reverse**
<a name="payments_reverse"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} payments_reverse(request)



### Example

```python
import freedompay-client
from freedompay-client.apis.tags import payments_api
from freedompay-client.model.reversal_request import ReversalRequest
from pprint import pprint
# Defining the host is optional and defaults to https://hpc.uat.freedompay.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = freedompay-client.Configuration(
    host = "https://hpc.uat.freedompay.com/api"
)

# Enter a context with an instance of the API client
with freedompay-client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Bearer ",
    }
    body = ReversalRequest(
        pos_sync_attempt_num=1,
        pos_sync_id="pos_sync_id_example",
    )
    try:
        api_response = api_instance.payments_reverse(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except freedompay-client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_reverse: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReversalRequest**](../../models/ReversalRequest.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ReversalRequest**](../../models/ReversalRequest.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ReversalRequest**](../../models/ReversalRequest.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ReversalRequest**](../../models/ReversalRequest.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ReversalRequest**](../../models/ReversalRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "Bearer "

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payments_reverse.ApiResponseFor200) | OK

#### payments_reverse.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

