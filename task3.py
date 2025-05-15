from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-task3.j2")

class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interfaces = []
for i in range(1, 11):
    name = f"GigabitEthernet0/{i}"
    description = f"Server Port {i}"
    vlan = 10
    interfaces.append(NetworkInterface(name, description, vlan))

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)
print(template.render(interface=interface_obj))
