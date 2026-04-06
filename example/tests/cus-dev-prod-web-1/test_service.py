import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_dnsmasq_service_running_and_enabled(host):
    service = host.service("dnsmasq")
    assert service.is_running
    assert service.is_enabled
