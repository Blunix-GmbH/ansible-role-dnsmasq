import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_dnsmasq_listens_on_local_port_53(host):
    assert host.socket("tcp://127.0.0.1:53").is_listening
    assert host.socket("udp://127.0.0.1:53").is_listening
