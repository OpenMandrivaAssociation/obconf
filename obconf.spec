Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.4
Release:	12
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
Source0:	http://openbox.org/dist/obconf/%{name}-%{version}.tar.gz
Patch0:		obconf-2.0.3-link.patch

BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	openbox-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0),
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:	pkgconfig(obt-3.5)

Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%files -f %{name}.lang
%doc AUTHORS README COPYING TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-openbox-theme.desktop
%{_datadir}/pixmaps/%{name}.png

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#autoreconf -fiv
%configure
%make_build

%install
%makei_nstall

# .desktop
desktop-file-install \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# locales
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
