Title: DERP! : Diminished Eavesdrop Raspberry Pi by One Byte Too Many
Date: 2013-07-10 10:20
Category: blog
Tags: raspberry-pi
Slug: derp-diminished-eavesdrop-raspberry-pi
Author: William Culver
Summary: DERP! : Diminished Eavesdrop Raspberry Pi by One Byte Too Many.


![alt text](/static/img/DERP-Photo.jpg "Image of DERP!")

## The Need

Ever since the whistle blower Edward Snowden released chilling information about government spying and collection of massive amounts of our personal data by ‘Five Eyes’ countries (USA, Canada, UK, Australia, and New Zealand)  against our will, a lot of us have felt extremely disheartened by our governments’ actions.  Many of us believe that privacy is not only a fundamental right but also a benefit for all people, not just the ones that have malicious things to hide.  It’s an ironic contradiction that the governments are so opaque about their own surveillance yet feel the people should be of the mindset that if they aren’t doing anything wrong then they have nothing to hide.  According to the actions of our governments we should be content with trading our freedoms for increased national security even when this increased level of national security has not been quantified to us.

Whatever your personal opinions to this recent news are, we still do have constitutional rights to protecting the sanctity of privacy and we also have many technologies and tools to help us achieve this, particularly on computers.  My aim is to lower the cost of entry to these tools by providing easy to use ‘plug & play’ style internet privacy & encryption devices.

Please note: The following is not a one stop ‘Snake Oil’ anonymity solution! Please learn all you can about the technologies that I have used, none of them are one stop solutions.  Nevertheless these technologies can go a long way to help with pulling power back in your own hands and should be treated as one of your many privacy tools.
The Goal

To create a device which helps to mitigate the surveillance capabilities of internet service providers, governments & malicious people in general in order to protect against intrusion of privacy.
The Device

The intention is to build a portable transparent Tor proxy.   To quote Wikipedia, “Tor directs Internet traffic through a free, worldwide volunteer network consisting of more than three thousand relays[6] to conceal a user’s location or usage from anyone conducting network surveillance or traffic analysis“

My device will encapsulate this technology in a black box, easy to use form.

**It will be comprized of the following parts.**

 -   Raspberry Pi Type B.
 -   Black Case
 -   USB Wifi Dongle
 -   SD/Micro SD Card pre-loaded & configured with custom software
 -   (Optional) Ethernet & Power Cables, which complete the prerequisites needed for plug and play.
 -   (Optional) Real Time clock add on.

All parts to be assembled and ready to go out of the box.
### Features

 -   Must be easy to use, portable,  & zero low configuration
 -   Provides a complete Wifi Hardware solution, i.e. can be used as a Wifi dongle.
 -   Device must be completely independently verifiable by using Free and Open Source Software throughout.
 -   Device must fail closed i.e. when Tor fails, no traffic gets through at all. (security feature)
 -   Device must be capable of  updating itself.
 -   I must share all future add ons (shown below) to the project with everyone that owns a device, free of charge.

### Future Goals & add ons.

 -   VPN Connection to this proxy so that it can be placed in a large LAN environment and still JustWork™
 -   Non persistant logging on the Rpi. (Maybe mount var as ramfs, or kill logging completely).  Same for DNS caching.
 -   Html web app front end configuration – for ease.
 -   LXC Containment or DOCKER containers with full merkle tree hash checking for self analysis for the mega paranoid.
 -   Rapid re-provisioning from scratch with provisioning tools like Puppet.  This will provide a complete automatic update solution

## Wait!… This sounds familiar!

Yes this is true :( .Technically Adafruit Industries have created a similar product with their Onion Pi .  I’m claiming prior art as I had a similar idea when I first got my Rpi  *pokes tongue*

Regardless of originality my product differs in the following ways:-

1. Pre-configured out of the box.  My product comes with everything you need pre-installed and ready to use with one command on an SSH terminal.

2. Bespoke open source Tor monitor and set up software.  I have written custom software to set up and monitor the connection with as much ease of use as possible to make this product newbie friendly.

3. Free updates forever.   All my work is in a Git repository and can be provisioned to your box automatically through Puppet.  All of this is open source and as the project evolves you will always be able to pull down the latest updates and features.

4. Network configuration.
My product is set up to be a DHCP server on the ethernet port passing traffic through a firewall to a wifi client on the wifi port.  The Onion Pi is a software wifi access point and SOCKS5 proxy.  My product does not require SOCKS proxy enabled software, nor does it create a wifi hotspot.  My product is designed to be a personal device that you would take with you two a public wifi hotspot and therefore it only allows a single tor connection through the ethernet port.  This is just how it’s setup although all the hardware is the pretty much the same as the Onion Pi so you can certainly run it as a wifi access point if you wish.

If you have any grievances please aim them here. All my work is copyleft or completely free so I hope the work i’ve done on this gets used for greater good elsewhere.


## How it works
### Diagram of the D.E.R.P.

![Diagram of Derp](/static/img/DERP-Diagram.png "DERP Diagram")

This diagram shows how the DERP re-routes internet traffic through it’s transparent Tor Proxy.

The DERP works as follows.  You plug an ethernet cable into the ethernet port and attach the other end to your computer.  The DERP then gives your computer an IP address and sets itself up as a gateway.  Traffic which then comes from your computer via the ethernet port will then pass by the DERP’s internal firewall and get re-routed to ports 9040 and 9053 where the Tor service is waiting and listening.  The tor service then ‘Torify’s’ the data and routes it through the Tor network.  This is all done completely transparently.  You can check your new IP address by visiting a service like http://icanhazip.com or http://icanhazptr.com if you want your reverse DNS.


## I want one.

Thats great!  All the money I raise gets put back into the project and will go towards the development of future features from this list.


