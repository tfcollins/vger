# axi_hdmi_tx

<center>

![axi_hdmi_tx](axi_hdmi_tx-axi_hdmi_tx.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| CR_CB_N | 0 | NA |
| FPGA_TECHNOLOGY | 0 | NA |
| INTERFACE | 16_BIT | NA |
| OUT_CLK_POLARITY | 0 | NA |
| Component_Name | axi_hdmi_tx_v1_0 | NA |


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
| TREADY | vdma_ready | axis |
| TVALID | vdma_valid | axis |
| TDATA | vdma_data | axis |
| TLAST | vdma_end_of_frame | axis |



### reference_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | reference_clk | clock |



### hdmi_out_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | hdmi_out_clk | clock |



### vga_out_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | vga_out_clk | clock |



### vdma_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | vdma_clk | clock |




## Registers