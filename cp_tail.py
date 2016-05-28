#! /usr/bin/env python
import sefim

n = "10"
filename = "/var/log/syslog"
print sefim.runner("tail -n %s %s" % (n, filename))
