# SSH

## SSH keys

To generate new ssh keys run
```bash
ssh-keygen
```

**Hit enter 3 times to avoid accadentally setting a password or different location for the file**

To copy the keys to another host so you can jump between NFS mounts without issue run:
```bash
ssh-copy-id <user@host>
```
Remember to go back the other way so you can go both directions


