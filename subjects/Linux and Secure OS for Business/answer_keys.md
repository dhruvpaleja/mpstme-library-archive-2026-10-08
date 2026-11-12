# Linux and Secure OS for Business: answer keys

Answer keys and model answers published on the portal, newest first.

## 2025-26 · Final-Exam · Sem 4 · Answer key · paper 72f7662ba697

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Final-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/ANS_Linux and Secure OS for Business(702CO0C069)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 05 May 2026
- Text: text (7 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2025-2026)
Subject: Linux and Secure OS for Business
Date: 05 May 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 7 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question number 1 is compulsory
5. Attempt any 4 from the rest
Q1.
a) Compression Commands (Any 4)   [5M]
gzip
Compresses files → .gz
Command: gzip file.txt
Fast and widely used
gunzip
Decompress .gz files
Command: gunzip file.txt.gz
bzip2
Higher compression than gzip but slower
Command: bzip2 file.txt
bunzip2
Decompress .bz2 files
Command: bunzip2 file.txt.bz2
tar
Archive + compress multiple files
Command:
tar -cvf file.tar dir/
tar -czvf file.tar.gz dir/
********** 1 **********
--- page 2 ---
b) Linux File Systems   [5M]
Common file systems:
ext4
xfs
btrfs
ntfs
Explanation (Any 2):
ext4
Journaling file system
Stable and widely used
Supports large files
Use case: General-purpose Linux systems
xfs
High performance for large files
Excellent for parallel I/O
c)   [5M]
Definition:
Package management is the process of installing, updating, configuring, and removing software
packages in Linux. 2M
Difference 3M
Feature apt   yum/dnf
Used in Debian/Ubuntu RHEL/CentOS/Fedora
Install   apt install pkg yum install pkg
Update apt update   yum update
Remove apt remove pkg yum remove pkg
(d)
[5M]
********** 2 **********
--- page 3 ---
Definition:
ACL (Access Control List) provides fine-grained permissions beyond standard rwx. 2M
Commands: 2M
•   getfacl file.txt → View ACL
•   setfacl -m u:user:rwx file.txt → Set permission
Example: 1M
•   setfacl -m u:john:r file.txt
Q2.   20M
Commands (8M)
mkdir projects
mv file.txt projects/
cp projects/file.txt projects/file_copy.txt
rm projects/file_copy.txt
Explanation (6M)
• mkdir → Creates directory
• mv → Moves file
•   cp → Copies file
• rm → Deletes file
Display & Create File (6M)
cat file.txt
touch newfile.txt
•   cat → Displays content
•   touch → Creates empty file
Q3. Logical Volume Manager (LVM)   20 Marks
LVM Architecture (10M)
Information
Diagram
LVM consists of:
1. Physical Volume (PV)
o Raw disk (e.g., /dev/sda)
2. Volume Group (VG)
o Pool of storage from PVs
3. Logical Volume (LV)
********** 3 **********
--- page 4 ---
o   Virtual partition used like disk
Flow:
PV → VG → LV
Create Snapshot (5M)
lvcreate -L 1G -s -n snap1 /dev/vg1/lv1
Steps:
1. Ensure free space in VG
2. Create snapshot using -s
3. Assign name
Mount & Backup (5M)
mkdir /mnt/snapshot
mount /dev/vg1/snap1 /mnt/snapshot
cp -r /mnt/snapshot /backup/
• Mount snapshot
• Take backup safely
********** 4 **********
--- page 5 ---
Q4. Security Mechanisms   20 Marks
1. SUID (Set User ID)
•   Executes file with owner privileges
chmod u+s script.sh
2. SGID (Set Group ID)
•   Files inherit group ownership
chmod g+s project_dir
3. Sticky Bit
•   Only owner can delete files
chmod +t project_dir
4. ACLs
•   Fine-grained permissions
setfacl -m u:dev1:rwx project_dir
Combined Use Case
• SGID → group sharing
•   Sticky Bit → file protection
• ACL → custom access
• SUID → privileged scripts
Q5.   20 Marks
Troubleshooting Commands (10M)
1. ping
ping google.com
2. traceroute
traceroute google.com
3. netstat
netstat -tuln
4. ss
ss -tuln
5. nslookup
********** 5 **********
--- page 6 ---
nslookup google.com
6. dig
dig google.com
Explanation (5M)
•   ping → connectivity
•   traceroute → path tracking
•   netstat/ss → port status
•   nslookup/dig → DNS check
Solutions (5M)
Issue   Solution
DNS   Fix /etc/resolv.conf
Firewall Allow ports (iptables, ufw)
Routing Check gateway
Q6. Bash Scripting   20 Marks
Shell Script (10M)
#!/bin/bash
# CPU Monitoring Script
echo "Enter CPU threshold:"
read threshold
usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)
logfile="cpu_log.txt"
if [ ! -f $logfile ]; then
touch $logfile
fi
if [ $usage -lt $threshold ]; then
echo "Normal"
elif [ $usage -lt 80 ]; then
echo "Warning"
else
echo "Critical"
echo "High CPU: $usage%" >> $logfile
fi
********** 6 **********
--- page 7 ---
Explanation (5M)
•   #!/bin/bash → Shebang
•   read → input
•   if-elif-else → condition
•   touch → create log
• >> → append logs
Cron Job (5M)
*/5 * * * * /home/user/script.sh
Fields:
Field Meaning
*/5 every 5 minutes
*   hour
*   day
*   month
*   weekday
********** 7 **********
````

