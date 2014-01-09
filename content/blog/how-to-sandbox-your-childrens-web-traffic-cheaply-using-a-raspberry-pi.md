Title: Child Safety: How to sandbox your children's web traffic cheaply using a Raspberry Pi
Date: 2013-08-23 15:55
Category: blog
Tags: raspberry-pi, router
Slug: how-to-sandbox-your-childrens-web-traffic-cheaply-using-a-raspberry-pi
Author: William Culver
Summary: There is no need for ISP level filtering, we have the tech already.

## Forget the rubbish (ISP Porn Block) proposal put forward by our P.M.!  You can create a cheaper, more robust, secure and granular solution for less than £30.00 (+ some network equipment you may or may not have)

[<img class="size-medium wp-image-343" alt="Picture of a Raspberry Pi" src="/static/img/1024px-Raspberry_Pi_Photo2-300x221.jpg" width="300" height="221" />][1] You can pick up one of these for under £30

Heavy Disclaimer Although the Raspberry Pi described here is super cheap, you will have to have some slightly specialized network equipment to do this.  In particular you will need a VLAN aware network switch and a VLAN aware Wifi Access Point at a minimum.  These used to be costly but are getting cheaper.  I HIGHLY recommend the:

*   [Ubiquiti UniFi UAP Indoor Scalable WiFi Access Point ][2]- around £50.00
*   [Ubiquiti TOUGHSwitch][3] 5-Port PoE Switch- around £90.00 I have fallen in love with Ubiquiti network products.  They offer you the power of a corporate network for home user cost.

> Q: OK so what exactly is this thing and what can I do with it?

A: Quite simply you will have absolute control of your kids' network traffic while at the same time enjoying complete freedom of your own.  It will be like having two separate internet connections to your home and you can say goodbye to slow downs whenever your kids are on you tube.

**It allows you to do many cool things such as:**

*   Schedule access times for your children's internet.
*   Set up a transparent porn/ content filter for your kids internet.
*   Log & capture your childrens network traffic.
*   Monitor speeds & bandwidth usage and set caps on data.
*   Separate the rest of your network from your kids (protecting your home office etc)
*   Block certain sites, filter adverts, and many more things!

**All this can be done with free, libre, open source software and a cheap raspberry pi computer that you can get for under £30.00!**

### My rough network topology

[<img class=" wp-image-344 " alt="My network topology.  We are only interested in the left hand side." src="/static/img/topology-rasp-child-filter.png" width="629" height="820" />][4]

 My network topology. We are only interested in the left hand side.[/caption] Note the left hand side of the above diagram and in particular the dashed blue line.  This represents your children's wireless network connection to the internet.  Basically what we will be creating is known as a 'One Armed Router'.  It's a router with only a single network port, yet it is able to capture traffic at the hardware level using the power of VLANs , and then change the traffic before spitting it out again.  This happens in both directions effectively creating a sandbox.  VLANs are used by ISP's and enterprises; they are a way to have two or more networks sharing the same physical wires. The white circular object shown above is the Ubiquiti Unifi Wifi access point I described above.  It allows you to create multiple separate wifi connections which is key because you can have a separate password for each and then give your kids their own wifi connection.  All their traffic becomes the blue dashed line shown above and is sent to the Raspberry Pi by the switch yet your own green traffic passes freely through.  You can even have your wifi connection completely hidden so that only the sandboxed connection shows up, this is also great for guests & strangers who want to use your internet because all your green network including your LAN (in my case) is completely separated


> Q: OK I'm ready to do this. How do we get started? A: First of all you will need the following:-

*   A Raspberry Pi (case optional)
*   A spare SD card (at least 4GB)
*   About 90mins of time (+ some download time)
*   Some VLAN capable network hardware.  (Check your router/network gear.  Admittedly at the time of writing these are fairly rare, especially as most people stick with the BT Home Hub/router that your ISP has provided which mostly suck.  If you don't have these things then please scroll to the bottom where I will try to convince you to invest in some top gear and if you live in the south east of england I will even come and install it for you.  Just head over to my business website https://www.onebytetoomany.co.uk )

1)  Install Arch Linux onto the SD Card Instructions for this can be found here :- <http://archlinuxarm.org/platforms/armv6/raspberry-pi>

2) Boot up and Log in to your Raspberry Pi as root, either physically or via SSH. (If you use windows you can download a tool called PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/> )

3) Set up your raspberry pi for VLAN.

	$ cd /etc/netctl
	$ cp examples/vlan-static .
	$ cp examples/ethernet-dhcp .
	$ (vi or nano) vlan-static

	# [edit the file to look like this ]
	Description='Virtual LAN 32 on interface eth0'
	Interface=eth0.32
	Connection=vlan
	BindsToInterfaces=eth0
	VLANID=32
	Address="10.13.37.1/24"
	Gateway="10.13.37.1"
	DNS=("10.13.37.1")
	ExecUpPost=("route del default dev eth0.32")
	Hostname="RpisRCool"

	$ (vi or nano) ethernet-dhcp
	# [edit the file to look like this ]
	Description='A basic dhcp ethernet connection'
	Interface=eth0
	Connection=ethernet
	IP=dhcp

	$ netctl enable ethernet-dhcp
	$ netctl enable vlan-static

	$ netctl start ethernet-dhcp
	$ netctl start vlan-static

