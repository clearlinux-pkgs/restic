PKG_NAME := restic
URL = https://github.com/restic/restic/releases/download/v0.14.0/restic-0.14.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/restic-vendor/snapshot/restic-vendor-0.13.0.tar.xz ./

include ../common/Makefile.common
