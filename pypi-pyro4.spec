#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyro4
Version  : 4.82
Release  : 40
URL      : https://files.pythonhosted.org/packages/2e/0b/e1066a2ba154a1fd6ade41b35d38482fc399feb90fe4768ce8d6d3eb368c/Pyro4-4.82.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/0b/e1066a2ba154a1fd6ade41b35d38482fc399feb90fe4768ce8d6d3eb368c/Pyro4-4.82.tar.gz
Summary  : distributed object middleware for Python (RPC)
Group    : Development/Tools
License  : MIT
Requires: pypi-pyro4-bin = %{version}-%{release}
Requires: pypi-pyro4-license = %{version}-%{release}
Requires: pypi-pyro4-python = %{version}-%{release}
Requires: pypi-pyro4-python3 = %{version}-%{release}
Requires: pypi(serpent)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(selectors34)
BuildRequires : pypi(serpent)

%description
[![Latest Version](https://img.shields.io/pypi/v/Pyro4.svg)](https://pypi.python.org/pypi/Pyro4/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyro4/badges/version.svg)](https://anaconda.org/conda-forge/pyro4)

%package bin
Summary: bin components for the pypi-pyro4 package.
Group: Binaries
Requires: pypi-pyro4-license = %{version}-%{release}

%description bin
bin components for the pypi-pyro4 package.


%package license
Summary: license components for the pypi-pyro4 package.
Group: Default

%description license
license components for the pypi-pyro4 package.


%package python
Summary: python components for the pypi-pyro4 package.
Group: Default
Requires: pypi-pyro4-python3 = %{version}-%{release}

%description python
python components for the pypi-pyro4 package.


%package python3
Summary: python3 components for the pypi-pyro4 package.
Group: Default
Requires: python3-core
Provides: pypi(pyro4)
Requires: pypi(serpent)

%description python3
python3 components for the pypi-pyro4 package.


%prep
%setup -q -n Pyro4-4.82
cd %{_builddir}/Pyro4-4.82
pushd ..
cp -a Pyro4-4.82 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399973
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyro4
cp %{_builddir}/Pyro4-4.82/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyro4/28687233f8a681dc4d5979e85b98d6231a800839
cp %{_builddir}/Pyro4-4.82/docs/source/license.rst %{buildroot}/usr/share/package-licenses/pypi-pyro4/d4c0c8299052f2e2089f956acbbb99f2a6ea77c1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyro4-check-config
/usr/bin/pyro4-flameserver
/usr/bin/pyro4-httpgateway
/usr/bin/pyro4-ns
/usr/bin/pyro4-nsc
/usr/bin/pyro4-test-echoserver

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyro4/28687233f8a681dc4d5979e85b98d6231a800839
/usr/share/package-licenses/pypi-pyro4/d4c0c8299052f2e2089f956acbbb99f2a6ea77c1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
