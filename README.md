# dnsmasq Ansible Role (ansible-role-dnsmasq) from Blunix GmbH

This Ansible role installs and configures `dnsmasq` as a local DNS forwarder on Debian hosts.

The Ansible Role is written and actively maintained by <a href="https://www.blunix.com" target="_blank">Blunix GmbH</a>.
It is used in the Blunix <a href="https://www.blunix.com/linux-managed-hosting.html" target="_blank">Linux Managed Hosting</a> Stack.
Its usage is documented at our <a href="https://www.blunix.com/manual" target="_blank">Linux Managed Hosting Documentation</a>.


## Features

- Installs `dnsmasq`.
- Removes `dnscrypt-proxy` if present.
- Manages `/etc/dnsmasq.d/99-ansible.conf` with upstream resolvers from `dnsmasq_dns_servers`.
- Adds a cleanup cron job for `/etc/resolv.conf.dhclient-new.*` temp files.


## Requirements

- Ansible: **>= 2.20.0**
- Managed operating systems:
  - Debian **trixie**


## Role variables and example playbook

Role variable:

- `dnsmasq_dns_servers`: upstream DNS resolver list used to render `server=` lines in `/etc/dnsmasq.d/99-ansible.conf`.
  - default:
    - `9.9.9.9`
    - `8.8.8.8`
  - example mapping used in this role's `example/inventory/group_vars/all/dnsmasq.yml`:
    - `dnsmasq_dns_servers: "{{ dns_servers_hosting_provider }}"`

Example playbook:

```yaml
# Apply dnsmasq role to all hosts in the inventory.
- name: setup dnsmasq
  hosts: all
  roles:
    - role: ansible-role-dnsmasq
```


## Infra as code tests

- Playbook: `example/play.yml` applies the role to the test host group.
- Inventory vars: `example/inventory/group_vars/all/dnsmasq.yml` maps role variable `dnsmasq_dns_servers` to `dns_servers_hosting_provider`.
- Provider vars: `example/inventory/group_vars/hcloud.yml` provides `dns_servers_hosting_provider`.
- Tests in `example/tests/cus-dev-prod-web-1/`:
  - `test_package.py` checks package install/remove state.
  - `test_service.py` checks service state.
  - `test_config_file.py` checks rendered dnsmasq config ownership, mode, and resolver lines.
  - `test_listener.py` checks DNS listeners on port `53`.
  - `test_cron.py` checks the resolv.conf temp-file cleanup cron entry.


## Author Information

Blunix GmbH Berlin

`root@Linux:~# Support | Consulting | Hosting | Training`

Blunix GmbH provides 24/7/365 Linux emergency support and consulting, Service Level Agreements for Debian Linux managed hosting using Ansible Configuration Management as well as Linux trainings and workshops.

Learn more at <a href="https://www.blunix.com" target="_blank">https://www.blunix.com</a>.

## Contact Information

Click here to see our <a href="https://www.blunix.com/#contact" target="_blank">Contact Information</a>.

For bug reports and feature requests, please open an issue in this repository’s GitHub issue tracker.


## License

Apache-2.0

Please refer to the `LICENSE` file in the root of this repository.
