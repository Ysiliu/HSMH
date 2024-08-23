The HSMH source code, including the simulator part, and experiment results in the paper "An Efficient Approach for Improving Message Acceptance Rate and Link Utilization in Time-Sensitive Networking"

component: various components that are used to build a tsn network, including switch, host, link, gcl, flow, flowset, fifoqueue, heapqueue, node, port, and routetable.

config: config.py contains some parameters used by a network.

data: generate_data.py is used to randomly generate some flow data in a network.

simulation: simulation_BT.py, simulation_PASA.py, simulation_EDF.py, and simulation_HSMH.py denote the four algorithms described in the paper, respectively.