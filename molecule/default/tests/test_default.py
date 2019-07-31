import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fail2ban_running(host):
    # NOTE: I cannot use host.service because of problems running sysv/sysctrl
    # on docker. Too difficult! So I fallback on a much easier `ps aux` test.
    # This won't test that the service is started on boot,
    # but.... that's the best we can get now :)
    process = host.process.get(user='root', comm='fail2ban-server')
    assert process is not None


def test_sshd_port(host):
    assert host.socket("tcp://0.0.0.0:6666").is_listening
    assert not host.socket("tcp://0.0.0.0:22").is_listening
