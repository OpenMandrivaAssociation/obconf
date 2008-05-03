%define name 	obconf
%define version 2.0.3
%define rel 2

Summary:	Openbox preferences manager
Name:    	%{name}
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://icculus.org/openbox/obconf/%name-%version.tar.gz
License: 	GPL
Group:   	Graphical desktop/Other
Url:     	http://tr.openmonkey.com/pages/obconf
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	openbox
BuildRequires: 	startup-notification-devel, openbox-devel, gtk+2-devel, libglade2.0-devel 

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q

%build
%configure2_5x
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

