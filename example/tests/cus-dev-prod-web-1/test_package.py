import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_dnsmasq_package_installed(host):
    package = host.package("dnsmasq")
    assert package.is_installed


def test_dnscrypt_proxy_package_removed(host):
    package = host.package("dnscrypt-proxy")
    assert not package.is_installed
