# How to use

This document describes how to run the team formation translator.
The available **mode** are:
* tf, classical team formation;
* ktf, robust team formation (at least k agents should be able to realize each
  skills).

To run this software you will need to install **PySAT**.
To do it please run the following command line (you can also directly use
  **pip** instead of using **python** to install the required libraries):
````bash
python3 -m pip install python-sat[pblib,aiger]
````
