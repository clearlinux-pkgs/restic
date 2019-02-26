#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x91A6868BD3F7A907 (alexander@bumpern.de)
#
Name     : restic
Version  : 0.9.4
Release  : 1
URL      : https://github.com/restic/restic/releases/download/v0.9.4/restic-0.9.4.tar.gz
Source0  : https://github.com/restic/restic/releases/download/v0.9.4/restic-0.9.4.tar.gz
Source99 : https://github.com/restic/restic/releases/download/v0.9.4/restic-0.9.4.tar.gz.asc
Summary  : restic is a backup program that is fast, efficient and secure.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause LGPL-3.0 MIT MPL-2.0-no-copyleft-exception
Requires: restic-license = %{version}-%{release}
BuildRequires : buildreq-golang

%description
restic is a program that does backups right. The design goals are:

Easy: Doing backups should be a frictionless process, otherwise you are tempted to skip it. Restic should be easy to configure and use, so that in the unlikely event of a data loss you can just restore it. Likewise, restoring data should not be complicated.

Fast: Backing up your data with restic should only be limited by your network or hard disk bandwidth so that you can backup your files every day. Nobody does backups if it takes too much time. Restoring backups should only transfer data that is needed for the files that are to be restored, so that this process is also fast.

Verifiable: Much more important than backup is restore, so restic enables you to easily verify that all data can be restored.

Secure: Restic uses cryptography to guarantee confidentiality and integrity of your data. The location where the backup data is stored is assumed to be an untrusted environment (e.g. a shared space where others like system administrators are able to access your backups). Restic is built to secure your data against such attackers, by encrypting it with AES-256 in counter mode and authenticating it using Poly1305-AES.

Efficient: With the growth of data, additional snapshots should only take the storage of the actual increment. Even more, duplicate data should be de-duplicated before it is actually written to the storage backend to save precious backup space.

Versatile storage: Users can provide many different places to store the backups. Local, SFTP, Restics REST-Server, Amazon S3, Minio, Openstack Swift, Backblaze B2, Microsoft Azure Blob Storage, Google Cloud Storage and more by the usage of rclone.

Free: restic is free software and licensed under the BSD 2-Clause License and actively developed on GitHub.

%package license
Summary: license components for the restic package.
Group: Default

%description license
license components for the restic package.


%prep
%setup -q -n restic-0.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
go build -mod vendor

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/restic
cp LICENSE %{buildroot}/usr/share/package-licenses/restic/LICENSE
cp vendor/bazil.org/fuse/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_bazil.org_fuse_LICENSE
cp vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_cloud.google.com_go_LICENSE
cp vendor/github.com/Azure/azure-sdk-for-go/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_Azure_azure-sdk-for-go_LICENSE
cp vendor/github.com/Azure/go-autorest/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_Azure_go-autorest_LICENSE
cp vendor/github.com/cenkalti/backoff/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_cenkalti_backoff_LICENSE
cp vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
cp vendor/github.com/dgrijalva/jwt-go/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_dgrijalva_jwt-go_LICENSE
cp vendor/github.com/elithrar/simple-scrypt/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_elithrar_simple-scrypt_LICENSE
cp vendor/github.com/go-ini/ini/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_go-ini_ini_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_google_go-cmp_LICENSE
cp vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_hashicorp_golang-lru_LICENSE
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/juju/ratelimit/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_juju_ratelimit_LICENSE
cp vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_kr_fs_LICENSE
cp vendor/github.com/kurin/blazer/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_kurin_blazer_LICENSE
cp vendor/github.com/marstr/guid/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_marstr_guid_LICENSE.txt
cp vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_mattn_go-isatty_LICENSE
cp vendor/github.com/minio/minio-go/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_minio_minio-go_LICENSE
cp vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_mitchellh_go-homedir_LICENSE
cp vendor/github.com/ncw/swift/COPYING %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_ncw_swift_COPYING
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/pkg/profile/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_pkg_profile_LICENSE
cp vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_pkg_sftp_LICENSE
cp vendor/github.com/pkg/xattr/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_pkg_xattr_LICENSE
cp vendor/github.com/restic/chunker/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_restic_chunker_LICENSE
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_russross_blackfriday_LICENSE.txt
cp vendor/github.com/satori/go.uuid/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_satori_go.uuid_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_github.com_spf13_pflag_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_oauth2_LICENSE
cp vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_sync_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_golang.org_x_text_LICENSE
cp vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_google.golang.org_api_LICENSE
cp vendor/google.golang.org/api/googleapi/internal/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_google.golang.org_api_googleapi_internal_uritemplates_LICENSE
cp vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_google.golang.org_appengine_LICENSE
cp vendor/gopkg.in/tomb.v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_gopkg.in_tomb.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_NOTICE


%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/restic/LICENSE
/usr/share/package-licenses/restic/vendor_bazil.org_fuse_LICENSE
/usr/share/package-licenses/restic/vendor_cloud.google.com_go_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_Azure_azure-sdk-for-go_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_Azure_go-autorest_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_cenkalti_backoff_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
/usr/share/package-licenses/restic/vendor_github.com_dgrijalva_jwt-go_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_elithrar_simple-scrypt_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_go-ini_ini_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_google_go-cmp_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_hashicorp_golang-lru_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_juju_ratelimit_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_kr_fs_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_kurin_blazer_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_marstr_guid_LICENSE.txt
/usr/share/package-licenses/restic/vendor_github.com_mattn_go-isatty_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_minio_minio-go_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_mitchellh_go-homedir_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_ncw_swift_COPYING
/usr/share/package-licenses/restic/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_pkg_profile_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_pkg_sftp_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_pkg_xattr_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_restic_chunker_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_russross_blackfriday_LICENSE.txt
/usr/share/package-licenses/restic/vendor_github.com_satori_go.uuid_LICENSE
/usr/share/package-licenses/restic/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/restic/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_oauth2_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_sync_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/restic/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/restic/vendor_google.golang.org_api_LICENSE
/usr/share/package-licenses/restic/vendor_google.golang.org_api_googleapi_internal_uritemplates_LICENSE
/usr/share/package-licenses/restic/vendor_google.golang.org_appengine_LICENSE
/usr/share/package-licenses/restic/vendor_gopkg.in_tomb.v2_LICENSE
/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/restic/vendor_gopkg.in_yaml.v2_NOTICE
