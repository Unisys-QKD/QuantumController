installations - 
# QuantumController


## Table of Contents
1. [Installations](#installations)
2. [Prerequisites](#prerequisites)
3. [How to Run Application](#how-to-run-application)
4. [References](#references)
5. [Applications](#applications)
6. [Tech Stack](#tech-stack)

## Installations

You need to have Ryu and Tornado installed to run this application.

You can install Ryu using :

-( Ryu works with python 3.8.5 or below)
```bash
pip install ryu
```

You can install dnspython==2.2.1 using :

```bash
python3 -m pip install dnspython==2.2.1
```

You can install eventlet using :

```bash
sudo apt install python3-eventlet
```

You can install qunetsim using :

```bash
pip install qunetsim
```

You can install tornado using :

```bash
pip install tornado
```

## Prerequisites

## How-to-run-application
Run Ryu_controller.py using the following command:
```bash
ryu-manager
```

## References
- https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5caf637f3&appId=PPGMS)


## Applications



## tech-stack

### Ryu:
- Component-based software-defined networking (SDN) framework written in Python.
- Provides a library for implementing SDN controllers using the OpenFlow protocol.
- `Ryu_controller.py` file utilizes Ryu to create a custom application implementing basic OpenFlow functionalities.

prerequisites 
how to run application 
References
Applications
Tech stack
<a href="https://aimeos.org/">
    <img src="https://aimeos.org/fileadmin/template/icons/logo.png" alt="Aimeos logo" title="Aimeos" align="right" height="60" />
</a>
### Tornado:
- Python web framework and asynchronous networking library.
- Well-suited for building high-performance, non-blocking web servers and applications.
- `App1.py` file uses Tornado to create a simple web application responding with "Hello, world" to HTTP requests.

# Aimeos TYPO3 extension
### Mininet:
- Network emulator used for creating virtual networks for testing SDN applications.
- Allows creating realistic network topologies using lightweight virtualization techniques.
- `mininet_setup.py` file sets up a custom network topology using Mininet, creating switches, hosts, and establishing links between them.

[![Total Downloads](https://poser.pugx.org/aimeos/aimeos-typo3/d/total.svg)](https://packagist.org/packages/aimeos/aimeos-typo3)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/aimeos/aimeos-typo3/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/aimeos/aimeos-typo3/?branch=master)
[![License](https://poser.pugx.org/aimeos/aimeos-typo3/license.svg)](https://packagist.org/packages/aimeos/aimeos-typo3)
### OpenFlow Protocol:
- Communication protocol enabling control of forwarding behavior of network devices (e.g., switches, routers) by external controllers.
- Utilized by Ryu and Mininet for communication between the controller and switches in the network.

:star: Star us on GitHub — it motivates us a lot!
### Python:
- Versatile programming language extensively used in the project.
- Utilized for implementing SDN applications, web servers, and network automation scripts.
- All provided files (`Ryu_controller.py`, `App1.py`, `Simple_switchex.py`, `mininet_setup.py`) are written in Python.

[Aimeos](https://aimeos.org/TYPO3) is THE professional, full-featured and
high performance e-commerce extension for TYPO3!  You can install it in your
existing TYPO3 web site within 5 minutes and can adapt, extend, overwrite
and customize anything to your needs.
