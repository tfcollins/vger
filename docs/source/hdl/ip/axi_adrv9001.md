# axi_adrv9001

<center>

![axi_adrv9001](axi_adrv9001-axi_adrv9001.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| CMOS_LVDS_N | 0 | NA |
| TDD_DISABLE | 0 | NA |
| DDS_DISABLE | 0 | NA |
| INDEPENDENT_1R1T_SUPPORT | 1 | NA |
| COMMON_2R2T_SUPPORT | 1 | NA |
| DISABLE_RX2_SSI | 0 | NA |
| DISABLE_TX2_SSI | 0 | NA |
| RX_USE_BUFG | 0 | NA |
| TX_USE_BUFG | 0 | NA |
| IODELAY_CTRL | 1 | NA |
| IO_DELAY_GROUP | dev_if_delay_group | NA |
| FPGA_TECHNOLOGY | 0 | NA |
| FPGA_FAMILY | 0 | NA |
| SPEED_GRADE | 0 | NA |
| DEV_PACKAGE | 0 | NA |
| EXT_SYNC | 0 | NA |
| USE_RX_CLK_FOR_TX | 0 | NA |
| Component_Name | axi_adrv9001_v1_0 | NA |


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



### delay_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | delay_clk | clock |



### adc_1_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | adc_1_clk | clock |



### adc_2_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | adc_2_clk | clock |



### dac_1_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dac_1_clk | clock |



### dac_2_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | dac_2_clk | clock |



### adc_1_rst
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | adc_1_rst | reset |



### adc_2_rst
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | adc_2_rst | reset |



### dac_1_rst
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dac_1_rst | reset |



### dac_2_rst
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | dac_2_rst | reset |




## Registers