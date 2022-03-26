Building Kernels
################

Building the ADI Linux kernel must be done on a Linux machine, Linux VM, or through `WSL <https://docs.microsoft.com/en-us/windows/wsl/about>`_ as Windows cannot support the kernel's filesystem by default. It will also require a supported compiler and a few utilities. For FPGA based platforms it is typically recommended to use the vendor tools for that platform, such as from Xilinx's SDK (or Vitis), Intel's SDK, or the standard ARM compilers from the Linaro project.

This version of the documentation is targeted at the |release_version_bold| release of the ADI prototyping platform and related tools. For other versions including **master** development branches, select the target release from the sidebar dropdown.

Installing Dependencies
-----------------------

First install the target compiler for your platform:

* `Xilinx FPGA <dd>`_
* `Intel FPGA <dd>`_
* `Raspberry PI <dd>`_

Install the additional tools:

.. tab:: Debian/Ubuntu

    .. code-block:: bash

      sudo apt-get install git build-essential fakeroot libncurses5-dev libssl-dev ccache
      sudo apt-get install dfu-util u-boot-tools device-tree-compiler libssl1.0-dev mtools
      sudo apt-get install bc python cpio zip unzip rsync file wget

.. tab:: RHEL/Fedora

    .. code-block:: bash

      sudo dnf install git gcc flex make bison openssl-devel elfutils-libelf-devel


Building Instructions
---------------------

First clone the kernel source and checkout the target branch:

.. code-block:: bash
  :substitutions:

  git clone -b |linux_branch| https://github.com/analogdevicesinc/linux.git


Next build for the desired target platform.

.. tab:: Zynq

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm
      export CROSS_COMPILE="arm-linux-gnueabihf-"

    Configure and build the kernel

    .. code-block:: bash

      make zynq_xcomm_adv7511_defconfig
      make -j5 UIMAGE_LOADADDR=0x8000 uImage


.. tab:: ZynqMP

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm64
      export CROSS_COMPILE="aarch64-linux-gnu-"

    Configure and build the kernel

    .. code-block:: bash

      make adi_zynqmp_defconfig
      make -j5 Image UIMAGE_LOADADDR=0x8000

.. tab:: Intel

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm
      export CROSS_COMPILE="arm-linux-gnueabi-"

    Configure and build the kernel

    .. code-block:: bash

      make make socfpga_adi_defconfig
      make -j5 zImage
