pkgname = "iotop"
pkgver = "1.26"
pkgrel = 2
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "ncurses-devel",
]
pkgdesc = "Top-like utility for IO"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/Tomas-M/iotop"
source = f"https://github.com/Tomas-M/iotop/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b0a334cba89249bc7cbb87cf92cf4166911bf00dd2ea8841b572fd776018c487"
hardening = ["cfi", "vis"]
# no tests
options = ["!check"]
