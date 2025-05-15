from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task4.j2")

class NetworkInterface(object):
    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan

# Prepare the list of interface objects
interfaces = []
for i in range(1, 11):
    description = f"Server Port {i}"
    vlan = 10 + i
    interfaces.append(NetworkInterface(description, vlan))

interface_obj = NetworkInterface("GigabitEthernet0/1", 10)
print(template.render(interface=interface_obj))
