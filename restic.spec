#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x91A6868BD3F7A907 (alexander@bumpern.de)
#
Name     : restic
Version  : 0.14.0
Release  : 47
URL      : https://github.com/restic/restic/releases/download/v0.14.0/restic-0.14.0.tar.gz
Source0  : https://github.com/restic/restic/releases/download/v0.14.0/restic-0.14.0.tar.gz
Source1  : http://localhost/cgit/projects/restic-vendor/snapshot/restic-vendor-0.14.0.tar.xz
Source2  : https://github.com/restic/restic/releases/download/v0.14.0/restic-0.14.0.tar.gz.asc
Summary  : restic is a backup program that is fast, efficient and secure.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause LGPL-3.0 MIT MPL-2.0
Requires: restic-bin = %{version}-%{release}
Requires: restic-data = %{version}-%{release}
Requires: restic-license = %{version}-%{release}
Requires: restic-man = %{version}-%{release}
BuildRequires : buildreq-golang
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n restic-0.14.0
cd %{_builddir}
tar xf %{_sourcedir}/restic-vendor-0.14.0.tar.xz
cd %{_builddir}/restic-0.14.0
mkdir -p ./
cp -r %{_builddir}/restic-vendor-0.14.0/* %{_builddir}/restic-0.14.0/./

%build
## build_prepend content
unset CLEAR_DEBUG_TERSE
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677183428
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
make  %{?_smp_mflags}  -f foo.make || go build -v -mod=vendor -ldflags='-X main.version=%{version}' -o ./restic ./cmd/restic


%install
export SOURCE_DATE_EPOCH=1677183428
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/restic
cp %{_builddir}/restic-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/restic/68645af047dcb3bcca960d2c1b1ece30a7141f76 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/cloud.google.com/go/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/cloud.google.com/go/compute/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/cloud.google.com/go/iam/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/cloud.google.com/go/storage/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/azure-sdk-for-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/646a9ad075072bb41132a4a0a2ceebbb457dda0c || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/autorest/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/autorest/adal/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/autorest/date/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/logger/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/Azure/go-autorest/tracing/LICENSE %{buildroot}/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/cenkalti/backoff/v4/LICENSE %{buildroot}/usr/share/package-licenses/restic/101c182fa18fd56a09164278f17e4282264c5e9e || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/7be82c1a81e7197640a88df91dc82d64b77c7acd || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/restic/b7a606730713ac061594edab33cf941704b4a95c || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/dustin/go-humanize/LICENSE %{buildroot}/usr/share/package-licenses/restic/4b5f40487c165cf31691824a93d375fcb65ea30a || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/elithrar/simple-scrypt/LICENSE %{buildroot}/usr/share/package-licenses/restic/71a24b258c1c84ec9cb58aa6174e62477ae0af0b || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/go-ole/go-ole/LICENSE %{buildroot}/usr/share/package-licenses/restic/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/gofrs/uuid/LICENSE %{buildroot}/usr/share/package-licenses/restic/b4b35a8138ee83256aca752d3813d3d0757d8380 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/golang-jwt/jwt/v4/LICENSE %{buildroot}/usr/share/package-licenses/restic/5e975d829f4ea420c028ba512f8bb3e0ebaaf574 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/restic/172ca3bbafe312a1cf09cfff26953db2f425c28e || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/restic/aa9b240f558caed367795f667629ccbca28f20b2 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/restic/7080652cc78cd9855d39e324529a3b5f3745dcd6 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/restic/08021ae73f58f423dd6e7b525e81cf2520f7619e || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/googleapis/enterprise-certificate-proxy/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/googleapis/gax-go/v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/2bda142bd58fd76f408cf18fa997d8fab0278a22 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/restic/ece3df1263c100f93c427face535a292723d38e7 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/restic/62446e71c226403f1a2e67d0f66ede03e3fbdd2f || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/restic/810612ee8c1872b7ee4dba34c090ebd8f7491aa1 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/juju/ratelimit/LICENSE %{buildroot}/usr/share/package-licenses/restic/2a1a5c359d4a8f86d77f7cdd6b4af6583ce0db2e || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/klauspost/compress/LICENSE %{buildroot}/usr/share/package-licenses/restic/0e8f2042647b8140e79c4eb7d233d1b39231db09 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/klauspost/compress/internal/snapref/LICENSE %{buildroot}/usr/share/package-licenses/restic/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/klauspost/compress/zstd/internal/xxhash/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/7be82c1a81e7197640a88df91dc82d64b77c7acd || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/klauspost/cpuid/v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/41a17a069904e6a10fa1b1bcf67c2e4d836937d1 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/kr/fs/LICENSE %{buildroot}/usr/share/package-licenses/restic/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/kurin/blazer/LICENSE %{buildroot}/usr/share/package-licenses/restic/34418523d96f6abcdf613b70f532649c3f49f679 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/minio/md5-simd/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/minio/md5-simd/LICENSE.Golang %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/minio/minio-go/v7/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/minio/minio-go/v7/NOTICE %{buildroot}/usr/share/package-licenses/restic/1ab6cff82ebc6ddb590da08bf488874f0b674d64 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/minio/sha256-simd/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/restic/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/restic/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/ncw/swift/v2/COPYING %{buildroot}/usr/share/package-licenses/restic/8fb789d383906a5e83d6a74149e094f8d6921812 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/restic/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/pkg/profile/LICENSE %{buildroot}/usr/share/package-licenses/restic/f63616ea1c9a1092cfea2c3c18309e3d1b67a9c9 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/pkg/sftp/LICENSE %{buildroot}/usr/share/package-licenses/restic/2510861d72bd971c91b53a5c5fc291e2971c669e || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/pkg/xattr/LICENSE %{buildroot}/usr/share/package-licenses/restic/0f1cfab3f5481834d4f073129376589fe305c5f7 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/restic/chunker/LICENSE %{buildroot}/usr/share/package-licenses/restic/05eefe8d1fd29f2514df448943df0b470eb716d1 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/rs/xid/LICENSE %{buildroot}/usr/share/package-licenses/restic/9af8d79ca96a43a2c76c79f32c0366c0ea64fdfd || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/da34754c05d40ff81f91de8c1b85ea6e5503e21d || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/restic/a1c7852c717fed2c9a0284ed112ea66013230da6 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/restic/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/restic/b3c86ae465b21f7323059db335158b48187731c7 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/restic/1128f8f91104ba9ef98d37eea6523a888dcfa5de || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/term/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/golang.org/x/xerrors/LICENSE %{buildroot}/usr/share/package-licenses/restic/844fb1cc442e5f3d1800e47ae5d76d11a872b91c || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/api/LICENSE %{buildroot}/usr/share/package-licenses/restic/ab32a5c14ccc0a6d38e173568a5577493e3f6870 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/api/internal/third_party/uritemplates/LICENSE %{buildroot}/usr/share/package-licenses/restic/475b0ccf682da5e05e3aa1eb6146b30132ae717d || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/restic/74850a25a5319bdddc0d998eb8926c18bada282b || :
cp %{_builddir}/restic-vendor-%{version}/vendor/gopkg.in/ini.v1/LICENSE %{buildroot}/usr/share/package-licenses/restic/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a || :
cp %{_builddir}/restic-vendor-%{version}/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/restic/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
cp %{_builddir}/restic-vendor-%{version}/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/restic/ad00ce7340d89dc13ccc59920ef75cb55af5b164 || :
cp %{_builddir}/restic-vendor-%{version}/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/restic/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785 || :
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
/usr/share/package-licenses/restic/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/restic/0e8f2042647b8140e79c4eb7d233d1b39231db09
/usr/share/package-licenses/restic/0f1cfab3f5481834d4f073129376589fe305c5f7
/usr/share/package-licenses/restic/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/restic/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/restic/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/restic/1ab6cff82ebc6ddb590da08bf488874f0b674d64
/usr/share/package-licenses/restic/2510861d72bd971c91b53a5c5fc291e2971c669e
/usr/share/package-licenses/restic/2a1a5c359d4a8f86d77f7cdd6b4af6583ce0db2e
/usr/share/package-licenses/restic/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/restic/2bda142bd58fd76f408cf18fa997d8fab0278a22
/usr/share/package-licenses/restic/308c47a3ea356402d2d14241da9a9f64cf404008
/usr/share/package-licenses/restic/34418523d96f6abcdf613b70f532649c3f49f679
/usr/share/package-licenses/restic/41a17a069904e6a10fa1b1bcf67c2e4d836937d1
/usr/share/package-licenses/restic/475b0ccf682da5e05e3aa1eb6146b30132ae717d
/usr/share/package-licenses/restic/4b5f40487c165cf31691824a93d375fcb65ea30a
/usr/share/package-licenses/restic/565471fdf06cfb21b7c69c5fc329a1341d5d9ad0
/usr/share/package-licenses/restic/5e975d829f4ea420c028ba512f8bb3e0ebaaf574
/usr/share/package-licenses/restic/62446e71c226403f1a2e67d0f66ede03e3fbdd2f
/usr/share/package-licenses/restic/646a9ad075072bb41132a4a0a2ceebbb457dda0c
/usr/share/package-licenses/restic/68645af047dcb3bcca960d2c1b1ece30a7141f76
/usr/share/package-licenses/restic/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/restic/71a24b258c1c84ec9cb58aa6174e62477ae0af0b
/usr/share/package-licenses/restic/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/restic/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/restic/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/restic/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/restic/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/restic/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
/usr/share/package-licenses/restic/8fb789d383906a5e83d6a74149e094f8d6921812
/usr/share/package-licenses/restic/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/restic/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/restic/9af8d79ca96a43a2c76c79f32c0366c0ea64fdfd
/usr/share/package-licenses/restic/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/restic/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/restic/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/restic/ab32a5c14ccc0a6d38e173568a5577493e3f6870
/usr/share/package-licenses/restic/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/restic/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/restic/b4b35a8138ee83256aca752d3813d3d0757d8380
/usr/share/package-licenses/restic/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/restic/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a
/usr/share/package-licenses/restic/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/restic/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/restic/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/restic/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
/usr/share/package-licenses/restic/ece3df1263c100f93c427face535a292723d38e7
/usr/share/package-licenses/restic/f63616ea1c9a1092cfea2c3c18309e3d1b67a9c9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/restic-backup.1
/usr/share/man/man1/restic-cache.1
/usr/share/man/man1/restic-cat.1
/usr/share/man/man1/restic-check.1
/usr/share/man/man1/restic-copy.1
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
