%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		python-opentsdbclient
Version:    XXX
Release:    XXX
Summary:	Python REST API of OpenTSDB
License:	ASL 2.0
URL:		http://launchpad.net/%{name}/

Source0:	http://tarballs.openstack.org/%{name}/%{name}-master.tar.gz

BuildArch:	noarch

BuildRequires:	python2-devel
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
BuildRequires:  git


%description
This is a python library that provides a REST client for OpenTSDB, The Scalable
Time Series Database. It can be used to post or query metrics.

%package tests
Summary:	Tests for the python REST API for OpenTSDB
Requires:	%{name} = %{version}-%{release}

%description tests
This package contains the python-opentsdb test files.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build

%install
%py2_install

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/opentsdbclient
%{python2_sitelib}/python_opentsdbclient-*.egg-info
%exclude %{python2_sitelib}/opentsdbclient/tests

%files tests
%license LICENSE
%{python2_sitelib}/opentsdbclient/tests

%changelog
