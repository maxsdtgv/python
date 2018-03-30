import os, sys

path = "/dev/ttyuu"


info = os.lstat(path)


major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print "Major:", major_dnum
print "Minor:", minor_dnum


dev_num = os.makedev(major_dnum, minor_dnum)
print "nnn:", dev_num