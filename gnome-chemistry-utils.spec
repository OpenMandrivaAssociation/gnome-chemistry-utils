%define api	0.14
%define major 	0
%define libname %mklibname gcu %{api} %{major}
%define libgchempaint %mklibname gchempaint %{api} %{major}
%define libgcrystal %mklibname gcrystal %{api} %{major}

Summary:	Backend for Gnome chemistry applications
Name:		gnome-chemistry-utils
Version:	0.13.92
Release:	1
License:	LGPLv2+
Group:		Sciences/Chemistry
URL:		http://www.nongnu.org/gchemutils/
Source0:	http://download.savannah.nongnu.org/releases/gchemutils/%{api}/%{name}-%{version}.tar.xz
BuildRequires:	libgnomeprint-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	pkgconfig(libgoffice-0.10)
BuildRequires:	openbabel-devel >= 1.100.1
BuildRequires:	libgnomeui2-devel
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	gtk-doc
BuildRequires:  perl-XML-Parser
BuildRequires:  intltool
BuildRequires:  chemical-mime-data
BuildRequires:	bodr
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	chrpath
Provides:	gcu = %{EVRD}
Provides:	gchemutils = %{EVRD}
Obsoletes:	gcu < %{EVRD}
Obsoletes:	gchemutils < %{EVRD}
# fwang: the main package comes meta package since 0.10
Requires:	gchem3d = %{version}
Requires:	gchemcalc = %{version}
Requires:	gchempaint = %{version}
Requires:	gchemtable = %{version}
Requires:	gcrystal = %{version}
Requires:	gspectrum = %{version}

%description
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

%files
%defattr(-, root, root)
%doc README ChangeLog NEWS AUTHORS

#--------------------------------------------------------------------

%package common
Summary:	Common files shared by different components of %{name}
Group:		Sciences/Chemistry
Conflicts:	%{name} < %{version}
Requires:       chemical-mime-data
Requires:       bodr

%description common
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the common files ahred by different components of
%{name}.

%preun common
%preun_uninstall_gconf_schemas gchemutils

%files common -f gchemutils-%{api}.lang
%defattr(-, root, root)
#%{_sysconfdir}/gconf/schemas/gchemutils.schemas
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.gschema.xml
%dir %{_libdir}/gchemutils
%dir %{_libdir}/gchemutils/%{api}
%dir %{_libdir}/gchemutils/%{api}/plugins
%{_libdir}/gchemutils/%{api}/plugins/cdx
%{_libdir}/gchemutils/%{api}/plugins/cdxml
%{_libdir}/gchemutils/%{api}/plugins/cif
%{_libdir}/gchemutils/%{api}/plugins/cml
%{_libdir}/gchemutils/%{api}/plugins/ctfiles
%{_libdir}/gchemutils/%{api}/plugins/nuts
%dir %{_datadir}/gchemutils
%dir %{_datadir}/gchemutils/%{api}
%{_datadir}/gchemutils/%{api}/*.xml
%dir %{_datadir}/gchemutils/%{api}/pixmaps
%dir %{_datadir}/gchemutils/%{api}/ui
%{_datadir}/gchemutils/%{api}/ui/libgcu
%{_datadir}/mime/packages/*.xml
%{_libdir}/babelserver

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Main libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/libgcu-%{api}.so.%{major}*
%{_libdir}/libgcugtk-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libgchempaint}
Summary:        Libraries for gchempaint
Group:          System/Libraries

%description -n %{libgchempaint}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry. They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the library needed to run programs dynamically
linked with gchempaint.

%files -n %{libgchempaint}
%defattr(-, root, root)
%{_libdir}/libgcp-%{api}.so.%{major}*
%{_libdir}/libgccv-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n %{libgcrystal}
Summary:        Libraries for gchempaint
Group:          System/Libraries

%description -n %{libgcrystal}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry. They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the library needed to run programs dynamically
linked with gcrystal.

%files -n %{libgcrystal}
%defattr(-, root, root)
%{_libdir}//libgcrystal-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n gchempaint
Summary:        GNOME 2D chemical structure drawing tool
Group:          Sciences/Chemistry
Requires:	%{name}-common = %{version}
Suggests:	%{name}-goffice = %{version}
Conflicts:	%{name}-common < 0.10.1-2

%description -n gchempaint
GChemPaint is a 2D chemical structures editor for the Gnome-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server so
that some chemistry could be embedded in Gnome applications such as
Gnumeric and Abiword.

%preun -n gchempaint
%preun_uninstall_gconf_schemas gchempaint gchempaint-arrows

%files -n gchempaint
%defattr(-, root, root)
#%{_sysconfdir}/gconf/schemas/gchempaint-arrows.schemas
#%{_sysconfdir}/gconf/schemas/gchempaint.schemas
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.paint.plugins.arrows.gschema.xml
%{_bindir}/gchempaint*
%{_libdir}/gchemutils/%{api}/plugins/paint
%{_datadir}/applications/gchempaint*.desktop
%{_datadir}/gchemutils/%{api}/paint
%{_datadir}/gchemutils/%{api}/pixmaps/gchempaint_logo.*
%{_datadir}/gchemutils/%{api}/ui/paint
%{_datadir}/gnome/help/gchempaint-%{api}
%{_iconsdir}/hicolor/*/apps/gchempaint.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-gchempaint.*
%{_mandir}/man1/gchempaint*
%{_datadir}/omf/gchempaint-%{api}/gchempaint-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchem3d
Summary:        Molecules Viewer
Group:          Sciences/Chemistry
Requires:       %{name}-common = %{version}
Conflicts:	%{name} < %{version}

