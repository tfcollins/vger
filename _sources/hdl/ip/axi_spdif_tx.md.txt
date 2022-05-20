# axi_spdif_tx

<center>

![axi_spdif_tx](axi_spdif_tx-axi_spdif_tx.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| S_AXI_DATA_WIDTH | 32 | NA |
| S_AXI_ADDRESS_WIDTH | 32 | NA |
| DEVICE_FAMILY | virtex6 | NA |
| DMA_TYPE | 0 | NA |
| Component_Name | axi_spdif_tx_v1_0 | NA |


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



### s_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TDATA | s_axis_tdata | axis |
| TLAST | s_axis_tlast | axis |
| TVALID | s_axis_tvalid | axis |
| TREADY | s_axis_tready | axis |



### dma_req_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_aclk | clock |



### s_axis_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | s_axis_aclk | clock |



### spdif_data_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | spdif_data_clk | clock |



### dma_req_rstn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_rstn | reset |



### s_axis_aresetn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | s_axis_aresetn | reset |



### dma_ack
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_davalid | axis |
| TREADY | dma_req_daready | axis |
| TUSER | dma_req_datype | axis |



### dma_req
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_drvalid | axis |
| TREADY | dma_req_drready | axis |
| TUSER | dma_req_drtype | axis |
| TLAST | dma_req_drlast | axis |



### dma_req_dma_ack_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_aclk | clock |



### dma_req_dma_ack_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_rstn | reset |




## Registers