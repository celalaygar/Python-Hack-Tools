import subprocess
import optparse
import re

# python MyMacChanger.py -i eth0 -m 33:22:44:21:3a:4c
# python MyMacChanger.py --interface  eth0 --mac 44:22:54:21:2a:11

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac :
        return new_mac.group(0)
    else :
        return None

def get_user_parameters():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_adress", help="new mac adress")
    return  parse_object.parse_args()

def change_mac_adress(user_interface, user_mac_adress):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["ifconfig",user_interface,"up"])
    result_mac = control_new_mac(user_interface)
    if(result_mac == user_mac_adress) :
        print("Sueccess !")
    else :
        print("Error !")

print("My Mac changer started!")
(user_inputs, arguments) = get_user_parameters()
change_mac_adress(user_inputs.interface, user_inputs.mac_adress)

# print(parse_object.parse_args())       # show values of -i and -m
# print(user_inputs)                     # show values of -i and -m
# print(user_inputs.interface)           # show values of -i
# print(user_inputs.mac_adress)          # show values of -m

print("My Mac changer finished!")
