%define version 0.12.8
%define release %mkrel 2

%define api	0.12
%define major 	0
%define libname %mklibname gcu %api %major
%define libgchempaint %mklibname gchempaint %api %major

Summary:	Backend for Gnome chemistry applications
Name:		gnome-chemistry-utils
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.nongnu.org/gchemutils/
Source0:	http://download.savannah.nongnu.org/releases/gchemutils/%api/%{name}-%version.tar.bz2
Patch1:		gnome-chemistry-utils-0.10.8-fix-str-fmt.patch
BuildRequires:	libgnomeprint-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	goffice-devel
BuildRequires:	openbabel-devel >= 1.100.1
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui2-2-devel
BuildRequires:	gtk-doc
BuildRequires:  perl-XML-Parser
BuildRequires:  intltool
BuildRequires:  chemical-mime-data
BuildRequires:	bodr
BuildRequires:	gnome-doc-utils
BuildRequires:	chrpath
Provides:	gcu = %{version}-%{release}
Provides:	gchemutils = %{version}-%{release}
Obsoletes:	gcu < %{version}-%{release}
Obsoletes:	gchemutils < %{version}-%{release}
# fwang: the main package comes meta package since 0.10
Requires:	gchem3d = %version
Requires:	gchemcalc = %version
Requires:	gchempaint = %version
Requires:	gchemtable = %version
Requires:	gcrystal = %version
Requires:	gspectrum = %version

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
Conflicts:	%name < %version
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
%_sysconfdir/gconf/schemas/gchemutils.schemas
%dir %_libdir/gchemutils
%dir %_libdir/gchemutils/%{api}
%dir %_libdir/gchemutils/%{api}/plugins
%_libdir/gchemutils/%{api}/plugins/cdx
%_libdir/gchemutils/%{api}/plugins/cdxml
%_libdir/gchemutils/%{api}/plugins/cif
%_libdir/gchemutils/%{api}/plugins/cml
%dir %_datadir/gchemutils
%dir %_datadir/gchemutils/%{api}
%_datadir/gchemutils/%{api}/*.xml
%dir %_datadir/gchemutils/%{api}/pixmaps
%dir %_datadir/gchemutils/%{api}/ui
%_datadir/gchemutils/%{api}/ui/libgcu
%_datadir/mime/packages/*.xml

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
%_libdir/libgcu-%{api}.so.%{major}*

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
%_libdir/libgcp-%{api}.so.%{major}*
%_libdir/libgccv-%{api}.so.%{major}*

#--------------------------------------------------------------------

%package -n gchempaint
Summary:        GNOME 2D chemical structure drawing tool
Group:          Sciences/Chemistry
Requires:	%name-common = %version
Suggests:	%name-goffice = %version
Conflicts:	%name-common < 0.10.1-2

%description -n gchempaint
GChemPaint is a 2D chemical structures editor for the Gnome-2 desktop.
GChemPaint is a multi-document application and will be a bonobo server so
that some chemistry could be embedded in Gnome applications such as
Gnumeric and Abiword.

%preun -n gchempaint
%preun_uninstall_gconf_schemas gchempaint gchempaint-arrows

%files -n gchempaint
%defattr(-, root, root)
%_sysconfdir/gconf/schemas/gchempaint-arrows.schemas
%_sysconfdir/gconf/schemas/gchempaint.schemas
%_bindir/gchempaint*
%_libdir/gchemutils/%{api}/plugins/paint
%_datadir/applications/gchempaint*.desktop
%_datadir/gchemutils/%{api}/paint
%_datadir/gchemutils/%{api}/pixmaps/gchempaint_logo.png
%_datadir/gchemutils/%{api}/ui/paint
%_datadir/gnome/help/gchempaint-%{api}
%_iconsdir/hicolor/*/apps/gchempaint.png
%_iconsdir/hicolor/*/mimetypes/application-x-gchempaint.png
%_mandir/man1/gchempaint.*
%_datadir/omf/gchempaint-%{api}/gchempaint-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchem3d
Summary:        Molecules Viewer
Group:          Sciences/Chemistry
Requires:       %name-common = %version
Conflicts:	%name < %version

%description -n gchem3d
GChem3Viewer is a 3D molecular structure viewer.

%files -n gchem3d
%defattr(-, root, root)
%_bindir/gchem3d*
%_datadir/applications/gchem3d*.desktop
%_datadir/gnome/help/gchem3d-%{api}
%_iconsdir/hicolor/*/apps/gchem3d.png
%_mandir/man1/gchem3d.*
%_datadir/omf/gchem3d-%{api}/gchem3d-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchemcalc
Summary:        Chemical calculator
Group:          Sciences/Chemistry
Requires:       %name-common = %version
Conflicts:	%name < %version

