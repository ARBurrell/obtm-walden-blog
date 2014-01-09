Title: Gnome: Nautilus: How to hide partitions from the 'devices' area on the left pane
Date: 2013-12-02 17:17
Category: blog
Tags: linux, arch linux, gnome
Slug: gnome-nautilus-how-to-hide-partitions-from-the-devices-area-on-the-left-pane
Author: William Culver
Summary: Hide Windows Partitions and things you just don't care about from Nautilus.

I have a lot of partitions such as windows system partitions that I never use from Linux yet it always annoyed me that they were showing up automatically in nautilus and if I happened to click on them accidentally I would get a mount dialog that I could not cancel.

**Solution** - add udev rules to ignore them and reboot.

Heres a copy of my file, modify yours accordingly...

    % cat /etc/udev/rules.d/99-hide-disks.rules

    ACTION!="add|change", GOTO="hide_partitions_end"
    SUBSYSTEM!="block", GOTO="hide_partitions_end"
    KERNEL=="loop*|ram*", GOTO="hide_partitions_end"

    KERNEL=="sda1", ENV{UDISKS_IGNORE}="1"
    KERNEL=="sda5", ENV{UDISKS_IGNORE}="1"
    KERNEL=="sda6", ENV{UDISKS_IGNORE}="1"
    KERNEL=="sda8", ENV{UDISKS_IGNORE}="1"

    LABEL="hide_partitions_end"