## 2025-26 · Re-Exam · Sem 4 · Answer key · paper 083b7f16d75b

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2025/Sem_04/Re-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/ANS_Linux and Secure OS for Business(702CO0C069)_2025-2026.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 01 Jul 2026
- Text: text (9 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Sem 4 Re-exam(Exam Year: 2025-2026)
Subject: Linux and Secure OS for Business
Date: 01 Jul 2026   Time: 02:00 pm to 05:00 pm (03:00 Hrs.)
Max. Marks: 100
RE EXAMINATION (Acad. Year:2025-2026)
Instructions:
1. This question paper contains 9 pages.
2. Answer to each new question to be started on a fresh page.
3. Figure in right hand side indicates full marks
4. Question number 1 is compulsory
5. Attempt any 4 from the rest
Q1. Linux Fundamentals   20 Marks
(a) File and Directory Management & File Manipulation Commands [5M]
[5M]
Key file and directory commands:
•   ls [-l, -a, -lh] — list files/directories with details, hidden files, human-readable sizes
• cd [path] — change directory; cd .. goes one level up; cd ~ goes to home
• pwd — print working directory (absolute path)
• mkdir [-p] dirname — create directory; -p creates parent directories
• rmdir / rm -r — remove empty directory / recursively remove directory with contents
• cp [-r] src dest — copy file or directory (-r for recursive)
• mv src dest — move or rename file/directory
• touch filename — create empty file or update timestamp
• cat / more / less — display file contents (less allows scrolling)
• head -n / tail -n — show first/last n lines of a file
•   find [path] -name 'pattern' — search for files by name
• wc [-l -w -c] — word/line/character count of a file
(b) Disk Partitioning in Linux — Primary, Extended & Logical Partitions [5M]
[5M]
Disk partitioning divides a physical disk into isolated sections so each can have its own filesystem.
• Primary Partition: Up to 4 can be created on an MBR disk. Bootable; holds an OS or data
directly.
• Extended Partition: A special primary partition acting as a container for logical partitions. Only 1
allowed per disk.
• Logical Partition: Created inside the extended partition. No fixed limit (beyond MBR constraints).
Cannot be directly booted from.
********** 1 **********
--- page 2 ---
Tools: fdisk (MBR), gdisk (GPT), parted (both). GPT disks support up to 128 primary partitions,
removing the need for extended/logical.
(c) Linux Booting Process — BIOS/UEFI to Login Prompt [5M]
[5M]
•   1. Power On → BIOS/UEFI: Hardware POST (Power-On Self Test); detects and initialises
hardware.
•   2. Bootloader (GRUB2): Located in MBR/EFI partition; loads the Linux kernel and initramfs into
RAM.
•   3. Kernel Initialisation: Kernel decompresses, detects hardware, mounts initramfs (temporary
root FS).
•   4. initramfs / initrd: Provides early userspace; loads drivers needed to mount the real root
filesystem.
•   5. Real Root FS Mounted: Control handed off from initramfs to the actual root partition.
•   6. systemd (PID 1): First process; reads targets, starts services (networking, display manager,
etc.).
•   7. Login Prompt / Display Manager: TTY text login or graphical login screen presented to the
user.
(d) Managing File Permissions and Ownership [5M]
[5M]
Linux uses a User–Group–Others (UGO) permission model.
• chmod — change permissions symbolically or numerically
◦   Symbolic: chmod u+x file (add execute for owner); chmod o-w file (remove write for others)
◦   Numeric (Octal): chmod 755 file (rwxr-xr-x); chmod 644 file (rw-r--r--)
• chown user:group file — change owner and/or group of a file
• chgrp groupname file — change group ownership only
• umask — sets default permission mask for newly created files (e.g., umask 022 → files get 644)
•   ls -l — view current permissions; format: [type][owner perms][group perms][others perms]
Q2. grep, Regex & Linux Distributions   20 Marks
(a) Purpose of grep Command [5M]
[5M]
grep (Global Regular Expression Print) searches files or standard input for lines matching a pattern and
prints matching lines.
• grep 'pattern' file — basic search
• grep -i — case-insensitive match
• grep -n — show line numbers
• grep -v — invert match (lines NOT matching)
• grep -r — recursive search in directory
• grep -E — extended regex (same as egrep)
• grep -c — count matching lines
********** 2 **********
--- page 3 ---
(b) grep Commands for Specific Patterns [10M]
[10M]
Find lines containing a 3-digit number:
grep -E '[0-9]{3}' logfile.txt
Or more precisely (standalone 3-digit number):
grep -E '\b[0-9]{3}\b' logfile.txt
Find lines starting with 'A' or 'a':
grep -E '^[Aa]' logfile.txt
Alternative using case-insensitive flag:
grep -i '^a' logfile.txt
Explanation of regex elements used:
•   [0-9]{3} — exactly three consecutive digits
•   \b — word boundary anchor
• ^ — start-of-line anchor
• [Aa] — character class matching uppercase or lowercase A
(c) Comparison of Two Linux Distributions [5M]
[5M]
Aspect   Ubuntu (Debian-based)   CentOS / RHEL (RPM-based)
Stability   LTS versions (2-yr cycle) stable;   Extremely stable; release cycle
non-LTS may include newer   ~10 yrs; used in enterprise
packages   production
Usability   User-friendly; beginner-oriented;   Server-oriented; steeper learning
large community; GUI available   curve; excellent for sysadmins
Package Manager   APT (apt-get, apt)   YUM / DNF (dnf install)
Security Updates   Timely; Canonical provides   Red Hat backports security
patches   patches; very conservative
Target Audience   Developers, students, desktops   Enterprise servers, financial/govt
sectors
Q3. Logical Volume Manager (LVM)   20 Marks
How LVM Solves the Multiple Small Disks Problem [2M]
[2M]
LVM (Logical Volume Manager) abstracts physical storage into a flexible pool. Multiple 10 GB disks are
grouped into one Volume Group (VG), and Logical Volumes (LVs) are carved from this pool. The
filesystem sees one large contiguous storage unit, regardless of how many physical disks underlie it.
Steps: Physical Volumes → Volume Group → Logical Volume [10M]
[10M]
********** 3 **********
--- page 4 ---
Step 1 — Create Physical Volumes (PVs):
pvcreate /dev/sdb /dev/sdc /dev/sdd
pvdisplay   # verify PVs
Step 2 — Create a Volume Group (VG):
vgcreate datavg /dev/sdb /dev/sdc /dev/sdd
vgdisplay datavg   # verify VG (shows total PE size ~30 GB)
Step 3 — Create a Logical Volume (LV):
lvcreate -L 25G -n datalv datavg
lvdisplay   # verify LV
Step 4 — Create a Filesystem and Mount:
mkfs.ext4 /dev/datavg/datalv
mount /dev/datavg/datalv /mnt/data
Step 5 — Persist in /etc/fstab:
/dev/datavg/datalv /mnt/data ext4 defaults 0 2
Advantages of LVM over Traditional Partitioning [2M]
[2M]
• Dynamic resizing: LVs can be extended or reduced without rebooting
• Snapshot support: point-in-time snapshots for backups
•   Striping and mirroring: built-in performance and redundancy
• No fixed partition boundaries: space allocated as needed from pool
Extending Storage Dynamically [2M]
[2M]
pvcreate /dev/sde   # add new disk as PV
vgextend datavg /dev/sde   # add PV to VG
lvextend -L +10G /dev/datavg/datalv   # extend LV
resize2fs /dev/datavg/datalv   # resize filesystem (ext4)
For XFS: use xfs_growfs /mnt/data instead of resize2fs.
LVM vs. Traditional Disk Partitioning [2M]
[2M]
LVM   Traditional Partitioning
Flexible resizing at runtime   Fixed at creation; resize requires unmount
Spans multiple disks   Limited to single disk
Snapshot capability   No native snapshot support
Complex setup   Simple, well-understood
********** 4 **********
--- page 5 ---
Q4. Linux Security — SUID/SGID/Sticky Bit, ACLs & File
20 Marks
Links
1. SUID, SGID, and Sticky Bit [5M]
[5M]
SUID (Set User ID) — Numeric: 4
•   Definition: When set on an executable, it runs with the privileges of the file's owner, not the
invoking user.
• Purpose: Allows limited privilege escalation for specific programs (e.g., passwd needs root to
update /etc/shadow).
• Set: chmod u+s file or chmod 4755 file
• Example: ls -l /usr/bin/passwd → shows -rwsr-xr-x
SGID (Set Group ID) — Numeric: 2
•   Definition: On executables, runs with group of the file; on directories, new files inherit the
directory's group.
• Purpose: Used for shared directories — files belong to the project group, not the creator's
primary group.
• Set: chmod g+s dir or chmod 2755 dir
• Example: A shared /project dir where all team files automatically get group 'devteam'.
Sticky Bit — Numeric: 1
•   Definition: On a directory, only the file owner (or root) can delete or rename their own files.
• Purpose: Prevents accidental/malicious deletion of others' files in world-writable directories.
• Set: chmod +t dir or chmod 1777 dir
• Example: /tmp directory (drwxrwxrwt) — all users write, but none can delete others' files.
2. Access Control Lists (ACLs) [10M]
[10M]
Need for ACLs:
•   Traditional UGO permissions allow only 3 permission sets. ACLs allow per-user and per-group
fine-grained permissions on any file.
• Example: Grant user 'alice' read-only access to a file owned by 'bob' without changing group
membership.
getfacl — View ACL:
getfacl /data/finance.txt
Output shows: owner, group, and any extra user/group ACL entries.
setfacl — Set ACL:
setfacl -m u:alice:r-- /data/finance.txt   # grant alice read
setfacl -m u:bob:rwx /data/finance.txt   # grant bob read/write/execute
setfacl -m g:devteam:rw- /data/project/   # grant group rw
setfacl -x u:alice /data/finance.txt   # remove alice's ACL
********** 5 **********
--- page 6 ---
setfacl -b /data/finance.txt   # remove all ACL entries
setfacl -d -m u:alice:rw /data/shared/   # default ACL for new files
Multiple user example:
setfacl -m u:analyst1:r--,u:manager:rw- /data/report.txt
Use getfacl to verify. Files with ACLs show a '+' in ls -l output: -rw-rw-r--+
3. File Links in Linux [5M]
[5M]
Hard Links:
• A hard link is a directory entry that points directly to the same inode (data blocks) as the original
file.
• Both the original and hard link are indistinguishable; deleting one doesn't affect the other.
• Cannot span filesystems; cannot link to directories.
ln original.txt hardlink.txt
Symbolic (Soft) Links:
• A symlink is a special file containing the path to another file; like a Windows shortcut.
• Can span filesystems and can link to directories.
•   If the target is deleted, the symlink becomes a 'dangling' (broken) link.
ln -s /etc/nginx/nginx.conf ~/nginx.conf
Feature   Hard Link   Symbolic Link
Inode   Same inode as original   Different inode
Cross-filesystem   No   Yes
Deleted target   Data persists   Link becomes broken
Links to dirs   No   Yes
Use case   Backups, deduplication   Config shortcuts, aliases
********** 6 **********
--- page 7 ---
Q5. Network Traffic Analysis & Security   20 Marks
tcpdump and Wireshark — Capture & Analyse Network Traffic [5M]
[5M]
tcpdump (CLI tool):
tcpdump -i eth0 -w capture.pcap   # capture on interface, save to file
tcpdump -i eth0 port 80   # filter HTTP traffic
tcpdump -i eth0 host 192.168.1.100   # traffic to/from specific IP
tcpdump -i eth0 -n -vv   # verbose, no DNS resolution
Wireshark (GUI tool):
• Open capture.pcap in Wireshark or capture live via interface.
• Display filters: ip.addr == 192.168.1.100 | tcp.port == 443 | http
• Follow TCP/UDP stream: right-click packet → Follow → TCP Stream
•   Statistics → Protocol Hierarchy shows traffic breakdown
•   Statistics → Conversations shows top talkers
Identifying Suspicious Packets / Abnormal Traffic Patterns [10M]
[10M]
Step 1 — Baseline Normal Traffic:
•   Identify known services, expected hosts, typical bandwidth usage.
Step 2 — Look for Anomalies:
• Port scans: SYN packets to many ports from one source (filter: tcp.flags.syn==1)
• Large data transfers at odd hours or to unknown external IPs
• Unencrypted sensitive data (cleartext passwords in HTTP/FTP/Telnet)
• DNS tunnelling: unusually long DNS queries or high DNS volume
• Repeated failed auth attempts: many RST packets or HTTP 401 responses
• ARP spoofing: duplicate ARP replies for the same IP
Step 3 — Tools for Detection:
•   netstat -tulnp — show active connections and listening ports
• ss -antp — socket statistics
•   iftop / nload — real-time bandwidth per connection
• ntopng — web-based network traffic monitor
• Snort / Suricata — IDS/IPS for signature-based detection
Preventive Measures to Secure the Network [5M]
[5M]
•   Firewall rules: Use iptables / nftables / ufw to whitelist only required ports
• Network segmentation: VLANs to isolate departments; limit lateral movement
• VPN / Encryption: Enforce TLS/SSH; disable cleartext protocols (Telnet, FTP, HTTP)
• IDS/IPS: Deploy Snort or Suricata with updated rulesets
• Regular audits: Schedule tcpdump captures; review logs in /var/log/syslog and /var/log/auth.log
• Patch management: Keep kernel, services, and software up to date
• Access control: Disable unused network interfaces; apply principle of least privilege
********** 7 **********
--- page 8 ---
Q6. Bash Scripting — User Account Management   20 Marks
Complete Bash Script [10M]
[10M]
#!/bin/bash
# User Account Checker Script
LOGFILE="user_check.log"
# Function: Check if user exists
check_user_exists() {
local username=$1
if grep -q "^$username:" /etc/passwd; then
echo "User '$username' EXISTS on this system."
echo "$(date): User '$username' found" >> "$LOGFILE"
check_home "$username"
check_execute "$username"
else
echo "User '$username' does NOT exist."
echo "$(date): User '$username' not found" >> "$LOGFILE"
fi
}
# Function: Check home directory
check_home() {
local username=$1
local homedir
homedir=$(grep "^$username:" /etc/passwd | cut -d: -f6)
if [ -d "$homedir" ]; then
echo " Home directory '$homedir' exists."
else
echo " Home directory '$homedir' does NOT exist."
fi
}
# Function: Check execute permission on home dir
check_execute() {
local username=$1
local homedir
homedir=$(grep "^$username:" /etc/passwd | cut -d: -f6)
if [ -x "$homedir" ]; then
echo " Execute permission on home directory: YES"
else
echo " Execute permission on home directory: NO"
fi
}
********** 8 **********
--- page 9 ---
# Main loop
while true; do
echo ""
echo "Enter username to check (or 'exit' to quit):"
read -r uname
if [ "$uname" = "exit" ]; then
echo "Exiting. Log saved to $LOGFILE."
break
fi
check_user_exists "$uname"
done
Working of Loops and Conditions [5M]
[5M]
• while true — infinite loop; continues until break is encountered when user types 'exit'.
•   if [ "$uname" = "exit" ] — string comparison using test/[ ] builtin; exits the loop with break.
•   if grep -q — runs grep silently; the exit code (0=found, 1=not found) drives the if-else branch.
•   if [ -d "$homedir" ] — file test operator -d checks directory existence.
•   if [ -x "$homedir" ] — file test operator -x checks execute permission.
• Functions (check_user_exists, check_home, check_execute) — modular blocks called with
username as argument; local variables prevent scope pollution.
Input/Output Handling [5M]
[5M]
•   Input: read -r uname — reads a line from stdin into variable uname; -r prevents backslash
interpretation.
• Command substitution: homedir=$(grep ...) — captures command output into a variable.
• stdout (echo): Displays messages to the terminal for the user.
•   File logging (>>): Results appended to user_check.log using >> (append redirection) with date
timestamp.
• Pipes (|): grep output piped to cut to extract specific field from /etc/passwd.
•   Exit codes: Bash commands return 0 (success) or non-zero (failure); if statements evaluate
these codes.
********** 9 **********
````

## 2024-25 · Final-Exam · Sem 4 · Answer key · paper 85be9dae081d

- Departments: Data Science
- Programmes: BTech CSE DS 7011
- Source: `02_Question_Papers/2024/Sem_04/Final-Exam/BTech_CSE_DS_7011/Linux and Secure OS for Business/ANS_Linux and Secure OS for Business(702CO0C052)_2024-2025.pdf`
- Printed on paper: max marks: 100; duration hours: 3; exam date: 28 Apr 2025
- Text: text (5 pages)

````text
SYNOPTICS
SVKMs NMIMS
MUKESH PATEL SCH.OF TECH.MGMT ENGG-NM-M
Programme: BACHELOR OF TECHNOLOGY - COMPUTER SCIENCE AND
ENGINEERING (DATA SCIENCE)
Year: II/Semester IV(Exam Year: 2024-2025)
Subject: Linux and Secure OS for Business
Date: 28 Apr 2025   Time: 10:00 am to 01:00 pm (03:00 Hrs.)
Max. Marks: 100
FINAL EXAMINATION (Acad. Year:2024-2025)
Instructions:
1. This question paper contains 5 pages.
2. Question No. 1 is compulsory.
3. Figure in right handout of remaining questions, attempt any 4 questions. side indicates full marks
4. In all 5 questions to be attempted.
5. All questions carry equal marks.
6. Answer to each new question to be started on a fresh page.
7. Figures in brackets on the right hand side indicate full marks.
8. Assume Suitable data if necessary.
Q1.
CO:1 A. What is the difference between ls -a and ls -l commands?   5 M
SO:1
BL:1
Difference between ls -a and ls -l:
• ls -a: Lists all files, including hidden files (files starting with .).
• ls -l: Lists files in long format, showing permissions, ownership, size, and
modification time
CO:1 B. What are the key components of LVM, and what role does each component   5 M
SO:1   play?
BL:1
Key components of LVM and their roles:
1. Physical Volume (PV): Represents physical storage (disks/partitions).
2. Volume Group (VG): Combines PVs into a pool of storage.
3. Logical Volume (LV): Virtual partitions created from VGs, used like
traditional partitions.
CO:1 C. What is the purpose of cron and at commands in job scheduling, and   5 M
SO:1   how do they differ?
BL:1
********** 1 **********
--- page 2 ---
• cron: Schedules recurring tasks at fixed intervals (e.g., daily, weekly).
• at: Schedules one-time tasks at a specific future time.
CO:1 D. What is the difference between the usermod, useradd, and userdel   5 M
SO:1   commands?
BL:2
Difference between usermod, useradd, and userdel:
• useradd: Creates a new user.
• usermod: Modifies existing user settings (e.g., group membership).
• userdel: Deletes a user and optionally removes the home directory.
Q2
CO:1 A. Explain the steps involved in installing a Linux OS and setting up   10 M
SO:1   environment variables.
BL:2
Steps to install Linux OS and set up environment variables:
1. Boot from installation media, select installation type, and configure partitions.
2. Install packages and set root password.
3. After installation, edit /etc/environment or ~/.bashrc to set variables.
Example: export PATH=$PATH:/custom/path.
CO:1 B. Describe the steps involved in mounting and unmounting file systems in   10 M
SO:1   Linux. Why is mounting necessary?
BL:2
Mounting and unmounting file systems:
1. Mount: mount /dev/sdX /mnt — Links the device to the filesystem.
2. Unmount: umount /mnt — Safely detaches the device.
• Why necessary? Mounting gives access to files, while unmounting prevents
data corruption during removal.
Q3
CO:1 A. Apply package management commands to install, update, and remove   10 M
SO:1   software on a Linux system.
BL:3
********** 2 **********
--- page 3 ---
Package management commands:
•   Install: apt install <package> (Debian) or yum install <package>
(Red Hat).
• Update: apt update && apt upgrade
• Remove: apt remove <package>
CO:1 B. Apply the necessary commands to create a new user, assign the user to a   10 M
SO:1   group, and set a password.
BL:3
sudo useradd newuser
sudo passwd newuser
sudo usermod -aG groupname newuser
Q4
CO:2 A. Encrypt a disk partition using cryptsetup and demonstrate the process   10 M
SO:2   of mounting and accessing it.
BL:3
cryptsetup luksFormat /dev/sdX
cryptsetup luksOpen /dev/sdX encrypted_disk
mkfs.ext4 /dev/mapper/encrypted_disk
mount /dev/mapper/encrypted_disk /mnt
CO:2 B. Configure a network interface with a static IP address and verify the   10 M
SO:2   connection.
BL:3
Configure static IP:
1. Edit /etc/netplan/*.yaml (Ubuntu) or /etc/sysconfig/network-
scripts/ifcfg-eth0 (Red Hat).
2. Apply changes with netplan apply or systemctl restart network.
Q5
CO:2 A. Analyze a scenario where improper file permissions led to a security   10 M
SO:2   breach. How would you correct and prevent such issues?
BL:4
Analyze improper file permissions:
•   Issue: World-writable files (chmod 777) can be modified by any user, leading
to security risks.
•   Fix: Restrict permissions (chmod 640) and apply ACLs for fine-grained
control.
********** 3 **********
--- page 4 ---
CO:3 B. Write a BASH script that takes two integers as input, compares them using   10 M
SO:2   conditional expressions, and prints whether the first is greater, smaller, or
BL:3
equal to the second.
#!/bin/bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2
if [ $num1 -gt $num2 ]; then
echo "$num1 is greater"
elif [ $num1 -lt $num2 ]; then
echo "$num1 is smaller"
else
echo "Both numbers are equal"
fi
Q6
CO:2 A. Describe how Access Control Lists (ACLs) extend traditional file permissions 10 M
SO:2   in Linux. When would you use ACLs?
BL:2
ACLs vs traditional permissions:
•   Traditional permissions use rwx for owner, group, and others.
• ACLs provide more flexibility, allowing permissions for specific users and
groups.
Example: setfacl -m u:john:rwx file.txt grants john full access.
CO:3 B. Create a script to check if a file exists, is readable, and is executable.   10 M
SO:3   Display appropriate messages based on the results.
BL:3
#!/bin/bash
read -p "Enter file name: " file
if [ -e "$file" ]; then
echo "File exists"
[ -r "$file" ] && echo "File is readable"
[ -x "$file" ] && echo "File is executable"
else
echo "File does not exist"
fi
Q7
********** 4 **********
--- page 5 ---
CO:2 A. Describe how to install and configure the Apache web server in Linux.   10 M
SO:2   What configuration files are involved?
BL:2
Install and configure Apache:
1. Install: apt install apache2 (Debian) or yum install httpd (Red Hat).
2. Start service: systemctl start apache2
3. Configuration file: /etc/apache2/apache2.conf (Debian) or
/etc/httpd/conf/httpd.conf (Red Hat).
CO:3 B. Write a BASH script that automates daily system updates using cron and   10 M
SO:3   logs the results in a file.
BL:3
1. Write script (update.sh):
#!/bin/bash
apt update && apt upgrade -y >> /var/log/update.log
2. Make it executable: chmod +x update.sh
3. Schedule with cron: crontab -e and add:
0 0 * * * /path/to/update.sh
********** 5 **********
````