%description -n gchem3d
GChem3Viewer is a 3D molecular structure viewer.

%files -n gchem3d
%defattr(-, root, root)
%{_bindir}/gchem3d*
%{_datadir}/applications/gchem3d*.desktop
%{_datadir}/gnome/help/gchem3d-%{api}
%{_iconsdir}/hicolor/*/apps/gchem3d.*
%{_mandir}/man1/gchem3d*
%{_datadir}/omf/gchem3d-%{api}/gchem3d-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchemcalc
Summary:        Chemical calculator
Group:          Sciences/Chemistry
Requires:       %{name}-common = %{version}
Conflicts:	%{name} < %{version}

%description -n gchemcalc
GChemCalc is a Chemical calculator.

%files -n gchemcalc
%defattr(-, root, root)
%{_bindir}/gchemcalc*
%{_datadir}/applications/gchemcalc*.desktop
%{_datadir}/gchemutils/%{api}/ui/calc
%{_datadir}/gnome/help/gchemcalc-%{api}
%{_iconsdir}/hicolor/*/apps/gchemcalc.*
%{_mandir}/man1/gchemcalc*
%{_datadir}/omf/gchemcalc-%{api}/gchemcalc-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchemtable
Summary:        Periodic table
Group:          Sciences/Chemistry
Requires:       %{name}-common = %{version}
Conflicts:	%{name} < %{version}

%description -n gchemtable
GChemTable is a periodic table of the elements application.

%files -n gchemtable
%defattr(-, root, root)
%{_bindir}/gchemtable*
%{_datadir}/applications/gchemtable*.desktop
%{_datadir}/gnome/help/gchemtable-%{api}
%{_datadir}/gchemutils/%{api}/ui/table
%{_iconsdir}/hicolor/*/apps/gchemtable.*
%{_mandir}/man1/gchemtable*
%{_datadir}/omf/gchemtable-%{api}/gchemtable-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gcrystal
Summary:        Crystal structure viewer
Group:          Sciences/Chemistry
Requires:       %{name}-common = %{version}
Conflicts:	%{name} < %{version}

%description -n gcrystal
GCrystal is a Crystal structure viewer.

%preun -n gcrystal
%preun_uninstall_gconf_schemas gcrystal

%files -n gcrystal
%defattr(-, root, root)
#%{_sysconfdir}/gconf/schemas/gcrystal.schemas
%{_datadir}/glib-2.0/schemas/org.gnome.gchemutils.crystal.gschema.xml
%{_bindir}/gcrystal*
%{_datadir}/gchemutils/%{api}/pixmaps/gcrystal_logo.png
%{_datadir}/gchemutils/%{api}/ui/crystal
%{_datadir}/applications/gcrystal*.desktop
%{_datadir}/gnome/help/gcrystal-%{api}
%{_iconsdir}/hicolor/*/apps/gcrystal.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-gcrystal.*
%{_mandir}/man1/gcrystal*
%{_datadir}/omf/gcrystal-%{api}/gcrystal-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gspectrum
Summary:        Spectrum viewer
Group:          Sciences/Chemistry
Requires:       %{name}-common = %{version}
Conflicts:	%{name} < %{version}

