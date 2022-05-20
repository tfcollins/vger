# axi_i2s_adi

<center>

![axi_i2s_adi](axi_i2s_adi-axi_i2s_adi.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| SLOT_WIDTH | 24 | NA |
| LRCLK_POL | 0 | NA |
| BCLK_POL | 0 | NA |
| S_AXI_DATA_WIDTH | 32 | NA |
| S_AXI_ADDRESS_WIDTH | 32 | NA |
| DEVICE_FAMILY | virtex6 | NA |
| DMA_TYPE | 0 | NA |
| NUM_OF_CHANNEL | 1 | NA |
| HAS_TX | 1 | NA |
| HAS_RX | 1 | NA |
| Component_Name | axi_i2s_adi_v1_0 | NA |


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
| TDATA | m_axis_tdata | axis |
| TKEEP | m_axis_tkeep | axis |
| TLAST | m_axis_tlast | axis |
| TVALID | m_axis_tvalid | axis |
| TREADY | m_axis_tready | axis |



### s_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TDATA | s_axis_tdata | axis |
| TLAST | s_axis_tlast | axis |
| TVALID | s_axis_tvalid | axis |
| TREADY | s_axis_tready | axis |



### dma_req_rx_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_rx_aclk | clock |



### dma_req_tx_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_tx_aclk | clock |



### m_axis_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | m_axis_aclk | clock |



### s_axis_aclk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | s_axis_aclk | clock |



### dma_req_rx_rstn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_rx_rstn | reset |



### dma_req_tx_rstn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_tx_rstn | reset |



### s_axis_aresetn
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | s_axis_aresetn | reset |



### dma_ack_rx
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_rx_davalid | axis |
| TREADY | dma_req_rx_daready | axis |
| TUSER | dma_req_rx_datype | axis |



### dma_req_rx
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_rx_drvalid | axis |
| TREADY | dma_req_rx_drready | axis |
| TUSER | dma_req_rx_drtype | axis |
| TLAST | dma_req_rx_drlast | axis |



### dma_req_rx_dma_ack_rx_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_rx_aclk | clock |



### dma_req_rx_dma_ack_rx_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_rx_rstn | reset |



### dma_ack_tx
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_tx_davalid | axis |
| TREADY | dma_req_tx_daready | axis |
| TUSER | dma_req_tx_datype | axis |



### dma_req_tx
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | dma_req_tx_drvalid | axis |
| TREADY | dma_req_tx_drready | axis |
| TUSER | dma_req_tx_drtype | axis |
| TLAST | dma_req_tx_drlast | axis |



### dma_req_tx_dma_ack_tx_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dma_req_tx_aclk | clock |



### dma_req_tx_dma_ack_tx_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dma_req_tx_rstn | reset |



### i2s
| Logical | Physical | Type |
| ------- | -------- | ---- |
| BCLK | bclk_o | i2s |
| LRCLK | lrclk_o | i2s |
| SDATA_OUT | sdata_o | i2s |
| SDATA_IN | sdata_i | i2s |



### i2s_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | data_clk_i | clock |




## Registers