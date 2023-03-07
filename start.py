from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

from nornir.core.filter import F

nr = InitNornir(config_file="config.yml")

SW = nr.filter(F(groups__contains="SWS"))

result = SW.run(netmiko_send_command, command_string="sh ip int brief")

print_result(result)