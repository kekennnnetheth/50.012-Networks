# 50.012 Networks Spring 2015
# Lab 4 install script
# Nils, SUTD, 2015
sudo apt -y install python-matplotlib mininet openvswitch-testcontroller
# fix the ovs-controller renaming problem with mininet
sudo cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller
