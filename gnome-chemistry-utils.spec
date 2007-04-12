%define version 0.6.4
%define release %mkrel 2

%define major 	0
%define libname %mklibname gcu

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
BuildRequires:	goffice21-devel
BuildRequires:	openbabel-devel >= 1.100.1
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui2-2-devel
BuildRequires:	gtk-doc
BuildRequires:  perl-XML-Parser
#BuildRequires:  mozilla-firefox-devel
BuildRequires:  gettext-devel
BuildRequires:  desktop-file-utils
BuildRequires:  chemical-mime-data
Requires:       chemical-mime-data
Provides:	gcu = %{version}-%{release}
Provides:	gchemutils = %{version}-%{release}
Obsoletes:	gcu

%description
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

%package -n %{libname}%{major}
Summary:	Main libraries for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}
Provides:	%{libname} = %{version}-%{release}

%description -n %{libname}%{major}
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related to
chemistry.  They are currently used in Gnome Crystal (gcrystal) and Gnome
Chemistry Paint (gchempaint).

This package contains the library needed to run programs dynamically
linked with %{name}.       
                                                                                                                     
%package	-n %{libname}%{major}-devel
Summary:	Development related files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname}%{major} = %{version}
Provides:	gcu-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libname}%{major}-devel
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
./configure --libdir=%_libdir --datadir=%_datadir --disable-rpath --enable-static=yes --disable-update-databases --disable-mozilla-plugin
#perl -pi -e 's@^(sys_lib_dlsearch_path_spec="/lib /usr/lib)"@$1 /usr/X11R6/%{_lib}"@' libtool
#perl -p -i -e 's|install-data-hook|||g' Makefile
%make

%install
rm -rf %{buildroot}
%makeinstall HTMLDIR=`pwd`/reference/html

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Gnome" \
  --add-category="X-MandrivaLinux-MoreApplications-Sciences-Chemistry;Science;Chemistry" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#kill intrusive docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/gchemutils
  
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -n %{libname}%{major} -p /sbin/ldconfig

%post
%update_menus
%{update_desktop_database}

%postun
%clean_menus
%{clean_desktop_database}

%postun -n %{libname}%{major} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/gchemutils
%{_datadir}/applications/*
%{_mandir}/man1/*.1.bz2
%{_mandir}/man3/*.3.bz2

%files -n %{libname}%{major}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{libname}%{major}-devel
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



