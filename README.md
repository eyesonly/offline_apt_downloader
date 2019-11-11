# offline_apt_downloader
Download `apt-upgrade` files for use on another Debian/Ubuntu machine

Sometimes you have a Debian or Ubuntu machine connected via a slow or expensive internet connection and need to apply updates.

If you have another machine with good internet access that you can use to download the updates required using the script here.

## Process for download .deb archives for another machine:

With the script here, you can still call `apt update` with special parameters so that you get a list of updates required, then you can run this script on another host with suitable internet access to actually fetch and verify the .deb files. Afterwards, by whatever means (e.g. flash disk) you can copy the .deb files directly onto the host that needs to be updated.

1.  On the host with poor internet access, run apt-update with the following additional flags.
```
sudo apt-get upgrade -qq --reinstall --print-uris > deblist.txt
```

If you take a look at this file, it should have lines that look like this:
```
```
Note each line has the UIL of a file to download, as well as the checksum and file size of the file.

2.  Copy the deblist.txt file to the machine with the better internet accoess

3.  Run the script from this package on that machine to perform the downloads. The script will check md5 and file sizes:
```
python_apt_retrieve.py deblist.txt
```

4. Copy all the .deb files download into the /var/cache/apt/archives/ folder on the machine that needs to be updated.

5. Run
```
sudo apt-get upgrade
```
on that machine
