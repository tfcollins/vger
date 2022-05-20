# util_axis_upscale

<center>

![util_axis_upscale](util_axis_upscale-util_axis_upscale.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| NUM_OF_CHANNELS | 4 | NA |
| DATA_WIDTH | 24 | NA |
| UDATA_WIDTH | 32 | NA |
| Component_Name | util_axis_upscale_v1_0 | NA |


## Buses


### s_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | s_axis_valid | axis |
| TREADY | s_axis_ready | axis |
| TDATA | s_axis_data | axis |



### s_axis_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk | clock |



### s_axis_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | resetn | reset |



### m_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | m_axis_valid | axis |
| TREADY | m_axis_ready | axis |
| TDATA | m_axis_data | axis |




## Registers