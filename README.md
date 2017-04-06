<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [initVM](#initvm)
  - [Todo](#todo)
  - [Usage](#usage)
    - [Basic installation](#basic-installation)
    - [doctoc](#doctoc)
    - [TensorFlow](#tensorflow)
    - [Jupyter Notebook](#jupyter-notebook)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# initVM
Ansible playbooks for VMs initialization

## Todo
- [x] Timeout the `install vim plugins` task.
- [ ] Add `/etc/hosts` file modification

## Usage

    sh -c "$(wget https://raw.githubusercontent.com/chapter09/initVM/master/init.sh -O -)"

### Basic installation
1. Run `init.sh`
2. Rename `host.template` to `host`
3. Add your public keys (e.g., `https://github.com/chapter09.keys`) to `group_vars/all`
4. Run `ansible-playbook site.yml`

### doctoc

### Jupyter 

    ansible-playbook jupyter.yml

### TensorFlow



### Jupyter Notebook
