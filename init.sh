#!/bin/sh
sudo apt-get install -y software-properties-common
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible

cp hosts.template > hosts
cp group_vars/all.template > group_vars/all
