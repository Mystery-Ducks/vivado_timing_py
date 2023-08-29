# Vivado Timing Generator  
A simple python script to generate timing code for simulations in Vivado FPGA simluation software.  
The output is in the format:  

  
`'0', '1' after 100ns, '0' after 200ns, '1' after 300ns;`  

This format is used for the VHDL language.

This was written for Python2.7 because I have no idea what I'm doing, however a version check has been implemented and it now runs on python3.

Tested working on the following python versions:

* 3.11.4
* 2.7.18.7
