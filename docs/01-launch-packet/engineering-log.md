### 2026-05-17 

DigitalOcean droplet
```
ssh root@142.93.68.153
```

uname -r
```
5.15.0-179-generic
```

cat /etc/os-release | head -3
```
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
```

start a tmux session to keep long-running commands going if your SSH session drops
```
tmux new -s safeexec
```

DigitalOcean Premium Intel droplet, NYC3, 2 vCPU / 4 GB / 120 GB NVMe
Ubuntu 22.04.5 LTS
Linux kernel: <output of `uname -r`>
Docker: 29.5.0
runsc: release-20260511.0 (OCI spec 1.2.1)

=== W1 droplet inventory (2026-05-17T21:06:18Z) ===
Linux safeexec-dev 5.15.0-179-generic #189-Ubuntu SMP Tue May 5 18:20:56 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
Description:    Ubuntu 22.04.5 LTS
Docker version 29.5.0, build 98f1464
runsc version release-20260511.0
spec: 1.2.1

{
    "runtimes": {
        "runsc": {
            "path": "/usr/bin/runsc"
        }
    }
}