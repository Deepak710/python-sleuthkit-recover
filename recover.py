import subprocess as s
import re

p = s.Popen('lsblk -o NAME,MOUNTPOINT | grep -e "/media/"', stdout=s.PIPE, shell=True)
x = re.sub('[^A-Za-z0-9/ \n]+', '', p.stdout.read().decode('utf-8')).splitlines()

if not x:
    print("No partitions. Make sure the thumbdrive is mounted properly!")
    exit()
else:
    w = s.Popen('whoami', stdout=s.PIPE, shell=True).stdout.read().decode('ascii').strip()
    l, drives = list(), list()
    for i in x:
        l = i.split()
        drives.append(l)

    while(True):
        print('List of Partitions\n____ __ __________\n')
        for i in range(1, len(drives) + 1):
            print(str(i) + '\t' + re.sub('/media/' + w + '/', '', drives[i-1][1]))

        c = int(input('Enter partition number to examine\t: ' ))
        f = input('Enter temporary image name\t: ')
        s.Popen('umount /dev/' + drives[c-1][0], stdout=s.PIPE, shell=True)
        p = s.Popen('sudo dd if=/dev/' + drives[c-1][0] + ' of=' + f, stdin=s.PIPE, stdout=s.PIPE, shell=True)
        p.communicate()
        files = list()
        c = s.Popen('fls ' + f + ' | grep -e "*"', stdout=s.PIPE, shell=True).stdout.read().decode('utf-8').splitlines()
        for i in c:
            l = i.split()
            l[2] = re.sub('[^0-9]+', '', l[2])
            files.append(l)
        
        if not files:
            print('No recoverable files in this partition. Sorry!')
            exit()
        else:
            while(True):
                for i in range(1, len(files) + 1):
                    print(str(i) + '\t' + files[i-1][3])
                c = int(input('Enter file to recover : '))
                print(s.Popen('istat ' + f + ' ' + files[c-1][2], stdout=s.PIPE, shell=True).stdout.read().decode('utf-8'))
                s.Popen('icat ' + f + ' ' + files[c-1][2] + ' > ' + files[c-1][3], stdout=s.PIPE, shell=True)
                c = input('Continue recovering files from this partition? ')
                if c.lower() == 'n':
                    c = s.Popen('rm -f ' + f, stdout=s.PIPE, shell=True)
                    break

        c = input('Continue recovering from other partitions? ')
        if c.lower() == 'n':
            exit()