Title: Arch Linux: Network Manager: Activation failed - fix
Date: 2014-01-28 11:17
Category: blog
Tags: linux, arch linux, gnome, NetworkManager
Slug: arch-linux-networkmanager-activation-failed-fix
Author: William Culver
Summary: I keep getting this error and forget the fix so I'm posting it here for future reference.

I was getting a problem that whenever I activated NetworkManager my ethernet card would drop its ip address.  Doing a `sudo systemctl status NetworkManager` would give me the following output.


	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> Activation (enp3s0) Stage 4 of 5 (IPv6 Configure Timeout) scheduled...
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> Activation (enp3s0) Stage 4 of 5 (IPv6 Configure Timeout) started...
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> (enp3s0): device state change: ip-config -> failed (reason 'ip-config-unavailable') [70 120 5]
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> NetworkManager state is now DISCONNECTED
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> Marking connection 'Wired connection 1' invalid.
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <warn> Activation (enp3s0) failed for connection 'Wired connection 1'
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> Activation (enp3s0) Stage 4 of 5 (IPv6 Configure Timeout) complete.
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> (enp3s0): device state change: failed -> disconnected (reason 'none') [120 30 0]
	Jan 28 11:11:19 desiced.cedeon.local NetworkManager[2317]: <info> (enp3s0): deactivating device (reason 'none') [0]


Not very informative.

After much digging around I finally found the solution.  It seems I had the `dhcpcd.service` enabled.

	`sudo systemctl stop dhcpcd.service`

Fixed the issue. :)

