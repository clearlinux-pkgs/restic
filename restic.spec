#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x91A6868BD3F7A907 (alexander@bumpern.de)
#
Name     : restic
Version  : 0.9.6
Release  : 18
URL      : https://github.com/restic/restic/releases/download/v0.9.6/restic-0.9.6.tar.gz
Source0  : https://github.com/restic/restic/releases/download/v0.9.6/restic-0.9.6.tar.gz
Source1  : https://github.com/restic/restic/releases/download/v0.9.6/restic-0.9.6.tar.gz.asc
Summary  : restic is a backup program that is fast, efficient and secure.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause LGPL-3.0 MIT MPL-2.0
Requires: restic-bin = %{version}-%{release}
Requires: restic-data = %{version}-%{release}
Requires: restic-license = %{version}-%{release}
Requires: restic-man = %{version}-%{release}
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

%package bin
Summary: bin components for the restic package.
Group: Binaries
Requires: restic-data = %{version}-%{release}
Requires: restic-license = %{version}-%{release}

%description bin
bin components for the restic package.


%package data
Summary: data components for the restic package.
Group: Data

%description data
data components for the restic package.


%package license
Summary: license components for the restic package.
Group: Default

%description license
license components for the restic package.


%package man
Summary: man components for the restic package.
Group: Default

%description man
man components for the restic package.


%prep
%setup -q -n restic-0.9.6
cd %{_builddir}/restic-0.9.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605150428
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  -f foo.make || go build -mod=vendor -v -buildmode=pie -ldflags '-linkmode external -extldflags "-static-pie"' -tags netgo,osusergo -o restic ./cmd/restic


