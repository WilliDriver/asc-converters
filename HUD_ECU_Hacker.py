import can
from bs4 import BeautifulSoup
import datetime
import sys

filename = sys.argv[1].removesuffix(".htm") if len(sys.argv) == 2 else "test"

with open(filename + ".htm", "r") as f:
    html = f.read()

parsed_html = BeautifulSoup(html, features="html.parser")
# print(i.text[:28])
init_time = None

with open(filename + ".asc", "w") as f_out:
    log_out = can.io.ASCWriter(f_out)
    for idx, i in enumerate(parsed_html.body.find_all('span', attrs={'class':'RxData'})):
        if i:
            id = int(i.text.split(": ")[0],16)
            time_str = i.previous_sibling.text
            time = (int(time_str[0:2])*3600 + int(time_str[3:5])*60 + int(time_str[6:8]) + int(time_str[9:12]) /1000)
            if not init_time:
                init_time = time
                last_time = 0
            rel_time = time - init_time
            if last_time > rel_time:
                raise ValueError("Frames not in order.")
            last_time = rel_time
            # print(time-init_time)
            data = [int(d, 16) for d in i.text.split(": ")[1][:23].split(" ")]
            msg = can.Message(timestamp=rel_time,arbitration_id=id,data=data,is_extended_id=False)
            # print(msg)
            log_out.on_message_received(msg)
        else: 
            raise Exception(i.text)

