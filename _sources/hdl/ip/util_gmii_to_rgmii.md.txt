# util_gmii_to_rgmii

<center>

![util_gmii_to_rgmii](util_gmii_to_rgmii-util_gmii_to_rgmii.svg)

</center>

## Parameters

| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| PHY_AD | "10000" | NA |
| IODELAY_CTRL | "0" | NA |
| IDELAY_VALUE | 18 | NA |
| IODELAY_GROUP | if_delay_group | NA |
| REFCLK_FREQUENCY | 200 | NA |
| Component_Name | util_gmii_to_rgmii_v1_0 | NA |


## Buses


### gmii
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TXD | gmii_txd | gmii |
| TX_EN | gmii_tx_en | gmii |
| TX_ER | gmii_tx_er | gmii |
| RXD | gmii_rxd | gmii |
| RX_DV | gmii_rx_dv | gmii |
| RX_ER | gmii_rx_er | gmii |
| CRS | gmii_crs | gmii |
| COL | gmii_col | gmii |
| TX_CLK | gmii_tx_clk | gmii |
| RX_CLK | gmii_rx_clk | gmii |



### rgmii
| Logical | Physical | Type |
| ------- | -------- | ---- |
| TD | rgmii_td | rgmii |
| TX_CTL | rgmii_tx_ctl | rgmii |
| TXC | rgmii_txc | rgmii |
| RD | rgmii_rd | rgmii |
| RX_CTL | rgmii_rx_ctl | rgmii |
| RXC | rgmii_rxc | rgmii |



### clk_20m
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk_20m | clock |



### clk_25m
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk_25m | clock |



### clk_125m
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | clk_125m | clock |



### idelayctrl_clk
| Logical | Physical | Type |
| ------- | -------- | ---- |
| CLK | idelayctrl_clk | clock |



### reset
| Logical | Physical | Type |
| ------- | -------- | ---- |
| RST | reset | reset |




## Registers