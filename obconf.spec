%define name 	obconf
%define version 1.6
%define release 1

Summary:	Openbox preferences manager
Name:    	%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group:   	Graphical desktop/Other
Url:     	http://tr.openmonkey.com/pages/obconf
Requires: 	openbox
BuildRequires: 	startup-notification-devel, openbox-devel, gtk+2-devel, libglade2.0-devel 

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING TODO
%_bindir/*
%_datadir/*/*

