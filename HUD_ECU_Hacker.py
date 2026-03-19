"""
Potential example file (not exclusive, only time format set (see above)):
<!-- This file can also be read with an XML reader -->
<html>
<head>  (...)  </head>
<body>
	<div class='Debug'>Date: 7. Mar 2026
		HUD ECU Hacker version: 5.8.2
		.NET Framework version: 4.8.9251.0
		Operating System: Windows 11 Core, Version 23H2, Build 22621, 64 bit
		Current Language: (...)
		CPU: Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz, 8 Cores, 1498 MHz, RAM: 15.8 GB
		ECU Model: OBD2</div>
	<div>&nbsp;</div>
	<div><span class='TimeBk'>15:01:37.190</span><span class='Info'>Open J2534 adapter, Protocol: CAN Raw, 500
			kbaud</span></div>
	<div><span class='TimeBk'>15:01:37.190</span><span class='Info'>CAN ID: 11 and 29 bit, CAN Filter: None, Command ID:
			7E0</span></div>
	<div><span class='TimeBk'>15:01:37.188</span><span class='Debug'>Loading Passthru DLL
			&quot;C:\Windows\SysWOW64\op20pt32.dll&quot;</span></div>
	<div><span class='TimeBk'>15:01:37.596</span><span class='Detail'>Adapter: OpenPort 2.0 J2534 ISO/CAN/VPW/PWM</span>
	</div>
	<div><span class='TimeBk'>15:01:37.596</span><span class='Detail'>Vendor: Tactrix Inc.</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Detail'>Serial Number: TAhJALxt</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Detail'>Driver Version: 1.0.0.4227</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Detail'>Firmware Version: 1.17.4877</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Detail'>Pass-Thru API Version: 04.04</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Detail'>Pass-Thru DLL Version: 1.02.4820 Jul 6 2016
			17:20:04</span></div>
	<div><span class='TimeBk'>15:01:37.610</span><span class='Info'>Measure the vehicle voltage at the J2534
			adapter</span></div>
	<div><span class='TimeBk'>15:01:37.612</span><span class='Detail'>Battery voltage: 13.88V</span></div>
	<div><span class='TimeBk'>15:01:37.613</span><span class='Info'>Clear all filters</span></div>
	<div><span class='TimeBk'>15:01:37.613</span><span class='Info'>Set pass ALL filter</span></div>
	<div><span class='TimeBk'>15:01:37.614</span><span class='Info'>Clear Rx buffer</span></div>
	<div><span class='TimeBk'>15:01:37.614</span><span class='Warning'>Silent monitoring is not possible. Tactrix
			adapters acknowledge all CAN packets as soon as the adapter is opened.</span></div>
	<div><span class='TimeBk'>15:01:37.614</span><span class='Info'>Sniffing data ....</span></div>
	<div><span class='TimeBk'>15:02:48.884</span><span class='RxData'>28D: 00 00 00 00 00 00 00 00</span></div>
	<div><span class='TimeBk'>15:02:48.884</span><span class='RxData'>02F: 11 19 13 20 FC 1F FF 3F</span></div>
	<div><span class='TimeBk'>15:02:48.890</span><span class='RxData'>153: 00 BA 80 00 00 96 00 80</span></div>
	<div><span class='TimeBk'>15:02:48.890</span><span class='RxData'>263: AA 12 00 40 00 00 00 00</span></div>
	<div><span class='TimeBk'>15:02:48.900</span><span class='RxData'>223: 31 F3 FF 7F FE FF FF FF</span></div>
	<div><span class='TimeBk'>15:02:48.900</span><span class='RxData'>10D: FF 3F 00 00</span></div>
	<div><span class='TimeBk'>15:02:48.901</span><span class='RxData'>0B1: 80 79 FF FF 3F FF 1F 1F</span></div>
	<div><span class='TimeBk'>15:02:48.905</span><span class='RxData'>2B9: FF FF FF FF 34 FF 86 18</span></div>
	<div><span class='TimeBk'>15:02:48.905</span><span class='RxData'>02F: AB 1B 13 20 FC 1F FF 3F</span></div>
    <div><span class='TimeBk'>16:24:51.035</span><span class='RxData'>18EF0704: 40 24 22 00 04 00 00 00          '@$&quot;     '</span></div>
    <div><span class='TimeBk'>16:24:51.035</span><span class='RxData'>309: 9F 75 0F 66 FE 3F 00 20               ' u f ?  '</span></div>
    <div><span class='TimeBk'>16:24:51.036</span><span class='RxData'>15A: 91 72 55 55 68 0B 2D 00               ' rUUh - '</span></div>
	<div><span class='TimeBk'>15:02:48.910</span><span class='RxData'>021: 82 23 00 00 00 00 00 00</span></div>
	<div><span class='TimeBk'>15:02:48.910</span><span class='RxData'>4AF: 0F 07 F8 3F</span></div>
	<div><span class='TimeBk'>15:02:48.910</span><span class='RxData'>0A1: 5D A5 00 00 00 00 C0 00</span></div>
    (...)
</body>
</html>
"""

import can
from bs4 import BeautifulSoup
import sys

filename = sys.argv[1] if len(sys.argv) == 2 else "test.htm"

with open(filename, "r") as f:
    html = f.read()

parsed_html = BeautifulSoup(html, features="html.parser")
init_time = None

with open(filename.removesuffix(".htm") + ".asc", "w") as f_out:
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

