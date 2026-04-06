import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_dnsmasq_config_file(host):
    config_file = host.file("/etc/dnsmasq.d/99-ansible.conf")
    assert config_file.exists
    assert config_file.user == "root"
    assert config_file.group == "root"
    assert config_file.mode == 0o640


def test_dnsmasq_config_contains_inventory_resolvers(host):
    config_file = host.file("/etc/dnsmasq.d/99-ansible.conf")
    config_content = config_file.content_string
    variables = host.ansible.get_variables()
    provider_resolvers = variables.get("dns_servers_hosting_provider", [])

    assert provider_resolvers
    assert "interface=" in config_content
    assert "bind-interfaces" in config_content
    assert "port=53" in config_content
    assert "no-resolv" in config_content

    for provider_resolver in provider_resolvers:
        assert f"server={provider_resolver}" in config_content
