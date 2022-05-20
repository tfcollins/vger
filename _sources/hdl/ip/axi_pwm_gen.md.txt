# axi_pwm_gen

<center>

![axi_pwm_gen](axi_pwm_gen-axi_pwm_gen.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ID | 0 | NA |
| ASYNC_CLK_EN | true | NA |
| N_PWMS | 1 | NA |
| PWM_EXT_SYNC | 0 | NA |
| EXT_ASYNC_SYNC | 0 | NA |
| PULSE_0_WIDTH | 7 | NA |
| PULSE_1_WIDTH | 7 | NA |
| PULSE_2_WIDTH | 7 | NA |
| PULSE_3_WIDTH | 7 | NA |
| PULSE_0_PERIOD | 10 | NA |
| PULSE_1_PERIOD | 10 | NA |
| PULSE_2_PERIOD | 10 | NA |
| PULSE_3_PERIOD | 10 | NA |
| PULSE_0_OFFSET | 0 | NA |
| PULSE_1_OFFSET | 0 | NA |
| PULSE_2_OFFSET | 0 | NA |
| PULSE_3_OFFSET | 0 | NA |
| Component_Name | axi_pwm_gen_v1_0 | NA |


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



### ext_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | ext_clk | clock |




## Registers