%define module_name pydhcplib
%define shortname pydhcplib

%define name python-pydhcplib
%define release		%mkrel 1
Summary:    A python DHCP lib 
Name:		%name
Version:	0.6.2
Release:	%release
Source0:	http://pydhcplib.tuxfamily.org/download/pydhcplib-%{version}.tar.gz
License:	GPL
Group:		Development/Python
Url:		http://pydhcplib.tuxfamily.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
Requires:	python >= 2.5
BuildArch: noarch

%description
Pydhcplib is a pure python DHCP library. It permits to read/write and 
encode/decode DHCP packet on network. 

%prep
%setup -q -n %module_name-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc README
%{_mandir}/man3/*.3.*
%{_mandir}/man8/*.8.*
%{_mandir}/fr/man3/*.3.*
%{_bindir}/pydhcp
%{py_sitedir}/%{shortname}/
%{py_sitedir}/%{module_name}-%{version}-py%{pyver}.egg-info
