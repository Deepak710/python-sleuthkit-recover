import subprocess as s
import re


def recover(file_type):
    if file_type == 'fuseblk':
        c = s.Popen('fls -f ntfs ' + f + ' | grep -e "r" | grep -e "*"', stdout=s.PIPE,
                    shell=True).stdout.read().decode('utf-8').splitlines()
    else:
        c = s.Popen('fls ' + f + ' | grep -e "r" | grep -e "*"', stdout=s.PIPE,
                    shell=True).stdout.read().decode('utf-8').splitlines()
    for i in c:
        l = list()
        l.append(i[(i.find('*'))+1:i.find(':')].strip())
        l.append(i[(i.find(':\t'))+1:].strip())
        files.append(l)
    if not files:
        s.Popen('rm -f ' + f, stdout=s.PIPE, shell=True)
        print('No recoverable files in this partition. Sorry!')
        exit()
    else:
        while(True):
            for i in range(1, len(files) + 1):
                print(str(i) + '\t' + files[i-1][1])
            c = int(input('Enter file to recover : '))
            if c not in range(1, len(files) + 1):
                print('Enter correct file number')
                break
            else:
                if file_type == 'fuseblk':
                    print(s.Popen('istat -f ntfs ' + f + ' ' +
                                  files[c-1][0], stdout=s.PIPE, shell=True).stdout.read().decode('utf-8'))
                    s.Popen('icat -f ntfs ' + f + ' ' +
                            files[c-1][0] + " > ./'" + files[c-1][1] + "'", stdout=s.PIPE, shell=True)
                else:
                    print(s.Popen('istat ' + f + ' ' +
                                  files[c-1][0], stdout=s.PIPE, shell=True).stdout.read().decode('utf-8'))
                    s.Popen('icat ' + f + ' ' +
                            files[c-1][0] + " > ./'" + files[c-1][1] + "'", stdout=s.PIPE, shell=True)
                c = input(
                    'Continue recovering files from this partition? ')
                if c.lower() == 'n':
                    c = s.Popen(
                        'rm -f ' + f, stdout=s.PIPE, shell=True)
                    break


while(True):
    x = s.Popen('mount | grep -e "/media/"', stdout=s.PIPE,
                shell=True).stdout.read().decode('utf-8').splitlines()
    if not x:
        print("No partitions. Make sure the thumbdrive is mounted properly!")
        exit()
    else:
        w = s.Popen('whoami', stdout=s.PIPE,
                    shell=True).stdout.read().decode('ascii').strip()
        l, drives = list(), list()
        for i in x:
            l = i.split()
            if l[2] != i[i.find('/media/'):i.find(' type')]:
                l[2] = i[i.find('/media/'):i.find(' type')]
                del l[3]
            drives.append(l)
        print('List of Partitions\n____ __ __________\n')
        for i in range(1, len(drives) + 1):
            print(str(i) + '\t' + re.sub('/media/' +
                                         w + '/', '', drives[i-1][2]))

        c = int(input('Enter partition number to examine\t: '))
        if c not in range(1, len(drives) + 1):
            print('Enter correct partition number')
            break
        else:
            f = input('Enter temporary image name\t\t: ')
            s.Popen('umount ' + drives[c-1][0], stdout=s.PIPE, shell=True)
            p = s.Popen('sudo dd if=' + drives[c-1][0] + ' of=' +
                        f, stdin=s.PIPE, stdout=s.PIPE, shell=True)
            p.communicate()
            files = list()

            recover(drives[c-1][4])

    c = input('Continue recovering from other partitions? ')
    if c.lower() == 'n':
        exit()
