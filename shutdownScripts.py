import os
from iplist import hostname


for host in hostname:
    shutdown = os.system((r"shutdown /s /m \\{} -t 0").format(host))
    print("shutingdown Host : {}").format(host)
