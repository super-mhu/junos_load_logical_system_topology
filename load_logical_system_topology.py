import argparse
import sys
from jnpr.junos import Device 
from jnpr.junos.utils.config import Config 

##parse arguments 
parser = argparse.ArgumentParser()
parser.add_argument('ip', type=str,help="IP address of the target device")
parser.add_argument('username', type=str,help="Username of the target device")
parser.add_argument('password', type=str,help="Password of the target device")
parser.add_argument('topology', type=int, choices=[1,2,3,4,5,6,7,8],help='Select the topology index: '
                                                                       '\n1.ospf_multi_area. \n'
                                                                       '\n2.isis.\n'
                                                                       '\n3.bgp_with_rr_config\n'
                                                                       '\n4.vrrp.. \n'
                                                                       '\n5.mpls_core.. \n'
                                                                       '\n6.mcast_pim.\n'
                                                                       '\n7.mcast_mvpn_draft_rosen.\n'
                                                                       '\n8.mcast_mvpn_ng.\n')

args=parser.parse_args()

##assign arguments 
ipaddr=args.ip
uname=args.username
passwd=args.password
topo=args.topology

print(f"\nThe target device is {ipaddr}, username/password is {uname}/{uname}...\n")

topo_inventory = {1:'1_ospf_multi_area.txt',2:'2_isis_level_12.txt',3:'3_bgp_with_rr_config.txt',4:'4_vrrp.txt',5:'5_mpls_core.txt',6:'6_mcast_pim.txt',7:'7_mcast_mvpn_draft_rosen.txt',8:'8_mcast_mvpn_ng.txt'}
print(f"The selected topology is {topo_inventory[topo]}...\n")

print("Loading parameters...\n")

##connect to device 
try:
	dev=Device(host=ipaddr,user=uname,passwd=passwd)
	dev.open()
except Exception:
	print("Connetion issue, couldn't connect to device...\n") 
	sys.exit() 

print("connected to device...\n")

##load config to device
try:
	with Config(dev) as cu:
		cu.load('delete logical-systems', format='set', ignore_warning='statement not found')
		cu.load(path=topo_inventory[topo], merge='False')
		if cu.commit_check():
			cu.commit(timeout='60')
		else:
			raise Exception('Commit failed!')
except Exception as err:
	print(err.args)
	print("Exiting due to configuation issue. Please check existsing configuation on the router")
	sys.exit()

dev.close() 

print("config loading done...\n")

##print additional instructions 
print("printing instructions...\n")
print("**************************************************************************************************************************************")
with open('0_instruction.txt', 'r') as f:
	lines = f.readlines()
	print_line=False
	count=0
	for line in lines:
		if topo_inventory[topo].split('.')[0] in line:
			print_line=True 
		if '******' in line and print_line:
			count +=1
		if count == 2:
			print_line=False
		if print_line:
			print(line,end='')



