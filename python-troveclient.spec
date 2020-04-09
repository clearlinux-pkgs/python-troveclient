#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : python-troveclient
Version  : 3.3.1
Release  : 51
URL      : http://tarballs.openstack.org/python-troveclient/python-troveclient-3.3.1.tar.gz
Source0  : http://tarballs.openstack.org/python-troveclient/python-troveclient-3.3.1.tar.gz
Source1  : http://tarballs.openstack.org/python-troveclient/python-troveclient-3.3.1.tar.gz.asc
Summary  : Client library for OpenStack DBaaS API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-troveclient-bin = %{version}-%{release}
Requires: python-troveclient-license = %{version}-%{release}
Requires: python-troveclient-python = %{version}-%{release}
Requires: python-troveclient-python3 = %{version}-%{release}
Requires: Babel
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: python-mistralclient
Requires: python-swiftclient
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : coverage-python
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : keystoneauth1
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.utils
BuildRequires : oslotest
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mistralclient
BuildRequires : python-openstackclient-python
BuildRequires : python-swiftclient
BuildRequires : requests
BuildRequires : requests-mock-python
BuildRequires : simplejson
BuildRequires : six
BuildRequires : stestr
BuildRequires : stestr-python
BuildRequires : testscenarios
BuildRequires : tox
BuildRequires : virtualenv

%description
Python bindings to the OpenStack Trove API
==========================================

%package bin
Summary: bin components for the python-troveclient package.
Group: Binaries
Requires: python-troveclient-license = %{version}-%{release}

%description bin
bin components for the python-troveclient package.


%package license
Summary: license components for the python-troveclient package.
Group: Default

%description license
license components for the python-troveclient package.


%package python
Summary: python components for the python-troveclient package.
Group: Default
Requires: python-troveclient-python3 = %{version}-%{release}

%description python
python components for the python-troveclient package.


%package python3
Summary: python3 components for the python-troveclient package.
Group: Default
Requires: python3-core
Provides: pypi(python_troveclient)
Requires: pypi(prettytable)
Requires: pypi(python_mistralclient)
Requires: pypi(six)
Requires: pypi(requests)
Requires: pypi(simplejson)
Requires: pypi(keystoneauth1)
Requires: pypi(python_swiftclient)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.utils)
Requires: pypi(babel)
Requires: pypi(pbr)
Requires: pypi(osc_lib)

%description python3
python3 components for the python-troveclient package.


%prep
%setup -q -n python-troveclient-3.3.1
cd %{_builddir}/python-troveclient-3.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586448120
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-troveclient
cp %{_builddir}/python-troveclient-3.3.1/LICENSE %{buildroot}/usr/share/package-licenses/python-troveclient/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/trove

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-troveclient/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
