#!/bin/python

from dataclasses import dataclass
import subprocess
import json
import time

@dataclass
class Notification:
    body: str
    message: str
    summary: str
    appname: str
    category: str
    dan: str        # Default Action Name
    icon_path: str
    n_id: int       
    timestamp: int  # PC's uptime when notification was sent in milliseconds
    timeout: int
    progress: int


    def print(self):
        ms = int(time.clock_gettime(time.CLOCK_BOOTTIME)*1000000) - self.timestamp
        hours = int(ms // 3.6e9)
        mins  = int(ms // 6e7) % 60
        secs  = int(ms // 1e6) % 60

        print(f"\t{self.appname}: {self.body}")
        print(f"\t{hours}h {mins}m {secs}s ago")


notifs = []
history = json.loads(subprocess.check_output(['dunstctl', 'history']))

for n in history.get('data')[0]:
    notifs.append(Notification(
        n.get('body').get('data'),
        n.get('message').get('data'),
        n.get('summary').get('data'),
        n.get('appname').get('data'),
        n.get('category').get('data'),
        n.get('default_action_name').get('data'),
        n.get('icon_path').get('data'),
        n.get('id').get('data'),
        n.get('timestamp').get('data'),
        n.get('timeout').get('data'),
        n.get('progress').get('data'),
        )
    )

if (l := len(notifs)) == 1:
    print("1 notification:")
elif l > 1:
    print(f"{l} notifications:")
else:
    print("no notifications")

for i in reversed(notifs):
    i.print()
    print()

