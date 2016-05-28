#! /usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime

import sefim
from yardimci import Dosya


def formatter(input, by):
    return [i for i in input if by in i][0].split(":")[1].strip()

aide_out = sefim.runner("/usr/bin/aide -c /etc/aide/aide.conf --check")

# aide_out örneği bul :D
added = formatter(aide_out, "Added files:")
changed = formatter(aide_out, "Changed files:")
removed = formatter(aide_out, "Removed files:")

subject = "(A:%s)(R:%s)(C:%s)" % (added, removed, changed)
sefim.send_mail(subject, aide_out)

aide_outF = datetime.now().strftime("%Y%m%d%H%M")
Dosya.yaz("/var/log/aide/hourly/%s.log" % aide_outF, aide_out)
Dosya.yaz("/var/log/aide/hourly/last_scan.log" % aide_outF, aide_out)
