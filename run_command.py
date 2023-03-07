from nornir.core import InitNornir
from nornir.plugins.tasks import commands
from nornir.plugins.functions.text import print_result

nr = InitNornir(
    num_worker=100,
    inventory="nornir.plugins.inventory.simple.SimpleInventory"
    SimpleInventory={
        "host_file": "hosts.yml",
        "group_file": "groups.yml"
    }
)

commandToRun = input("Enter command to run: ")

result = nr.run(task=commands.remote_command, command=commandToRun)
print_result(result, vars=["stdout"]
)