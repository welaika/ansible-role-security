Ansible Role Security
=====================

[![Build Status](https://travis-ci.org/welaika/ansible-role-security.svg?branch=master)](https://travis-ci.org/welaika/ansible-role-dotfiles)

Some common security tweaks, e.g.:

* change OpenSSH server port
* do not allow root login
* install fail2ban and configure the jail for sshd
* ...

This role has been forked from [ https://github.com/geerlingguy/ansible-role-security ](https://github.com/geerlingguy/ansible-role-security). Thank you!

Requirements
------------

OpenSSH server must already be installed and running.

Role Variables
--------------

These are the default variables:

```yaml
security_ssh_port: 22  # change it!
security_ssh_password_authentication: "no"  # keep quotes!
security_ssh_permit_root_login: "no"  # keep quotes!
security_ssh_usedns: "no"  # keep quotes!
security_ssh_permit_empty_password: "no"  # keep quotes!
security_ssh_challenge_response_auth: "no"  # keep quotes!
security_ssh_gss_api_authentication: "no"  # keep quotes!
security_ssh_x11_forwarding: "no"  # keep quotes!
```

Dependencies
------------

Nope :)

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: ansible-role-security
      vars:
        security_ssh_port: 6666  # you should change this!
```

License
-------

MIT

Testing
-------

Install molecule

`$ pip3 install --user 'molecule[docker]'`

Start docker and run

`$ molecule test`

Author Information
------------------

made with ❤️ and ☕️ by [weLaika](https://dev.welaika.com)
