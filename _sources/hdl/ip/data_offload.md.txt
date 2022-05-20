# data_offload

<center>

![data_offload](data_offload-data_offload.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| MEM_TYPE | "0" | NA |
| MEM_SIZE_LOG2 | 10 | NA |
| TX_OR_RXN_PATH | 0 | NA |
| SRC_DATA_WIDTH | 64 | NA |
| DST_DATA_WIDTH | 128 | NA |
| DST_CYCLIC_EN | true | NA |
| AUTO_BRINGUP | 1 | NA |
| SYNC_EXT_ADD_INTERNAL_CDC | true | NA |
| HAS_BYPASS | true | NA |
| Component_Name | data_offload_v1_0 | NA |


## Buses


### s_axi
| Logical | Physical | Type |
| ------- | -------- | ---- |
| AWADDR | s_axi_awaddr | aximm |
| AWPROT | s_axi_awprot | aximm |
| AWVALID | s_axi_awvalid | aximm |
| AWREADY | s_axi_awready | aximm |
| WDATA | s_axi_wdata | aximm |
| WSTRB | s_axi_wstrb | aximm |
| WVALID | s_axi_wvalid | aximm |
| WREADY | s_axi_wready | aximm |
| BRESP | s_axi_bresp | aximm |
| BVALID | s_axi_bvalid | aximm |
| BREADY | s_axi_bready | aximm |
| ARADDR | s_axi_araddr | aximm |
| ARPROT | s_axi_arprot | aximm |
| ARVALID | s_axi_arvalid | aximm |
| ARREADY | s_axi_arready | aximm |
| RDATA | s_axi_rdata | aximm |
| RRESP | s_axi_rresp | aximm |
| RVALID | s_axi_rvalid | aximm |
| RREADY | s_axi_rready | aximm |



### s_axi_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | s_axi_aclk | clock |



### s_axi_aresetn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | s_axi_aresetn | reset |



### m_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TREADY | m_axis_ready | axis |
| TVALID | m_axis_valid | axis |
| TDATA | m_axis_data | axis |
| TLAST | m_axis_last | axis |
| TKEEP | m_axis_tkeep | axis |



### s_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TREADY | s_axis_ready | axis |
| TVALID | s_axis_valid | axis |
| TDATA | s_axis_data | axis |
| TLAST | s_axis_last | axis |
| TKEEP | s_axis_tkeep | axis |



### wr_ctrl
| Logical | Physical | Type |
| ------- | -------- | ---- |
| request_enable | wr_request_enable | if_do_ctrl |
| request_valid | wr_request_valid | if_do_ctrl |
| request_ready | wr_request_ready | if_do_ctrl |
| request_length | wr_request_length | if_do_ctrl |
| response_measured_length | wr_response_measured_length | if_do_ctrl |
| response_eot | wr_response_eot | if_do_ctrl |
| status_overflow | wr_overflow | if_do_ctrl |



### rd_ctrl
| Logical | Physical | Type |
| ------- | -------- | ---- |
| request_enable | rd_request_enable | if_do_ctrl |
| request_valid | rd_request_valid | if_do_ctrl |
| request_ready | rd_request_ready | if_do_ctrl |
| request_length | rd_request_length | if_do_ctrl |
| response_eot | rd_response_eot | if_do_ctrl |
| status_underflow | rd_underflow | if_do_ctrl |



### s_storage_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TREADY | s_storage_axis_ready | axis |
| TVALID | s_storage_axis_valid | axis |
| TDATA | s_storage_axis_data | axis |
| TKEEP | s_storage_axis_tkeep | axis |
| TLAST | s_storage_axis_last | axis |



### m_storage_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TREADY | m_storage_axis_ready | axis |
| TVALID | m_storage_axis_valid | axis |
| TDATA | m_storage_axis_data | axis |
| TKEEP | m_storage_axis_tkeep | axis |
| TLAST | m_storage_axis_last | axis |



### s_storage_axis_m_axis_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | m_axis_aclk | clock |



### s_storage_axis_m_axis_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | m_axis_aresetn | reset |



### m_storage_axis_s_axis_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | s_axis_aclk | clock |



### m_storage_axis_s_axis_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | s_axis_aresetn | reset |




## Registers