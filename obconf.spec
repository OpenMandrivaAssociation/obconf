%define name 	obconf
%define version 2.0.3
%define rel 5

Summary:	Openbox preferences manager
Name:    	%{name}
Version: 	%{version}
Release: 	%mkrel %{rel}
Source0: 	http://icculus.org/openbox/obconf/%name-%version.tar.gz
License: 	GPLv2+
Group:   	Graphical desktop/Other
Url:     	http://icculus.org/openbox/index.php/Obconf
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	openbox
BuildRequires:	startup-notification-devel, openbox-devel, gtk+2-devel, libglade2.0-devel 
BuildRequires:	desktop-file-utils

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

#fid .desktop file
desktop-file-install --remove-key="Encoding" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README COPYING TODO
%_bindir/*
%_datadir/*/*
