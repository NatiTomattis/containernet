#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')


net = Containernet(controller=None)

info('*** Adding controller\n')
# net.addController(c0)

info('*** Adding docker containers\n')
# d1 = net.addDocker('d1', ip='10.0.0.251', dimage="docker_snort:latest")
d2 = net.addDocker('d2', ip='10.0.0.252', dimage="alpine:latest", dcmd="ssh")
d1 = net.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:trusty")
# d2 = net.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:trusty")
h1 = net.addHost('h1', ip='10.0.0.253')

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')

info('*** Creating links\n')
net.addLink(d1, s2)
net.addLink(h1, s1)
net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(s1, d2)

info('*** Starting network\n')
net.start()

# d2.setIP(ip='10.0.0.252', prefixLen=16)

info('*** Testing connectivity\n')
# net.ping([d1, d2])



info('*** Running CLI\n')
CLI(net)

info('*** Stopping network')
net.stop()

