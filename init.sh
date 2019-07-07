#!/bin/sh
sudo umount /tmp
sudo apt-get install -y software-properties-common
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible python-apt git

# create key-pair
ssh-keygen -P "" -t rsa -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

git clone https://github.com/chapter09/initVM.git

cd initVM
sudo ln -s $PWD/rsync.py /usr/local/bin/prsync
cp hosts.template hosts
cp group_vars/all.template group_vars/all
