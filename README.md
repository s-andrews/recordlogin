Record Login
============

A small python curses app we use to let people tell us that they've successully logged in to a test server.

We use this program in advance of courses which use cloud based servers for the exercises.  Significant amounts of time can be wasted during the course dealing with simple connection issues to get a key based SSH connection to an EC2 server to work.  This script can be installed on a very small, inexpensive server in advance of the course to give the participants chance to try out the SSH connection and debug any issues before the course starts.

![RecordLogin Screenshot](https://raw.githubusercontent.com/s-andrews/recordlogin/master/interface_screenshot.png)

The ```recordlogin.py``` script can be launched from the users ```.bash_profile``` so it runs immediately upon login.  It launches a simple curses based interface which tells them they have logged in and asks them to enter their name so we can keep track of who has managed to log in.  It then shows a final message before automatically logging them out.   Details of the successful logins and their times are written to a hidden file ```~/.recorded_logins.txt```.

Installation
------------

From a blank EC2 default image you can run:

```
sudo yum -y install git python3

sudo timedatectl set-timezone Europe/London

git clone https://github.com/s-andrews/recordlogin.git

echo "~/recordlogin/recordlogin.py" >> ~/.bash_profile
```

All future logins should now launch the program.


Retrieving successful logins
----------------------------

Simply log in to the server and then use ```Control+C``` to quit out of the ```recordlogin.py``` script and use ```less ~/.recorded_logins.txt``` to view the successfully recorded logins to the server.






