Title: Linux: Preventing ‘No Caching mode page present’ errors from showing up on boot.
Date: 2012-12-09 10:00
Category: blog
Tags: linux, arch linux, boot
Slug: linux-preventing-no-caching-mode-page-present-errors-from-showing-up-on-boot
Author: William Culver
Summary: A look into how to remove those pesky boot messages that you don't care about.

I had a problem (minor annoyance) when booting up Arch linux with a USB drive connected.  The problem was, upon boot I was receiving the following messy output to the console:

	[sdb] No Caching mode page present
	[sdb] Assuming drive cache: write through

Rather than being hidden and showing up only on dmesg, these messages were obnoxiously appearing on my prompt screen and would mess up the look of the login.

If you get the same problem and would like to prevent this from happening, simply add

	loglevel=2


to your kernel boot parameters ( i.e. vi /etc/default/grub )


### Further information can be found here:

http://ubuntuforums.org/showpost.php?p=4950734&postcount=3

Hope this helps :)
