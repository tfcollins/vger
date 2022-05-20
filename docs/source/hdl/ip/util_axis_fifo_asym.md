# util_axis_fifo_asym

<center>

![util_axis_fifo_asym](util_axis_fifo_asym-util_axis_fifo_asym.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| ASYNC_CLK | 1 | NA |
| S_DATA_WIDTH | 64 | NA |
| S_ADDRESS_WIDTH | 5 | NA |
| M_DATA_WIDTH | 128 | NA |
| M_AXIS_REGISTERED | 1 | NA |
| ALMOST_EMPTY_THRESHOLD | 4 | NA |
| ALMOST_FULL_THRESHOLD | 4 | NA |
| TLAST_EN | 0 | NA |
| TKEEP_EN | 0 | NA |
| Component_Name | util_axis_fifo_asym_v1_0 | NA |


## Buses


### s_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | s_axis_valid | axis |
| TREADY | s_axis_ready | axis |
| TDATA | s_axis_data | axis |
| TLAST | s_axis_tlast | axis |



### m_axis
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TVALID | m_axis_valid | axis |
| TREADY | m_axis_ready | axis |
| TDATA | m_axis_data | axis |
| TLAST | m_axis_tlast | axis |



### m_axis_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | m_axis_aclk | clock |



### m_axis_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | m_axis_aresetn | reset |



### s_axis_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | s_axis_aclk | clock |



### s_axis_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | s_axis_aresetn | reset |




## Registers