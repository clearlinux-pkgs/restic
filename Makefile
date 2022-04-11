PKG_NAME := restic
URL = https://github.com/restic/restic/releases/download/v0.13.1/restic-0.13.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/restic-vendor/snapshot/restic-vendor-0.13.0.tar.xz ./

include ../common/Makefile.common
