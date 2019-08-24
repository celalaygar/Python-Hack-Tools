import subprocess
import optparse

# write commands on terminal
# python MyMacChanger.py -i eth0 -m 33:22:44:21:3a:4c
# python MyMacChanger.py --interface  eth0 --mac 44:22:54:21:2a:11


parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")
parse_object.add_option("-m", "--mac", dest="mac_adress", help="new mac adress")

(user_inputs, arguments) = parse_object.parse_args()

# print(parse_object.parse_args())       # show values of -i and -m
# print(user_inputs)                     # show values of -i and -m
# print(user_inputs.interface)           # show values of -i
# print(user_inputs.mac_adress)          # show values of -m

print("My Mac changer started!")

subprocess.call(["ifconfig",user_inputs.interface,"down"])
subprocess.call(["ifconfig",user_inputs.interface,"hw","ether",user_inputs.mac_adress])
subprocess.call(["ifconfig",user_inputs.interface,"up"])

print("My Mac changer finished!")
print("------------------------------------")
subprocess.call(["ifconfig"])

