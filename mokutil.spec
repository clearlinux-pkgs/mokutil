#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mokutil
Version  : fb6250f23a1dda24000522f1994f70c73407c402
Release  : 1
URL      : https://github.com/lcp/mokutil/archive/fb6250f23a1dda24000522f1994f70c73407c402.tar.gz
Source0  : https://github.com/lcp/mokutil/archive/fb6250f23a1dda24000522f1994f70c73407c402.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: mokutil-bin = %{version}-%{release}
Requires: mokutil-data = %{version}-%{release}
Requires: mokutil-license = %{version}-%{release}
Requires: mokutil-man = %{version}-%{release}
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(efivar)
BuildRequires : pkgconfig(openssl)

%description
The utility to manipulate machines owner keys which managed in shim

%package bin
Summary: bin components for the mokutil package.
Group: Binaries
Requires: mokutil-data = %{version}-%{release}
Requires: mokutil-license = %{version}-%{release}

%description bin
bin components for the mokutil package.


%package data
Summary: data components for the mokutil package.
Group: Data

%description data
data components for the mokutil package.


%package license
Summary: license components for the mokutil package.
Group: Default

%description license
license components for the mokutil package.


%package man
Summary: man components for the mokutil package.
Group: Default

%description man
man components for the mokutil package.


%prep
%setup -q -n mokutil-fb6250f23a1dda24000522f1994f70c73407c402

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551221792
export LDFLAGS="${LDFLAGS} -fno-lto"
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1551221792
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mokutil
cp COPYING %{buildroot}/usr/share/package-licenses/mokutil/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mokutil

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/mokutil

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mokutil/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mokutil.1
