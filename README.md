# GlobalSat DG-100

I've got a GlobalSat DG-100 GPS logger.
It's possible to put it into what the documentation refers to as "GMouse Mode",
which simply outputs NEMA sentences to the USB serial port.
Unfortunately it doesn't do this automatically, it requires a binary serial command to enable this mode.

# dg100.py

This is a quick and dirty Python script that enables said "GMouse Mode."
Once run, any other software expecting NEMA output can connect and start receiving data.
It will continue to output until it receives a command otherwise, or is turned off.

# Commands
For reference, if you wish to implement your own software, here's what you need to know.

## Enable

The data to enable the "GMouse Mode" is

`a0 a2 00 02 bc 01 00 bd b0 b3`

## Disable

The data to disable the "GMouse mode" is

`02 00 01 85 84 a0 a2 00 02 bc 00 00 bc b0 b3`
