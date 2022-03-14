#!/usr/bin/env python3
from fabric import *

env.hosts = [
        'pi@192.168.1.15',
        'pi@192.168.1.16',
        'pi@192.168.1.17',
        'pi@192.168.1.18',
        ]

env.password = 'raspberry'

@parallel
def check():
    host_type()

@parallel
def allshutdown():
    sudo("sudo shutdown now")

@parallel
def allreboot():
    sudo("shutdown -r ")

@parallel
def allcancel():
    sudo("shutdown -c")

@parallel
def cmd(command):
    sudo(command)

def allip():
    sudo("ifconfig eth0")

