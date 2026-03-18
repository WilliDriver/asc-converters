# A simple Collection of Programms that can convert to .asc files

The main intrest was to be able to take all kind of Log files and import them into the official MB Xentry CAN-Tool

## HUD_ECU_HACKER.py

For log files created by the sniffing mode of [HUD ECU Hacker](https://www.netcult.ch/elmue/HUD%20ECU%20Hacker/).

Input: Command line argument with file name (.htm)

Output: .asc file with the same Can Frames and relative times

> Tiny unrelated Tip: If you want to capture a non OBD-Port accesible can-bus, with a Tatrix Openport, and get errors about the Voltage, Plug into OBD, open connection, then unplug and do CAN-monitoring

# socketcan_log.py

For logs created with the candump utility of Socketcan Tools.

Input: Command line argument with file name (.log)

Output: .asc file with the same Can Frames and relative times