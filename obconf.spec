Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.4
Release:	7
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
Source0:	http://openbox.org/dist/obconf/%{name}-%{version}.tar.gz
Patch0:		obconf-2.0.3-link.patch
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	openbox-devel
BuildRequires:	pkgconfig(gtk+-2.0),
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q
%patch0 -p0
autoreconf -fi

%build
%configure2_5x
%make

%install
%makeinstall_std

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

