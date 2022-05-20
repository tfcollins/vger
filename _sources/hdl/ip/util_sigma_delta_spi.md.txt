# util_sigma_delta_spi

<center>

![util_sigma_delta_spi](util_sigma_delta_spi-util_sigma_delta_spi.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| NUM_OF_CS | 1 | NA |
| CS_PIN | 0 | NA |
| IDLE_TIMEOUT | 63 | NA |
| Component_Name | util_sigma_delta_spi_v1_0 | NA |


## Buses


### m_spi
| Logical | Physical | Type |
| ------- | -------- | ---- |
| SCLK | m_sclk | spi_master |
| SDI | m_sdi | spi_master |
| SDO | m_sdo | spi_master |
| SDO_T | m_sdo_t | spi_master |
| CS | m_cs | spi_master |



### s_spi
| Logical | Physical | Type |
| ------- | -------- | ---- |
| SCLK | s_sclk | spi_master |
| SDI | s_sdi | spi_master |
| SDO | s_sdo | spi_master |
| SDO_T | s_sdo_t | spi_master |
| CS | s_cs | spi_master |



### m_spi_s_spi_signal_clock
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk | clock |



### m_spi_s_spi_signal_reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | resetn | reset |




## Registers