4) Enable forwarding of packets between the two virtual network cards we just set up on the Pi

    $ echo net.ipv4.ip_forward = 1 &gt;&gt; /etc/sysctl.conf
    $ echo 1 >> /proc/sys/net/ipv4/ip_forward # so we don't have to restart.

5) Set up the iptables firewall to act as a Network Address Translation (NAT) router between the two virtual network cards.

    $ cd
    $ touch onearm.sh
    $ vi onearm.sh
	# [make a file like this (we can expand it later but for now this will do]
	ETH="eth0.32"
	WAN="eth0"
	SUBNET_LOCAL="10.13.37.0/24"

	function clean {
	iptables -F
	iptables -t nat -F
	}

	function onearm {
	iptables -t nat -A POSTROUTING -o $WAN -j MASQUERADE
	}

	clean
	onearm

    # [EXIT & SAVE the file ]
    :wq (for vi)

    $ ./onearm.sh # run our script
    $ iptables-save > /etc/iptables/iptables.rules

6) Set up your hardware to VLAN tag the port your Pi is plugged into as VLAN ID = 32.

Refer to your manual.  If you are using a Ubiquiti Toughswitch then you simply log into the switch, go to the VLANs tab and set the port to 'T' and the VLAN ID to 32 or whatever you chose your VLAN ID to be.

7) Set up your Wifi access point  and create a separate SSID & Network on VLAN 32 (or whatever you chose as your tag).


On the Ubiquiti Unifi this can be done through the management interface, simply create a network and set it's VLAN ID to be the same.  Make sure the port on the switch is similarly set up as the Pi with tag enabled on the port.


8) Enable a DHCP Server on your VLAN'd Raspberry Pi interface so that the kids get given an IP address from their sandboxed network (10.37.37.0).

	$ vi /etc/dnsmasq.conf

	interface=eth0.32
	domain=somedomainofmychoosing.local,10.37.37.0/24
	dhcp-range=10.13.37.30,10.13.37.60,12h
	:wq

	$ systemctl enable dnsmasq
	$ systemctl start dnsmasq

Thats it!.  You now have a sandboxed connection running through a separate network (10.13.37) and your kids have their own network on 10.13.37.0 which gets 'N.A.T.'ted through the Raspberry Pi onto the normal network which then gets N.A.T.ted again and out onto the public internet.  Double firewall.

*Drop me a mention on twitter @cedeon if you need any help!.*

Now you have the basic functionality set up you can do lots of cool things with it.  I'll leave it up to your imagination but here are a few ideas:

*   Set up a cron job to turn off eth0.32 at night and then turn it back on again in the morning.
*   Install a traffic analysis tool like IPTraf ( <http://iptraf.seul.org/> ) and have a look at whats going on with your kids online.
*   Install a content filter like safesquid / OpenDNS / squidguard
*   Install 'snort' intrusion tool
*   Make some advanced firewall rules & traffic shaping rules.

* * *

> Q: I've looked into doing something similar before but lots of people say that the Raspberry Pi is useless and too slow to be a router, besides don't I have to get a second network adapter for it?

A: No and No!  The raspberry pi is absolutely perfect for this because it has more than adequate speed to handle current broadband internet speeds that your kids require.  My set up doesn't use a second network adapter (normally you need a second USB NIC plugged in to the Pi) There is a USB/Network bottleneck on the Raspberry pi which my version avoids and you will easily get upto 40Mbit/s throughput.  The other beautiful thing about the network design is that any slow downs at all will have no affect on the rest of the network.  Furthermore you will usually *want* your kids' traffic to be slowed down a bit so that you can maintain a high quality of service on your own internet traffic so this is another reason why a raspberry pi works here.


> Q: You suck, your title says cheap but then your solution relies on enterprise grade network equipment and VLAN tagging!

A:  I'm sorry this is true.  I wish it was as simple as plugging a raspberry pi into a BT Home hub.  If home routers were better then it would be this simple but that is not the case.  There are ways of doing the same thing with a Pi with an extra Network port (NIC) or a device which has two NICs but I haven't gone into that here. Like hi-fi separates, you do get lots of benefits to buying a separate network switch and wifi access point like the Ubiquity ones I have mentioned at the top of the post.  You get the following benefits:

*   You can have a completely separate network & even a publicly accessible network running simultaneously
*   You can reposition your Wifi access point separately from your ADSL or Cable modem and put it more centrally in the house.
*   You get various security benefits and can do advanced security things such as creating black holes, honey pots etc.
*   You get network level virus separation and compartmentalization so that if your kids do silly things and get themselves hacked, the rest of the computers on your network are unaffected.

 [1]: /static/img/1024px-Raspberry_Pi_Photo2.jpg
 [2]: http://www.ubnt.com/unifi
 [3]: http://www.ubnt.com/airmax#toughswitch
 [4]: /static/img/topology-rasp-child-filter.png
