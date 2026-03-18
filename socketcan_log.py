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

