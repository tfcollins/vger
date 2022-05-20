# axi_clkgen

<center>

![axi_clkgen](axi_clkgen-axi_clkgen.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| FPGA_TECHNOLOGY | 0 | NA |
| FPGA_FAMILY | 0 | NA |
| SPEED_GRADE | 0 | NA |
| DEV_PACKAGE | 0 | NA |
| FPGA_VOLTAGE | 0 | NA |
| CLKSEL_EN | 0 | NA |
| CLKIN_PERIOD | 5 | NA |
| CLKIN2_PERIOD | 5 | NA |
| VCO_DIV | 11 | NA |
| VCO_MUL | 49 | NA |
| CLK0_DIV | 6 | NA |
| CLK0_PHASE | 0 | NA |
| CLK1_DIV | 6 | NA |
| CLK1_PHASE | 0 | NA |
| Component_Name | axi_clkgen_v1_0 | NA |
| ENABLE_CLKIN2 | false | NA |
| ENABLE_CLKOUT1 | false | NA |


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



### clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk | clock |



### clk2
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk2 | clock |



### clk_0
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk_0 | clock |



### clk_1
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk_1 | clock |




## Registers