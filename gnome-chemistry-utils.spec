%define version 0.8.7
%define release %mkrel 3

%define major 	0
%define libname %mklibname gcu %major
%define develname %mklibname -d gcu

%define __libtoolize /bin/true

Summary:	Backend for Gnome chemistry applications
Name:		gnome-chemistry-utils
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		Sciences/Chemistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.nongnu.org/gchemutils/

Source0:	http://download.savannah.nongnu.org/releases/gchemutils/0.8/%{name}-%version.tar.bz2

BuildRequires:	libglade2.0-devel
BuildRequires:	libgnomeprint-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	goffice0-devel
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
Requires(post,preun): scrollkeeper
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
Requires:	%{libname} = %{version}-%{release}
Provides:	gcu-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gcu 0

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
%configure2_5x \
	--disable-rpath --enable-static=no --disable-update-databases \
	--disable-mozilla-plugin --disable-schemas-install \
	--disable-scrollkeeper
%make

%install
rm -rf %{buildroot}
%makeinstall_std HTMLDIR=`pwd`/reference/html

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#kill intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gchemutils
  
%find_lang gchemutils

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post
%update_menus
%{update_desktop_database}
%post_install_gconf_schemas gcrystal
%update_scrollkeeper
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas gcrystal

%if %mdkversion < 200900
%postun
%clean_menus
%{clean_desktop_database}
%clean_scrollkeeper
%clean_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f gchemutils.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/gchemutils
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/mimelnk/application/*
%{_datadir}/gnome/help/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.png
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/omf/*/*.omf

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc docs/reference
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

#%files -n %{name}-firefox-plugin
#%defattr(-, root, root)
#%{_libdir}/mozilla/plugins/*.so
