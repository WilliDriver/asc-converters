"""
Potential example file (not exclusive):
(1729347424.747187) can1 41F#FE1F0402C4000006
(1729347424.751979) can1 007#608D38003F54AF7F
(1729347424.762027) can1 205#02780C0F00000000
(1729347424.771699) can1 385#000000
(1729347424.773413) can1 41E#FE1E040200000006
(1729347424.774888) can1 025#8F00
(...)
"""

import can
import sys

filename = sys.argv[1].removesuffix(".log") if len(sys.argv) == 2 else "test"

bus = can.LogReader(filename + ".log")

with open(filename + ".asc", "w") as f_out:
    log_out = can.io.ASCWriter(f_out)
    for i in bus:
        log_out.on_message_received(i)
        # if i.channel == "can1":
        #     log_out.on_message_received(i)

