# Linux Drivers and Kernel

ADI maintains Linux drivers for a large number of components including ADCs, DACs, IMUs, accelerometers, transceivers, beamformers, and many others. Drivers are available from the [Linux git repository](https://github.com/analogdevicesinc/linux), which can be used as is (recommended) or merged into your own kernel. The ADI Kuiper Linux distribution uses this kernel by default provided by the [development SD cards](https://wiki.analog.com/resources/tools-software/linux-software/embedded_arm_images).

The same Kuiper Linux SD card image can be used across all supported development kits such as: Xilinx FPGA or Intel FPGA development kits, and Raspberry Pi small board computers. It can be ported to other platforms from my leveraging existing devicetrees or creating custom ones for new boards.

For new users to ADI component, it is always recommended to start with the Kuiper Linux when available.

Linux resources:
```{toctree}
:maxdepth: 1

build
dt_bindings/index
```