%install
export SOURCE_DATE_EPOCH=1605150428
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/restic
cp %{_builddir}/restic-0.9.6/LICENSE %{buildroot}/usr/share/package-licenses/restic/68645af047dcb3bcca960d2c1b1ece30a7141f76
cp %{_builddir}/restic-0.9.6/vendor/bazil.org/fuse/LICENSE %{buildroot}/usr/share/package-licenses/restic/ae97d9da13b4f2a9a6c46d22d9af574956e4ea59
cp %{_builddir}/restic-0.9.6/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/azure-sdk-for-go/LICENSE %{buildroot}/usr/share/package-licenses/restic/861181924d993ee58a17a2c3c3a3faecf895849c
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/go-autorest/autorest/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/go-autorest/autorest/adal/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/go-autorest/autorest/date/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/go-autorest/logger/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/restic-0.9.6/vendor/github.com/Azure/go-autorest/tracing/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
cp %{_builddir}/restic-0.9.6/vendor/github.com/cenkalti/backoff/LICENSE %{buildroot}/usr/share/package-licenses/restic/101c182fa18fd56a09164278f17e4282264c5e9e
cp %{_builddir}/restic-0.9.6/vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/restic/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/restic-0.9.6/vendor/github.com/dgrijalva/jwt-go/LICENSE %{buildroot}/usr/share/package-licenses/restic/b132e03c6b6bd85fbc2394f808acae8f5d0ebaf0
cp %{_builddir}/restic-0.9.6/vendor/github.com/elithrar/simple-scrypt/LICENSE %{buildroot}/usr/share/package-licenses/restic/71a24b258c1c84ec9cb58aa6174e62477ae0af0b
cp %{_builddir}/restic-0.9.6/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/restic/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/restic-0.9.6/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/restic/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/restic-0.9.6/vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/restic/ece3df1263c100f93c427face535a292723d38e7
cp %{_builddir}/restic-0.9.6/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/restic/9174f93c54ad0022bbb9b445480cfb6b4217226a
cp %{_builddir}/restic-0.9.6/vendor/github.com/juju/ratelimit/LICENSE %{buildroot}/usr/share/package-licenses/restic/2a1a5c359d4a8f86d77f7cdd6b4af6583ce0db2e
cp %{_builddir}/restic-0.9.6/vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/restic/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/restic-0.9.6/vendor/github.com/kurin/blazer/LICENSE %{buildroot}/usr/share/package-licenses/restic/34418523d96f6abcdf613b70f532649c3f49f679
cp %{_builddir}/restic-0.9.6/vendor/github.com/marstr/guid/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/2e3d2ef4c73834a3a46bcc4e9ebc2cd9a713004e
cp %{_builddir}/restic-0.9.6/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/restic/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/restic-0.9.6/vendor/github.com/minio/minio-go/v6/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/github.com/minio/sha256-simd/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/restic/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/restic-0.9.6/vendor/github.com/ncw/swift/COPYING %{buildroot}/usr/share/package-licenses/restic/8fb789d383906a5e83d6a74149e094f8d6921812
cp %{_builddir}/restic-0.9.6/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/restic/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/restic-0.9.6/vendor/github.com/pkg/profile/LICENSE %{buildroot}/usr/share/package-licenses/restic/f63616ea1c9a1092cfea2c3c18309e3d1b67a9c9
cp %{_builddir}/restic-0.9.6/vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/restic/2510861d72bd971c91b53a5c5fc291e2971c669e
cp %{_builddir}/restic-0.9.6/vendor/github.com/pkg/xattr/LICENSE %{buildroot}/usr/share/package-licenses/restic/0f1cfab3f5481834d4f073129376589fe305c5f7
cp %{_builddir}/restic-0.9.6/vendor/github.com/restic/chunker/LICENSE %{buildroot}/usr/share/package-licenses/restic/05eefe8d1fd29f2514df448943df0b470eb716d1
cp %{_builddir}/restic-0.9.6/vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/restic-0.9.6/vendor/github.com/satori/go.uuid/LICENSE %{buildroot}/usr/share/package-licenses/restic/b4b35a8138ee83256aca752d3813d3d0757d8380
cp %{_builddir}/restic-0.9.6/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
cp %{_builddir}/restic-0.9.6/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/restic/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/restic-0.9.6/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/restic/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/restic-0.9.6/vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/restic/ab32a5c14ccc0a6d38e173568a5577493e3f6870
cp %{_builddir}/restic-0.9.6/vendor/google.golang.org/api/googleapi/internal/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/restic/e99e0980a6d8f06248a213a988ba1bb3c8d4a76b
cp %{_builddir}/restic-0.9.6/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/restic-0.9.6/vendor/gopkg.in/ini.v1/LICENSE %{buildroot}/usr/share/package-licenses/restic/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
cp %{_builddir}/restic-0.9.6/vendor/gopkg.in/tomb.v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/178b27feb961b28990b377da59e9d43d868a0a6f
cp %{_builddir}/restic-0.9.6/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/restic-0.9.6/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/restic/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/restic-0.9.6/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/restic/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
true
## install_append content
install -d %{buildroot}/usr/bin/
install -d %{buildroot}/usr/share/man/man1
install -d %{buildroot}/usr/share/zsh/site-functions
install -d %{buildroot}/usr/share/bash-completion/completions
install -m0755 restic %{buildroot}/usr/bin/
install -p -m 644 doc/man/* %{buildroot}/usr/share/man/man1/
install -p -m 644 doc/zsh-completion.zsh %{buildroot}/usr/share/zsh/site-functions/_restic
install -p -m 644 doc/bash-completion.sh %{buildroot}/usr/share/bash-completion/completions/restic
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/restic

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/restic
/usr/share/zsh/site-functions/_restic

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/restic/05eefe8d1fd29f2514df448943df0b470eb716d1
/usr/share/package-licenses/restic/0f1cfab3f5481834d4f073129376589fe305c5f7
/usr/share/package-licenses/restic/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/restic/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/restic/178b27feb961b28990b377da59e9d43d868a0a6f
/usr/share/package-licenses/restic/2510861d72bd971c91b53a5c5fc291e2971c669e
/usr/share/package-licenses/restic/2a1a5c359d4a8f86d77f7cdd6b4af6583ce0db2e
/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/restic/2e3d2ef4c73834a3a46bcc4e9ebc2cd9a713004e
/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
/usr/share/package-licenses/restic/34418523d96f6abcdf613b70f532649c3f49f679
/usr/share/package-licenses/restic/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/restic/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/restic/68645af047dcb3bcca960d2c1b1ece30a7141f76
/usr/share/package-licenses/restic/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/restic/71a24b258c1c84ec9cb58aa6174e62477ae0af0b
/usr/share/package-licenses/restic/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/restic/861181924d993ee58a17a2c3c3a3faecf895849c
/usr/share/package-licenses/restic/8fb789d383906a5e83d6a74149e094f8d6921812
/usr/share/package-licenses/restic/9174f93c54ad0022bbb9b445480cfb6b4217226a
/usr/share/package-licenses/restic/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/restic/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/restic/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/restic/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/restic/ab32a5c14ccc0a6d38e173568a5577493e3f6870
/usr/share/package-licenses/restic/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/restic/ae97d9da13b4f2a9a6c46d22d9af574956e4ea59
/usr/share/package-licenses/restic/b132e03c6b6bd85fbc2394f808acae8f5d0ebaf0
/usr/share/package-licenses/restic/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/restic/b4b35a8138ee83256aca752d3813d3d0757d8380
/usr/share/package-licenses/restic/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/restic/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/restic/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/restic/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
/usr/share/package-licenses/restic/e99e0980a6d8f06248a213a988ba1bb3c8d4a76b
/usr/share/package-licenses/restic/ece3df1263c100f93c427face535a292723d38e7
/usr/share/package-licenses/restic/f63616ea1c9a1092cfea2c3c18309e3d1b67a9c9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/restic-backup.1
/usr/share/man/man1/restic-cache.1
/usr/share/man/man1/restic-cat.1
/usr/share/man/man1/restic-check.1
/usr/share/man/man1/restic-diff.1
/usr/share/man/man1/restic-dump.1
/usr/share/man/man1/restic-find.1
/usr/share/man/man1/restic-forget.1
/usr/share/man/man1/restic-generate.1
/usr/share/man/man1/restic-init.1
/usr/share/man/man1/restic-key.1
/usr/share/man/man1/restic-list.1
/usr/share/man/man1/restic-ls.1
/usr/share/man/man1/restic-migrate.1
/usr/share/man/man1/restic-mount.1
/usr/share/man/man1/restic-prune.1
/usr/share/man/man1/restic-rebuild-index.1
/usr/share/man/man1/restic-recover.1
/usr/share/man/man1/restic-restore.1
/usr/share/man/man1/restic-self-update.1
/usr/share/man/man1/restic-snapshots.1
/usr/share/man/man1/restic-stats.1
/usr/share/man/man1/restic-tag.1
/usr/share/man/man1/restic-unlock.1
/usr/share/man/man1/restic-version.1
/usr/share/man/man1/restic.1
