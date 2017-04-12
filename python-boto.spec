%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define pkgname boto
%define buildid %{nil}

Summary:        A simple lightweight interface to Amazon Web Services
Name:           python-%{pkgname}
Version:        2.46.0
Release:        CROC8%{?buildid}%{?dist}
Epoch:          1441065600

Group:          Development/Languages
License:        MIT
URL:            http://github.com/C2Devel/boto
Source0:        %{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Provides:       %name = %version-%release

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__python2} setup.py build

%install
[ "%buildroot" = "/" ] || rm -rf "%buildroot"

%{__python2} setup.py install -O1 \
    --skip-build \
    --root "%buildroot" \
    --install-lib="%{python2_sitelib}"

%files
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/*
%{python2_sitelib}/*

%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"

%changelog
* Fri Apr 14 2017 Anton Vazhnetsov <dragen15051@gmail.com> - 2.46.1-CROC1
- Update to latest boto - 2.46.1
