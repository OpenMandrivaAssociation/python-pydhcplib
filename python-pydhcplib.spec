%define module_name pydhcplib
%define shortname pydhcplib

Summary:    A python DHCP lib 
Name:		python-pydhcplib
Version:	0.6.2
Release:	3
Source0:	http://pydhcplib.tuxfamily.org/download/pydhcplib-%{version}.tar.gz
License:	GPL
Group:		Development/Python
Url:		http://pydhcplib.tuxfamily.org
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
python setup.py install --root=%{buildroot}

%files
%doc README
%{_mandir}/man3/*.3.*
%{_mandir}/man8/*.8.*
%{_mandir}/fr/man3/*.3.*
%{_bindir}/pydhcp
%{py_sitedir}/%{shortname}/
%{py_sitedir}/%{module_name}-%{version}-py%{py_ver}.egg-info


%changelog
* Sat Feb 12 2011 Guilherme Moro <guilherme@mandriva.com> 0.6.2-1mdv2011.0
+ Revision: 637428
- Initial release
- Created package structure for python-pydhcplib.

