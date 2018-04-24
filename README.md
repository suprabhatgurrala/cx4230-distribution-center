# Distribution Center Simulator
Project 2 for CX 4230

A discrete event simulator written in Python 3.6 to model the delivery of packages from a distribution center.

`engine.py` has the core simulation engine code

`event_handler.py` has the event handlers for various events

**Execution**

`main.py` has the code for executing the simulator.

It can be run using `python main.py`.

Parameters can be specified for the following:
| Flag          | Parameter                 | Default value
|:-------------:|:-------------------------:|:-------------:|
| `-v`          | Number of vehicles        | 4
| `-w`          | Number of workers         | 10
| `-p`          | Total number of packages  | 500

If a flag is not given or an improper value was passed in, the default value is used.

Example execution using parameters:
`python main.py -p 1000 -v 5 -w 20`
