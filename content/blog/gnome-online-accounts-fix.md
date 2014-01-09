Title: Gnome: Arch Linux: Gnome Online Accounts (GOA) Not Working
Date: 2013-12-02 10:20
Category: blog
Tags: linux, arch linux, gnome
Slug: gnome-arch-linux-gnome-online-accounts-goa-not-working
Author: William Culver
Summary: A minor fix for GOA in Gnome 3.10

So the GOA add new account button suddenly didn't work after I upgraded to Gnome 3.10.

I note this fix but it doesn't work for me. https://bbs.archlinux.org/viewtopic.php?id=170965

I've been looking long and hard for a fix for this.  I will update as soon as I find it.

Update: Solved it.

    pacman -S gvfs-goa


I filed a bug report, seems this is now a dependency.
