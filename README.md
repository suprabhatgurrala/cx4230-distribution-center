# Distribution Center Simulator
**Project 2 for CX 4230**

A discrete event simulator written in Python 3.6 to model the delivery of packages from a distribution center.

`engine.py` has the core simulation engine code

`event_handler.py` has the event handlers for various events

**Execution**

`main.py` has the code for executing the simulator.

It can be run using `python main.py`.

Parameters can be specified for the following:

Flag | Parameter | Default Value
--- | --- | ---
`-v` | Number of vehicles | 4
`-w` | Number of workers | 10
`-p` | Total number of packages | 1000

If a flag is not given or an improper value was passed in, the default value is used.

Example execution using parameters:
`python main.py -p 1000 -v 4 -w 10`

Example output:
```
Running simulation with 1000 packages, 10 workers, 4 vehicles.
Processed 1000 packages:
Average package delivery time: 4250.80 minutes.
10 workers were idle for an average of 2869.30 minutes.
```
Note that output differs on each run due to random variables in the simulation.
