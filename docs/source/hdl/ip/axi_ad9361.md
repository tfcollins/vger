# axi_ad9361

<center>

![axi_ad9361](axi_ad9361-axi_ad9361.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| MODE_1R1T | 0 | NA |
| FPGA_TECHNOLOGY | 0 | NA |
| FPGA_FAMILY | 0 | NA |
| SPEED_GRADE | 0 | NA |
| DEV_PACKAGE | 0 | NA |
| TDD_DISABLE | 0 | NA |
| PPS_RECEIVER_ENABLE | 0 | NA |
| CMOS_OR_LVDS_N | 0 | NA |
| ADC_INIT_DELAY | 0 | NA |
| ADC_DATAPATH_DISABLE | 0 | NA |
| ADC_USERPORTS_DISABLE | 0 | NA |
| ADC_DATAFORMAT_DISABLE | 0 | NA |
| ADC_DCFILTER_DISABLE | 0 | NA |
| ADC_IQCORRECTION_DISABLE | 0 | NA |
| DAC_INIT_DELAY | 0 | NA |
| DAC_CLK_EDGE_SEL | 0 | NA |
| DAC_IODELAY_ENABLE | 0 | NA |
| DAC_DATAPATH_DISABLE | 0 | NA |
| DAC_DDS_DISABLE | 0 | NA |
| DAC_DDS_TYPE | 1 | NA |
| DAC_DDS_CORDIC_DW | 14 | NA |
| DAC_DDS_CORDIC_PHASE_DW | 13 | NA |
| DAC_USERPORTS_DISABLE | 0 | NA |
| DAC_IQCORRECTION_DISABLE | 0 | NA |
| IO_DELAY_GROUP | dev_if_delay_group | NA |
| IODELAY_CTRL | 1 | NA |
| MIMO_ENABLE | 0 | NA |
| USE_SSI_CLK | 1 | NA |
| DELAY_REFCLK_FREQUENCY | 200 | NA |
| RX_NODPA | 0 | NA |
| Component_Name | axi_ad9361_v1_0 | NA |


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



### l_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | l_clk | clock |



### delay_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | delay_clk | clock |



### rst
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | rst | reset |



### gps_pps_irq
| Logical | Physical | Type |
| ------- | -------- | ---- |
| INTERRUPT | gps_pps_irq | interrupt |




## Registers