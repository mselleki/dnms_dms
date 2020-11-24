import pyxid2
import time

devices = pyxid2.get_xid_device()
print(devices)
dev = devices[0]
dev.reset_base_timer()
dev.reset_rt_timer()