%description -n gspectrum
GSpectrum is a Spectrum viewer.

%files -n gspectrum
%defattr(-, root, root)
%{_bindir}/gspectrum*
%{_datadir}/applications/gspectrum*.desktop
%{_datadir}/gnome/help/gspectrum-%{api}
%{_iconsdir}/hicolor/*/apps/gspectrum.*
%{_mandir}/man1/gspectrum*
%{_datadir}/omf/gspectrum-%{api}/gspectrum-%{api}-C.omf

#--------------------------------------------------------------------

%package goffice
Summary:        GOffice plugin for gchemutils
Group:          Sciences/Chemistry
Requires:       gchempaint = %{version}
Requires:	goffice

%description goffice
GOffice plugin for gchemutils.

%files goffice
%defattr(-, root, root)
%{_libdir}/goffice/*/plugins/gchemutils

#--------------------------------------------------------------------

%package	devel
Summary:	Development related files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Requires:	%{libgchempaint} = %{EVRD}
Requires:	%{libgcrystal} = %{EVRD}
Provides:	gcu-devel = %{EVRD}
Provides:	gchemutils-devel = %{EVRD}
Provides:	gchempaint-devel = %{EVRD}
Obsoletes:	%mklibname -d gcu 0
Obsoletes:	%{_lib}gcu-devel < %{version}
Obsoletes:	gchempaint-devel < %{version}

%description	devel
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package includes the header files and static libraries necessary for
developing chemistry related programs using %{name}.

%files devel
%defattr(-, root, root)
%doc docs/reference
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%define Werror_cflags %{nil}
export CXXFLAGS="%optflags -fpermissive"
%configure2_5x \
	--enable-static=no --disable-update-databases \
	--disable-mozilla-plugin --disable-schemas-install \
	--disable-scrollkeeper --without-kde-mime-dir
%make

%install
%makeinstall_std HTMLDIR=`pwd`/reference/html

#kill intrusive docs
rm -rf %{buildroot}%{_docdir}/gchemutils

