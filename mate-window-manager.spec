#define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname marco-private %{major}
%define develname %mklibname -d marco-private

Summary:	MATE window manager
Name:		mate-window-manager
Version:	1.4.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: mate-conf
BuildRequires: mate-dialogs
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(mateconf-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(pangoxft)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)

Requires: mate-dialogs

%description
MATE Window Manager is a simple window manager that integrates nicely with 
MATE. 

%package -n %{libname}
Summary:	Libraries for MATE Window Manager
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by MATE Window Manager.

%package -n %{develname}
Summary:	Libraries and include files with MATE Window Manager
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
This package provides the necessary development libraries and include 
files to allow you to develop with MATE Window Manager.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper

%make

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

%find_lang marco

%files -f marco.lang
%doc README COPYING NEWS HACKING 
%{_sysconfdir}/mateconf/schemas/marco.schemas
%{_bindir}/marco
%{_bindir}/marco-message
%{_bindir}/marco-theme-viewer
%{_bindir}/marco-window-demo
%{_datadir}/applications/marco.desktop
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/mate/wm-properties/marco-wm.desktop
%{_datadir}/marco
%dir %_datadir/mate/help/creating-marco-themes
%_datadir/mate/help/creating-marco-themes/C
%{_datadir}/themes/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmarco-private.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

