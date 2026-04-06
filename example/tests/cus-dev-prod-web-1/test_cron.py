import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)

CLEANUP_COMMAND = "/usr/bin/rm -f /etc/resolv.conf.dhclient-new.* 2>/dev/null"


def test_resolv_conf_cleanup_cron_job_exists(host):
    root_crontab_file = host.file("/var/spool/cron/crontabs/root")
    if root_crontab_file.exists and CLEANUP_COMMAND in root_crontab_file.content_string:
        return

    system_crontab_file = host.file("/etc/crontab")
    if system_crontab_file.exists and CLEANUP_COMMAND in system_crontab_file.content_string:
        return

    crontab_output = host.check_output("crontab --list || true")
    assert CLEANUP_COMMAND in crontab_output