#kill libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#kill rpaths
chrpath --delete  %{buildroot}%{_bindir}/*
chrpath --delete  %{buildroot}%{_libdir}/goffice/*/plugins/gchemutils/gchemutils.so
chrpath --delete  %{buildroot}%{_libdir}/*.so.*

%find_lang gchemutils-%{api}


%changelog
* Wed Sep 05 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.13.92-1
+ Revision: 816392
- update to 0.13.92

* Tue Jul 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.13.7-1
+ Revision: 807967
- update to 0.13.7 unstable release

* Thu Apr 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.12.11-1
+ Revision: 793503
- update to 0.12.11

  + Funda Wang <fwang@mandriva.org>
    - new version 0.12.10

* Mon Aug 15 2011 Funda Wang <fwang@mandriva.org> 0.12.9-1
+ Revision: 694572
- update file list
- new version 0.12.9

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 0.12.8-2
+ Revision: 676971
- rebuild for new goffice

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.12.8-1
+ Revision: 673396
- update to new version 0.12.8

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 0.12.7-2
+ Revision: 672317
- use -fpermissive
- rebuild

* Tue Feb 22 2011 Funda Wang <fwang@mandriva.org> 0.12.7-1
+ Revision: 639250
- update file list
- drop requires
- new version 0.12.7

* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 0.12.6-1mdv2011.0
+ Revision: 627667
- 0.12.6

* Thu Dec 02 2010 Funda Wang <fwang@mandriva.org> 0.12.5-2mdv2011.0
+ Revision: 604683
- rebuild for bs monster

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 0.12.5-1mdv2011.0
+ Revision: 601500
- update to new version 0.12.5

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.12.4-2mdv2011.0
+ Revision: 583368
- rebuild

* Mon Sep 27 2010 Funda Wang <fwang@mandriva.org> 0.12.4-1mdv2011.0
+ Revision: 581200
- update to new version 0.12.4

* Sun Sep 05 2010 Funda Wang <fwang@mandriva.org> 0.12.3-1mdv2011.0
+ Revision: 576058
- new version 0.12.3

* Sun Sep 05 2010 Funda Wang <fwang@mandriva.org> 0.12.2-3mdv2011.0
+ Revision: 576041
- rebuild for new goffice

* Sat Aug 07 2010 Funda Wang <fwang@mandriva.org> 0.12.2-2mdv2011.0
+ Revision: 567409
- rebuild for new goffice

* Sat Jul 24 2010 Funda Wang <fwang@mandriva.org> 0.12.2-1mdv2011.0
+ Revision: 557893
- New version 0.12.2

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 0.10.12-2mdv2010.1
+ Revision: 536038
- rebuild for new goffice

* Sun Feb 28 2010 Funda Wang <fwang@mandriva.org> 0.10.12-1mdv2010.1
+ Revision: 512703
- new version 0.10.12

* Sun Feb 14 2010 G√∂tz Waschk <waschk@mandriva.org> 0.10.11-2mdv2010.1
+ Revision: 505830
- rebuild for new goffice

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.10.11-1mdv2010.1
+ Revision: 500358
- New version 0.10.11

* Mon Jan 25 2010 Funda Wang <fwang@mandriva.org> 0.10.10-2mdv2010.1
+ Revision: 496277
- rebuild for new goffice

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 0.10.10-1mdv2010.1
+ Revision: 484506
- fix linkage
- new version 0.10.10

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 0.10.9-3mdv2010.1
+ Revision: 479460
- rebuild for new goffice

* Mon Nov 30 2009 Funda Wang <fwang@mandriva.org> 0.10.9-2mdv2010.1
+ Revision: 471623
- add upstream patch to build with latest goffice
- rebuild for new goffice

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 0.10.9-1mdv2010.1
+ Revision: 466121
- new version 0.10.9

* Tue Nov 10 2009 Funda Wang <fwang@mandriva.org> 0.10.8-4mdv2010.1
+ Revision: 463997
- rebuild for new goffice

* Mon Oct 12 2009 Funda Wang <fwang@mandriva.org> 0.10.8-3mdv2010.0
+ Revision: 456813
- rebuild for new goffice

* Tue Oct 06 2009 Funda Wang <fwang@mandriva.org> 0.10.8-2mdv2010.0
+ Revision: 454557
- rebuild for new goffice

* Mon Sep 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.8-1mdv2010.0
+ Revision: 432936
- Update to new versio n0.10.8
- Fix string format patch

  + Funda Wang <fwang@mandriva.org>
    - rebuild for new goffice

* Sun Aug 16 2009 Funda Wang <fwang@mandriva.org> 0.10.5-2mdv2010.0
+ Revision: 416885
- rebuild for new goffice

* Sun Jul 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.10.5-1mdv2010.0
+ Revision: 392596
- update to new version 0.10.5

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Thu Apr 23 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10.4-2mdv2009.1
+ Revision: 368869
- Rebuild

* Thu Mar 19 2009 Funda Wang <fwang@mandriva.org> 0.10.4-1mdv2009.1
+ Revision: 357639
- New version 0.10.4

* Thu Jan 08 2009 Funda Wang <fwang@mandriva.org> 0.10.3-1mdv2009.1
+ Revision: 327120
- New version 0.10.3

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 0.10.2-1mdv2009.1
+ Revision: 308407
- new version 0.10.2

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 0.10.1-3mdv2009.1
+ Revision: 307456
- fix requires

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.10.1-2mdv2009.1
+ Revision: 303670
- the configure script does not accept chrpath
- move gchempaint plugins into correct pacakge
- goffice plugin actually belongs to gchempaint

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 303649
- refactor g-c-u, one package per tool
- New version 0.10.1

* Mon Aug 11 2008 Emmanuel Andry <eandry@mandriva.org> 0.8.7-3mdv2009.0
+ Revision: 270697
- Rebuild for openbabel

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.8.7-2mdv2009.0
+ Revision: 266910
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Funda Wang <fwang@mandriva.org> 0.8.7-1mdv2009.0
+ Revision: 194515
- New version 0.8.7

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Sat Jan 26 2008 Funda Wang <fwang@mandriva.org> 0.8.6-1mdv2008.1
+ Revision: 158360
- remove wrongly added files
- New version 0.8.6

* Sun Dec 23 2007 Funda Wang <fwang@mandriva.org> 0.8.5-1mdv2008.1
+ Revision: 137270
- New version 0.8.5

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.8.4-2mdv2008.1
+ Revision: 109262
- rebuild for new lzma

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 0.8.4-1mdv2008.1
+ Revision: 105590
- update icon cache
- BR goffice 0.4
- clearify libmajor
- New version 0.8.4
- Rebuild against goffice 0.5

* Tue Jul 31 2007 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2008.0
+ Revision: 56839
- fix file list
- disable scrollkeeper update when building
- fix man page list
- New version 0.8.2

* Wed Jul 04 2007 Funda Wang <fwang@mandriva.org> 0.8.1-2mdv2008.0
+ Revision: 47798
- fix develpacakge requires

* Tue Jul 03 2007 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 47551
- fix file list
- Corrected desktop file
- New version

* Sun May 27 2007 Funda Wang <fwang@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 31766
- New upstream version

* Thu May 10 2007 Austin Acton <austin@mandriva.org> 0.7.96-1mdv2008.0
+ Revision: 26174
- buildrequires gnome-doc-utils
- move to beta branch
- gconf schemas
- new version


* Mon Feb 26 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.4-2mdv2007.0
+ Revision: 125727
- fix datadir path

* Sun Feb 25 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.4-1mdv2007.1
+ Revision: 125625
- buildrequires goffice21-devel
- New version 0.6.4
- xdg menu

  + J√©r√¥me Soyer <saispo@mandriva.org>
    - Import gnome-chemistry-utils

* Thu Sep 14 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.6.1-2mdv2007.0
- - Rebuild against DBUS

* Wed Apr 05 2006 Lenny Cartier <lenny@mandriva.com> 0.6.1-1mdk
- 0.6.1

* Sat Apr 01 2006 Austin Acton <austin@mandriva.org> 0.6.0-1mdk
- New release 0.6.0
- buildrequires goffice
- mozilla plugin doesn't seem to build

* Tue Feb 14 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.4.8-3mdk
- Fix BuildRequires

* Mon Feb 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.8-2mdk
- Don't package mime cache
- fix mime cache update

* Thu Feb 09 2006 Lenny Cartier <lenny@mandriva.com> 0.4.8-1mdk
- 0.4.8

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.4.4-2mdk
- drop libtoolize hack
- I guess it's just major version 0

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.4.4-1mdk
- New release 0.4.4

* Sun Jun 19 2005 Austin Acton <austin@mandriva.org> 0.4.3-1mdk
- New release 0.4.3
- source URL fix

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.3.2-2mdk 
- Rebuild with latest howl

* Mon Dec 13 2004 Austin Acton <austin@mandrake.org> 0.3.2-1mdk
- 0.3.2

* Sun Oct 10 2004 Austin Acton <austin@mandrake.org> 0.3.1-1mdk
- 0.3.1
- major 0.3

* Mon Aug 09 2004 Austin Acton <austin@mandrake.org> 0.3.0-1mdk
- 0.3.0

* Sun Jun 06 2004 Austin Acton <austin@mandrake.org> 0.2.5-1mdk
- 0.2.5

