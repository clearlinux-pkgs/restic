PKG_NAME := restic
URL = https://github.com/restic/restic/releases/download/v0.12.1/restic-0.12.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/restic-vendor/snapshot/restic-vendor-0.12.1.tar.xz ./

include ../common/Makefile.common
