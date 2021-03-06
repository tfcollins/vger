---
hide-toc: true
---

# Analog Devices, Inc. Prototyping Platform

The ADI prototyping platform is a set of resources and tools that can be used for system-level prototyping and leverage for end products.

This is reference documentation that is heavily tied to the source code of the different supporting projects. The following project branches or tags and associated tools are reflected in this documentation:

| Project | Branch or Tag | Tooling Versions |
| ------- | ------ | ---------------- |
| [hdl](https://github.com/analogdevicesinc/hdl) | master | Vivado {{vivado_version}}, Quartus {{quartus_version}} |
| [no-OS](https://github.com/analogdevicesinc/no-os) | master | Vivado {{vivado_version}}, Quartus {{quartus_version}} |
| [Linux](https://github.com/analogdevicesinc/linux) | master | Vivado {{vivado_version}}, Quartus {{quartus_version}} |

Not all possible permutations of tools and branches are available as certain branches or tags are upgraded on a bi-annual basis. Collectively these are called releases, which are tested through a rigorous QA process. If you want to use the master/main branches, also known as non-release branches, these branches should be considered unstable and bugs may exist. Please start from release branches if possible. Otherwise, support can be limited.


```{panels}
:header: text-center bg-info
**Quick Start and Tutorials**
^^^

Introduction to platform

Where to start?

Getting support

---
:header: text-center bg-info
**Embedded Software**
^^^
[Linux kernel](http://google.com): A complete kernel part of

[ADI Kuiper Linux](http://google.com): Standard Linux image complete with kernel and userspace

[PetaLinux](http://google.com): This is a test

[No-OS](http://google.com):  Baremetal projects and standalone drivers



---
:header: text-center bg-info
**HDL, FPGAs, and Hardware**
^^^

Supported Platforms

Evaluation Systems

System-On-Modules

Modules

Attach



---
:header: text-center bg-info
**Interface and High-Level Tools**
^^^

[pyadi-iio](https://analogdevicesinc.github.io/pyadi-iio): Python interfaces for ADI devices with IIO drivers

[MATLAB Toolboxes](https://analogdevicesinc.github.io/TransceiverToolbox/master): Interfaces for data streaming, HDL/C targeting, and behavioral models in MATLAB


```

### Overview

```{toctree}
index: Home
```

```{toctree}
:caption: Tutorials
:hidden:

tutorials/index
```

```{toctree}
:caption: Embedded Software
:hidden:

linux/kuiper
linux/petalinux
linux/drivers
no_os/no_os_project_index

```

```{toctree}
:caption: HDL
:hidden:

hdl/hdl_reference_design_index
hdl/hdl_ip_core_index
```

```{toctree}
:caption: Tools
:hidden:

tools/part_tools
```

```{toctree}
:caption: Hardware
:hidden:

```

```{toctree}
:caption: Developers
:hidden:

vger
```
