# axi_ltc2387

<center>

![axi_ltc2387](axi_ltc2387-axi_ltc2387.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| FPGA_TECHNOLOGY | 1 | NA |
| FPGA_FAMILY | 1 | NA |
| SPEED_GRADE | 1 | NA |
| DEV_PACKAGE | 1 | NA |
| IO_DELAY_GROUP | adc_if_delay_group | NA |
| IODELAY_CTRL | 1 | NA |
| DELAY_REFCLK_FREQUENCY | 200 | NA |
| USERPORTS_DISABLE | 0 | NA |
| DATAFORMAT_DISABLE | 0 | NA |
| ADC_INIT_DELAY | 22 | NA |
| ADC_RES | 16 | NA |
| OUT_RES | 16 | NA |
| TWOLANES | 1 | NA |
| Component_Name | axi_ltc2387_v1_0 | NA |


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



### ref_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | ref_clk | clock |



### dco_p
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dco_p | clock |



### dco_n
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dco_n | clock |




## Registers