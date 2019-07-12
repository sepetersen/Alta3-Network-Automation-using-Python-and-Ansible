#!/usr/bin/env python3

# must be run inside a KVM (usually beachhead)
# python3 lab_complete.py <NUMBER>

import sys 
import requests
import datetime
import os
from pathlib import Path
import slackweb

# acquire data
if (len(sys.argv)) != 2:
    print("Failed to provide the appropriate number of arguments (1 argument required, the lab number completed)")
    sys.exit(1)
lab_number = sys.argv[1]
print("Registering lab %s completed" % lab_number)

# format data
metadata = os.uname()[1]
now = datetime.datetime.now().replace(microsecond=0).isoformat(' ')

# append output_line to prog_file
prog_file_path = '%s' % ( metadata)
progress_line = "%s\t%s\t" % (metadata, lab_number)
with open(prog_file_path, 'a') as prog_file:
    prog_file.write(progress_line)
with open(prog_file_path, 'r') as prog_file:
    progress_report = prog_file.read()

live_line = "Lab complete -- %s  Lab# %s\n" % (metadata, lab_number)
slack = slackweb.Slack(url = "https://hooks.slack.com/services/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")
slack.notify(
  text=live_line,
  channel="#labs-live",
  username="k8s",)
