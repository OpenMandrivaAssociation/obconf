Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.3
Release:	%mkrel 8
Source0:	http://openbox.org/dist/obconf/%name-%version.tar.gz
Source1:	ru.po
Patch0:		obconf-2.0.3-desktop.patch
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	startup-notification-devel, openbox-devel, gtk+2-devel, libglade2.0-devel 
BuildRequires:	desktop-file-utils
Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q
%patch0 -p0 -b .desktop
cp %SOURCE1 ./po

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

# fix .desktop file
desktop-file-install --remove-key="Encoding" \
		--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README COPYING TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-openbox-theme.desktop
%{_datadir}/pixmaps/%{name}.png
