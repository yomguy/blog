Title: M-Audio Fast Track Pro and Quattro special features now enabled for Linux
Date: 2011-07-14 7:33
Category: Linux
Tags: pelican, publishing
Slug: m-audio-fast-track-pro-special-features-now-enabled-linux
Author: Guillaume Pellerin
Summary: M-Audio Fast Track Pro and Quattro special features now enabled for Linux


A few month ago, I was looking for a 24 bits driver for the Fast Track Pro included in the [TC-202](http://parisson.com/products/tc-202-case-1/).

I found a patch for the 2.6.31 kernel on [Joe Giampaoli's blog](http://joegiampaoli.blogspot.com/2011/06/m-audio-fast-track-pro-for-debian-linux.html)  which were written first by Pavel Polischouk. It added some quirks to the snd-usb-audio driver enabling 24 bits, 96 kHz and other special features for the FTP. Then, I adapted it for 2.6.33 RT and [published it](http://files.parisson.com/debian/usbaudio-ftp-2.6.33.7-yomguy.patch).

Now that the kernel 2.6.39 includes almost all of the realtime functions - like threaded IRQs for example - I decided to produce the same patch for it. Not trivial for me because I'm not really a C developer and the driver architecture had been changed. But it just works now...

After some mail exchanges with interested people and beta testing, I'm very happy to [release this patch](http://files.parisson.com/debian/snd-usb-audio-FTP-2.6.39-yomguy-04.patch). You just need to apply it the 2.6.39 sources but NO RT patch anymore and compile the kernel. Don't forget to add "threadirqs" to the kernel boot arguments, for example adding it to the grub conf.

On Debian, editing /etc/default/grub :

```
GRUB_CMDLINE_LINUX="threadirqs"
```

and then :

```
$ sudo update-grub
```

Special configurations can be then loaded through a modprobe conf file. For example, to set the 24 bits mode on the Fast Track Pro plus digital inputs and outputs, add this to /etc/modprobe.d/fast-track-pro.conf :

```
options snd_usb_audio   vid=0x763 pid=0x2012 device_setup=0xB enable=1
```

Here is a list of the possibilities in [this example](http://files.parisson.com/debian/fast-track-pro.conf).

Don't forget to comment out other snd-usb-audio entries in ? /etc/modprobe.d/alsa-base.conf

Thanks a LOT to Takashi Iwai, the patch has been [applied to the sound kernel branch](http://git.kernel.org/?p=linux/kernel/git/tiwai/sound-2.6.git;a=commitdiff;h=0f5733b0c883158b13366ae34b5e4bd52a1ac346;hp=3101ba035ca9ba92f6cec7fd37348646b7a5cb61) and [merged](http://git.kernel.org/?p=linux/kernel/git/tiwai/sound-2.6.git;a=commitdiff;h=02e5fbf622aabf68bdc02282a17a3aeed054237a) . It will be added to Linux 3.1 !

Enjoy ;)
