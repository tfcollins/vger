# axi_gpreg

<center>

![axi_gpreg](axi_gpreg-axi_gpreg.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| NUM_OF_IO | 8 | NA |
| NUM_OF_CLK_MONS | 8 | NA |
| BUF_ENABLE_0 | 1 | NA |
| BUF_ENABLE_1 | 1 | NA |
| BUF_ENABLE_2 | 1 | NA |
| BUF_ENABLE_3 | 1 | NA |
| BUF_ENABLE_4 | 1 | NA |
| BUF_ENABLE_5 | 1 | NA |
| BUF_ENABLE_6 | 1 | NA |
| BUF_ENABLE_7 | 1 | NA |
| Component_Name | axi_gpreg_v1_0 | NA |


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




## Registers