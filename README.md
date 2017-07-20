push2clip
========
**push2clip** is a combination of Tasker profile and python script which allows you to set the clipboard on your phone from your shell.

Why?
--------
There are many ways to move data between your computer and your phone, and this is by no means the best way, and possibly not even a good way. However, I created this as an excercise in using python to interact with a Tasker profile on my phone. This lays the foundation for more interesting scripts.


Requirements
--------
- [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)
- [Simplepush](https://play.google.com/store/apps/details?id=io.tymm.simplepush)
- Python 3
  - Requests
  - click


Installation
--------
- Clone git repo:
```
~$ git clone https://github.com/kf5grd/push2clip.git
```


- Run install with pip:
```
~$ pip install .
    [...]
    Cleaning up...
~$ 
```


Setup
--------
- Import SPSetClipboard.prf.xml into Tasker:
  - long press on the "Profiles" tab
  - Select "Import," then navigate to the location of the xml file.
- Create "tasker" event in Simplepush app:
  - Tap the menu icon
  - Choose "Events"
    - Event ID: tasker
    - Vibration: None
    - Ringtone: None
    - Disable Notifications: Checked
- Initialize push2clip python script:
  - `~$ push2clip init <simplepush key>`


Usage
--------
Send custom message to clipboard:
```
~$ push2clip -m "Any message here."
```

Pipe output of command into push2clip:
```
~$ uptime | push2clip
```


License
--------
This software is licensed under **GPL-3.0+**