%description -n gchemcalc
GChemCalc is a Chemical calculator.

%files -n gchemcalc
%defattr(-, root, root)
%_bindir/gchemcalc*
%_datadir/applications/gchemcalc*.desktop
%_datadir/gchemutils/%{api}/ui/calc
%_datadir/gnome/help/gchemcalc-%{api}
%_iconsdir/hicolor/*/apps/gchemcalc.png
%_mandir/man1/gchemcalc.*
%_datadir/omf/gchemcalc-%{api}/gchemcalc-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gchemtable
Summary:        Periodic table
Group:          Sciences/Chemistry
Requires:       %name-common = %version
Conflicts:	%name < %version

%description -n gchemtable
GChemTable is a periodic table of the elements application.

%files -n gchemtable
%defattr(-, root, root)
%_bindir/gchemtable*
%_datadir/applications/gchemtable*.desktop
%_datadir/gnome/help/gchemtable-%{api}
%_datadir/gchemutils/%{api}/ui/table
%_iconsdir/hicolor/*/apps/gchemtable.png
%_mandir/man1/gchemtable.*
%_datadir/omf/gchemtable-%{api}/gchemtable-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gcrystal
Summary:        Crystal structure viewer
Group:          Sciences/Chemistry
Requires:       %name-common = %version
Conflicts:	%name < %version

%description -n gcrystal
GCrystal is a Crystal structure viewer.

%preun -n gcrystal
%preun_uninstall_gconf_schemas gcrystal

%files -n gcrystal
%defattr(-, root, root)
%_sysconfdir/gconf/schemas/gcrystal.schemas
%_bindir/gcrystal*
%_datadir/gchemutils/%{api}/pixmaps/gcrystal_logo.png
%_datadir/gchemutils/%{api}/ui/crystal
%_datadir/applications/gcrystal*.desktop
%_datadir/gnome/help/gcrystal-%{api}
%_iconsdir/hicolor/*/apps/gcrystal.png
%_iconsdir/hicolor/*/mimetypes/application-x-gcrystal.png
%_mandir/man1/gcrystal.*
%_datadir/omf/gcrystal-%{api}/gcrystal-%{api}-C.omf

#--------------------------------------------------------------------

%package -n gspectrum
Summary:        Spectrum viewer
Group:          Sciences/Chemistry
Requires:       %name-common = %version
Conflicts:	%name < %version

%description -n gspectrum
GSpectrum is a Spectrum viewer.

%files -n gspectrum
%defattr(-, root, root)
%_bindir/gspectrum*
%_datadir/applications/gspectrum*.desktop
%_datadir/gnome/help/gspectrum-%{api}
%_iconsdir/hicolor/*/apps/gspectrum.png
%_mandir/man1/gspectrum.*
%_datadir/omf/gspectrum-%{api}/gspectrum-%{api}-C.omf

#--------------------------------------------------------------------

%package goffice
Summary:        GOffice plugin for gchemutils
Group:          Sciences/Chemistry
Requires:       gchempaint = %version
Requires:	goffice

%description goffice
GOffice plugin for gchemutils.

%files goffice
%defattr(-, root, root)
%_libdir/goffice/*/plugins/gchemutils

#--------------------------------------------------------------------

%package	devel
Summary:	Development related files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgchempaint} = %{version}-%{release}
Provides:	gcu-devel = %{version}-%{release}
Provides:	gchemutils-devel = %{version}-%{release}
Provides:	gchempaint-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gcu 0
Obsoletes:	%{_lib}gcu-devel < %version
Obsoletes:	gchempaint-devel < %version

%description	devel
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package includes the header files and static libraries necessary for
developing chemistry related programs using %{name}.

%files devel
%defattr(-, root, root)
%doc docs/reference
%_libdir/*.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%define Werror_cflags %nil
export CXXFLAGS="%optflags -fpermissive"
%configure2_5x \
	--enable-static=no --disable-update-databases \
	--disable-mozilla-plugin --disable-schemas-install \
	--disable-scrollkeeper --without-kde-mime-dir
%make

%install
rm -rf %{buildroot}
%makeinstall_std HTMLDIR=`pwd`/reference/html

#kill intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gchemutils

#kill libtool archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#kill rpaths
chrpath --delete  %{buildroot}%{_bindir}/*
chrpath --delete  %{buildroot}%{_libdir}/goffice/*/plugins/gchemutils/gchemutils.so
chrpath --delete  %{buildroot}%{_libdir}/*.so.*

%find_lang gchemutils-%{api}

%clean
rm -rf %{buildroot}
