# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		63ec47c5e295ad4f09d1df6d92afb7e10c3fec39
	%global commitdate	20150213
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.4
Release:	13
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
#Source0:	http://openbox.org/dist/obconf/%{name}-%{version}.tar.gz
Source0:	https://github.com/danakj/obconf/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
Patch0:		obconf-c99.patch

BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	locales-extra-charsets
BuildRequires:	openbox-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0),
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:	pkgconfig(obt-3.5)
BuildRequires:	pkgconfig(sm)

Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-openbox-theme.desktop
%{_datadir}/pixmaps/%{name}.png

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
export LDFLAGS="%{ldflags} `pkg-config --libs x11`"
autoreconf -fiv
%configure
%make_build

%install
%make_install

# .desktop
desktop-file-install \
	--delete-original \
	--remove-key="Encoding" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# locales
%find_lang %{name}

