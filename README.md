# qwt-crossbuild
Qubes Windows Tools crossbuild environment based on mingw, wine and docker

[![Build Status](https://travis-ci.org/tabit-pro/qwt-crossbuild.svg?branch=master)](https://travis-ci.org/tabit-pro/qwt-crossbuild)

In comparison with the original ITL's Qubes Tools qwt-crossbuild contains several in-progress improvements:

- [x] rebuild QWT utils (mingw, x86, x86\_64)
- [x] include updated xen pv drivers (8.2.2)
- [x] avoid high cpu consumption (move qga CreateEvent outside an event processing loop)
- [x] fix dhcp dependencies (winhttproxy wants to stay alive)
- [x] hide command prompt windows during setup execution (WixQuiteExec)
- [x] sign and install drivers without prompt (libwdi-based pkihelper utility)
- [x] remove format dialog (diskpart instead of prepare-volume)
- [ ] troubleshoot bsod errors (0x101, 0xc5, 0x50 - the toughest elusive fighters)
- [x] prepare reproducible/deterministic build (binaries only)

## QWT Runtime prerequisuites

1. Fully updated Windows 7/10
1. Testsigning
1. Backup

## Build QWT

```shell_session
$ git clone https://github.com/tabit-pro/qwt-crossbuild .
$ docker build -t tabit/qwt .
$ mkdir -p ~/qwtiso
$ docker run -v $(pwd):/src -v ~/qwtiso:/build/noarch -it tabit/qwt sh -c "sh prep.sh && make x86 && make x64 && rpmbuild -bb --define '_sourcedir /build' --define '_rpmdir /build' *.spec && cd noarch && createrepo ./"
```

