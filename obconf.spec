Summary:	Openbox preferences manager
Name:		obconf
Version:	2.0.3
Release:	%mkrel 10
Source0:	http://openbox.org/dist/obconf/%name-%version.tar.gz

Patch0:		obconf-2.0.3-openbox3.5.patch
Patch1:		obconf-2.0.3-openbox3.5-part2.patch
Patch2:		obconf-2.0.3-preview_update-missing-argument.patch
Patch3:		obconf-2.0.3-load-rc.patch
Patch4:		obconf-2.0.3-link.patch
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://openbox.org/wiki/Obconf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf automake libtool gettext-devel
BuildRequires:	startup-notification-devel, openbox-devel, gtk+2-devel, libglade2.0-devel 
BuildRequires:	desktop-file-utils
Requires:	openbox

%description
ObConf is a graphical configuration tool for the Openbox window manager.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0

%build
autoreconf -fi
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


%changelog
* Mon Mar 26 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 2.0.3-10rosa.lts2012.0
- upstream patches for openbox 3.5 compatibility
- fix load rc.xml config file
- fix a crash due to missing argument to function

* Sat Jun 18 2011 Александр Казанцев <kazancas@mandriva.org> 2.0.3-9mdv2011.0
+ Revision: 685942
- update translations and delete unused plugins

* Sun May 01 2011 Александр Казанцев <kazancas@mandriva.org> 2.0.3-8
+ Revision: 661293
-add patch for desktop and mime-type files
- add russian translate, missing in master branch

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-7mdv2011.0
+ Revision: 613115
- the mass rebuild of 2010.1 packages

* Thu Jun 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0.3-6mdv2010.1
+ Revision: 547855
- change url and source to current location
- clean spec

* Fri May 14 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.0.3-5mdv2010.1
+ Revision: 544738
- fix .desktop file

* Sat Dec 12 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0.3-4mdv2010.1
+ Revision: 477580
- change Url (the former one was an archive)
- $RPM_BUILD_ROOT -> %%{buildroot}

* Thu May 21 2009 Jérôme Brenier <incubusss@mandriva.org> 2.0.3-3mdv2010.0
+ Revision: 378224
- fix license (GPLv2+)

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 2.0.3-2mdv2009.0
+ Revision: 200704
- rebuild

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 2.0.3-1mdv2009.0
+ Revision: 200688
- New version 2.0.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Lev Givon <lev@mandriva.org> 1.6-1mdv2008.0
+ Revision: 13738
- Update to 1.6.


* Wed Feb 08 2006 Lev Givon <lev@mandriva.org> 1.5-1mdk
- Package for Mandriva

