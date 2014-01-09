Title: Basic Linux Sysadmin: Untangling Linux Log Files
Date: 2013-07-12 10:20
Category: blog
Tags: linux, arch linux, sysadmin
Slug: basic-linux-sysadmin-untangling-linux-log-files
Author: William Culver
Summary: All about /var/log/

**Note & TL;DR:**  This post mainly relates to the new Systemd journal style logs and not the traditional text based logs.  Note the Arch Linux logo to the left :), if you are running Debian then this probably won't apply to you until 2050 :p (if ever if the Upstart folks have their way).

## Introduction

I've been a Linux user for over a decade now, and I would say it has been my primary go to desktop OS for more than half of that time.  I spend a lot of my day on the command line and I believe I would be pidgeon-holed well into 'Advanced User' territory.  Still, not a day goes by where I don't learn something new about Unix based systems, which is great.   One of my most avoided areas of Linux research has always been the syslog.  This is due to few reasons, firstly it's always looked 'hacky' to me and not fun at all.  Maybe some people love 'grepping' and 'catting' and mixing weird and wonderful awk and sed pipelines together, not me.  Personally I find it uncomfortable, probably because for some reason my brain is incapable of retaining knowledge about string formatting and regular expressions- I don't know why because I'm perfectly fine with absorbing numerous programming languages.  I seem to get a feeling of dyslexia wash over me as soon as I see too many symbols without ample white space and line breaks in between.  The second reason I've avoided the dreaded syslog up until now is simply because I've never had a need to.  I've always taken a clumsy approach to system administration- if it doesn't work simply take a proverbial sledgehammer to the PC and have a do-over :).  This has worked fine for me in the past because I have no one to answer to and I can manage my systems however I please.  This is all due to change soon with the launch of my new business

[One Byte Too Many][1].  Time to learn me some syslog!.

## Diving into some logs.

> Disclaimer:  I'm going to write this chronologically, in the order that I discovered certain things.  This may not be compatible with other brains!  If so I apologize for that.

### 1. utmp,wtmp,btmp have always annoyed me.. wtf are these!?

I remember blindly running cat on these files and having them smear crap all over my prompt.  Weirdly up until now I've never bothered to find out what they are.  It turns out they are actually quite simple binaries that log user log-ons and log offs. They can all be accessed with the 'last' command like this:

	last -f /var/log/wtmp

also the 'who' command uses these files and is particularly useful.   If you want to find out more about who and are as nerdy as me you could run :-

	alias doctor="man" && doctor who

Sorry, I couldn't resist.

### 2. Moar login logs? srious!?

Yes next we have **lastlog** and **faillog**.  Both have respective command line tools.

**Lastlog** is quite simple and the command lists all the users on your system and besides them puts the a timestamp of the last successful log in  as well as which tty/pts port and also a nice reverse dns if you logged in over ssh. The other important thing to note about lastlog is that it looks a lot more juicy than it actually is because of it's size. It is a <a class="ext" title="">sparse file</a> and as such will not tend to change in size.  This concept threw me a little because on the face of it it looks like its filled with juicy log data.

**Faillog** is a bit of a wierd one.  To quote the opening line of the man page:

> "faillog displays the contents of the failure log database (/var/log/faillog). It can also set the failure counters and limits."

So it seems that the userspace tool is a kind of hybrid log viewer and settings manager.  Naturally the userspace tool is the same as the filename 'faillog'.

### 3. Journalctl

This is worthy of an entire blog post by itself.  It's a beast that I havn't as yet been able to tame.  I normally just use

	journalctl -xn 20

Which gives me the last 20 lines of log files in a descriptive manner.   Also:

	systemctl status [service name]

will give you the tail logs of the specific systemd service. You can also do

	journalctl /name/of/bin/executable

and that will show you what you expect to see.

### An aside

I hope you are with me when I say that linux syslogs are a real mess and not at all intuitive.  In its present state we have a whole range of logging styles in the same folder from plaintext files with no .log extension, plaintext files with a .log extension, binary files mixed in the same folder, plaintext files in subfolders, rotated and gzipped files in subfolders and base folder.  Its a hodgepodge of mayhem that looks like it was designed by sadists.  I personally think Lennart Poettering's hugely criticised journalctl work is the right idea but unfortunately its one of those 1 steps back for 2 forward manoeuvres that we now have to struggle to get through in the meantime.  This interim period of having half binary, half plaintext is not easy on my brain and every time I type 'man journalctl' I want to take my shovel and thrust it towards my own face.  I mean sure.. i guess its intuitive if you precisely know what you want to search for and know systemd like the back of your hand but its in no way nice at first glance.  If I get enough feedback i'll troll through and do a proper write up on it.

 [1]: http://www.onebytetoomany.co.uk/ "One Byte Too Many Web Site"
