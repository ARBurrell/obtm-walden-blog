Slug: xbmc-certain-files-play-fast-with-no-sound.md
Title: XBMC: Certain files play fast with no sound (AC3 audio codec with pulseaudio passthrough)
Date: 2014-01-09 14:18
Category: blog
Tags: linux, arch linux, gnome
Author: William Culver
Summary: A fix for double speed playing of certain files in XBMC.

I was having an issue with certain media files which would play double speed with no sound.  After much searching around it appears that only files with AC3 audio codec were affected.  I confirmed that this was the case for me too.

The problem lies with the 'passthrough' audio device in XBMC.  Mine was set to PulseAudio (default).  After much tweaking around and research it appears that there is some kind of problem with Pulseaudio not passing through the AC3 stream correctly.

### The Fix

This problem was remedied by killing pulseaudio and using the ALSA fallback.

1) Edit /etc/pulse/client.conf

	autospawn = no
	daemon-binary = /usr/bin/true

2) Have a look in the following paths and remove pulseaudio files to prevent autoloading by others.

	/etc/X11/xinit/xinitrc.d/pulseaudio
	/etc/xdg/autostart/pulseaudio.desktop
	/etc/xdg/autostart/pulseaudio-kde.desktop

	~/.config/autostart/pulseaudio.desktop



### References
[Arch Wiki - Always the best source ][1]

------------------------


[1]: https://wiki.archlinux.org/index.php/PulseAudio#Daemon_already_running "Arch Wiki = the best"
