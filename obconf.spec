Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.3
Release:	10
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
Source0:	http://openbox.org/dist/obconf/%name-%version.tar.gz
Patch0:		obconf-2.0.3-openbox3.5.patch
Patch1:		obconf-2.0.3-openbox3.5-part2.patch
Patch2:		obconf-2.0.3-preview_update-missing-argument.patch
Patch3:		obconf-2.0.3-load-rc.patch
Patch4:		obconf-2.0.3-link.patch

BuildRequires:	startup-notification-devel
BuildRequires:	pkgconfig(obt-3.5)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	desktop-file-utils
Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

# fix .desktop file
desktop-file-install \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-openbox-theme.desktop
%{_datadir}/pixmaps/%{name}.png
