# junos_load_logical_system_topology

-> What is it
 - Maximizing the advantage of python/PY-EZ, this super user friendly tool helps anyone to build an end-to-end network topology with junos builtin logical-system / logical-tunnel for lots of scenarios 
 - Within minutes of time, building a semi-virtual topology from scratch on a single physical Junos device (MX preferred) provides a solid alternative way to physical or virtual topologies 


-> How to use it 
 - Reserve any Junos device anywhere and have the login information handy 
 - Cleanup the configuration on the device. The tool doesn't do configuration cleanup intelligently 
 - Copy the python script and archived configuration files under the same folder
 - Run the script. Users need only to specify hostname/IP, login, password and select the scenario they'd like to build 
 - The script does basic verification and inform user when the setup is ready to go 
 - The script archives the configuration locally on the router 


-> Target users
 - JTAC or Juniper Partner or customer or anyone who would like to build a junos network topology for lab replication or study or certification purpose 


-> Beta version supported scenarios:
 - OSPF multi-area
 - ISIS level 1 & 2 
 - BGP 
	- EBGP 
	- IGBP with Route Reflector 
 - VRRP
 - MPLS core traffic-engineering 
	- L3VPN
	- L2VPN L2CIRCUIT VPLS 
 - Multicast PIM Sparse Mode 
 - Multicast VPN (MVPN) Draft Rosen
 - Multicast VPN (MVPN) Next Generation


-> Pros
 - No physical connection needed in most use cases 
 - Minimum junos and hardware dependencies 
 - Instead of spending more time to get the baseline setup ready, this tool gets you a working baseline setup in minutes. You can spend more time digging into the real issue
 - No license needed 
 - Scalale. If anyone has any use cases to add, it can be simply added 


-> Cons 
 - All limitations of logical-system applies 
   https://www.juniper.net/documentation/en_US/junos/topics/topic-map/security-logical-systems-for-routers-and-switches.html#id-logical-systems-operations-and-restrictions
 - Slowness in CPU constraint platforms, eg MX80 

-> Future plan
 - Improve code based on feedback
 - Add more scenarios, eg EVPN MPLS single homing, EVPN VXLAN single homing 


