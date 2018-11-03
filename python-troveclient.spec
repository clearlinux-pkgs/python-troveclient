#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-troveclient
Version  : 2.17.0
Release  : 34
URL      : http://tarballs.openstack.org/python-troveclient/python-troveclient-2.17.0.tar.gz
Source0  : http://tarballs.openstack.org/python-troveclient/python-troveclient-2.17.0.tar.gz
Source99 : http://tarballs.openstack.org/python-troveclient/python-troveclient-2.17.0.tar.gz.asc
Summary  : Client library for OpenStack DBaaS API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-troveclient-bin = %{version}-%{release}
Requires: python-troveclient-license = %{version}-%{release}
Requires: python-troveclient-python = %{version}-%{release}
Requires: python-troveclient-python3 = %{version}-%{release}
Requires: Babel
Requires: Sphinx
Requires: httplib2
Requires: keystoneauth1
Requires: openstackdocstheme
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: python-mistralclient
Requires: python-swiftclient
Requires: reno
Requires: requests
Requires: simplejson
Requires: six
Requires: sphinxcontrib-apidoc
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
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

%description python3
python3 components for the python-troveclient package.


%prep
%setup -q -n python-troveclient-2.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541273195
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-troveclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-troveclient/LICENSE
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
/usr/share/package-licenses/python-troveclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
