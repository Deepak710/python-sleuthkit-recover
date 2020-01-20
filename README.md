# python-sleuthkit-recover

## Linux command line thumbstick file recovery script using SleuthKit

### Features
1. Recover accidentaly deleted files from your thumbstick
1. Choose which files to recover

### What won't work
1. Recover files from unallocated [or] deleted partitions

### To Run this file,
1. Make sure [SleuthKit](https://www.sleuthkit.org/sleuthkit/download.php "SleuthKit download page") and [Python 3.x](https://www.python.org/downloads/ "Python download page") is installed
1. [Clone](https://github.com/Deepak710/python-sleuthkit-recover.git)/[Download](https://github.com/Deepak710/python-sleuthkit-recover/archive/master.zip) this repo
1. Run the recover.py script
    ```cmd
      python3 recover.py
    ```
1. Select the partition with the deleted file using the corresponding number
1. Give a name for the temporary image of the partiton that will be created. This file will be as large as the partition. THIS PROCESS WILL TAKE TIME. DON'T PANIC!
1. Select the file to recover using the corresponding number

### Versions
* **[0.0a1.dev1](https://github.com/Deepak710/python-sleuthkit-recover/tree/0.0a1.dev1)**
  * Initial Commit
* **[0.1a1.dev1](https://github.com/Deepak710/python-sleuthkit-recover/tree/0.1a1.dev1)**
  * Added NTFS support

Contact Me: [Telegram](https://t.me/AzorAhoy)
