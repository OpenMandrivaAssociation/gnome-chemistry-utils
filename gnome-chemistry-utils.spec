%define version 0.8.1
%define release %mkrel 1

%define major 	0
%define libname %mklibname gcu %major
%define develname %mklibname -d gcu

%define __libtoolize /bin/true

Summary:	Backend for Gnome chemistry applications
Name:		gnome-chemistry-utils
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.nongnu.org/gchemutils/

Source0:	http://savannah.nongnu.org/download/gchemutils/%{name}-%version.tar.bz2

BuildRequires:	libglade2.0-devel
BuildRequires:	libgnomeprint-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	libgoffice-devel
BuildRequires:	openbabel-devel >= 1.100.1
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui2-2-devel
BuildRequires:	gtk-doc
BuildRequires:  perl-XML-Parser
#BuildRequires:  mozilla-firefox-devel
BuildRequires:  gettext-devel
BuildRequires:  desktop-file-utils
BuildRequires:  chemical-mime-data
BuildRequires:	bodr
BuildRequires:	gnome-doc-utils
Requires:       chemical-mime-data
Requires:	bodr
Provides:	gcu = %{version}-%{release}
Provides:	gchemutils = %{version}-%{release}
Obsoletes:	gcu
Obsoletes:	gnome-crystal
Provides:	gnome-crystal

%description
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

%package -n %{libname}
Summary:	Main libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the library needed to run programs dynamically
linked with %{name}.       
                                                                                                                     
%package	-n %{develname}
Summary:	Development related files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname}%{major} = %{version}
Provides:	gcu-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description	-n %{develname}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package includes the header files and static libraries necessary for
developing chemistry related programs using %{name}.

#%package -n     %{name}-firefox-plugin
#Summary:        %{name} firefox plugin
#Group:          Networking/WWW
#Requires:       %{name} = %{version}-%{release}

#%description -n  %{name}-firefox-plugin
#This package is a set of chemical utils. Three programs are avaible:
#* A 3D molecular structure viewer (GChem3Viewer).
#* A Chemical calculator (GChemCalc).
#* A periodic table of the elements application (GChemTable).
#This package contains the mozilla plugin.


%prep
%setup -q

%build
%configure2_5x --disable-rpath --enable-static=no --disable-update-databases --disable-mozilla-plugin --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std HTMLDIR=`pwd`/reference/html

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Gnome" \
  --add-category="Science;Chemistry" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#kill intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gchemutils
  
%find_lang gchemutils

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%post
%update_menus
%{update_desktop_database}
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gcrystal.schemas > /dev/null

%postun
%clean_menus
%{clean_desktop_database}
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gcrystal.schemas > /dev/null

%postun -n %{libname}%{major} -p /sbin/ldconfig

%files -f gchemutils.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/gchemutils
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/mimelnk/application/*
%{_datadir}/gnome/help/*
%{_iconsdir}/hicolor/*/apps/gcrystal.png
%{_iconsdir}/hicolor/*/mimetypes/gnome-mime-application-x-gcrystal.png
%{_mandir}/man1/*.1.bz2
%{_mandir}/man3/*.3.bz2

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-, root, root)
%doc docs/reference
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

#%files -n %{name}-firefox-plugin
#%defattr(-, root, root)
#%{_libdir}/mozilla/plugins/*.so



