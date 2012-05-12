#
# Conditional build:
%bcond_without	vala	# Vala API
#
Summary:	A GTK+ widget for VNC clients (GTK+ 2.x version)
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC (wersja dla GTK+ 2.x)
Name:		gtk-vnc
Version:	0.4.4
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-vnc/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	0c51bcbdf1530c4856f49ace7c8f709a
Patch0:		%{name}-codegen.patch
Patch1:		%{name}-libtool.patch
URL:		http://live.gnome.org/gtk-vnc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.2.0
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.10.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common
BuildRequires:	gnutls-devel >= 1.4.0
BuildRequires:	gobject-introspection-devel >= 0.9.4
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libview-devel >= 0.6.0
BuildRequires:	perl-Text-CSV
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygtk-devel >= 2:2.0.0
BuildRequires:	rpm-pythonprov
%{?with_vala:BuildRequires:	vala >= 0.14.0}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	libgvnc = %{version}-%{release}
Requires:	cairo >= 1.2.0
Requires:	gtk+2 >= 2:2.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package contains version for GTK+ 2.x.

%description -l pl.UTF-8
gtk-vnc to widget przeglądarki VNC dla GTK+. Jest skonstruowany z
użyciem korutyn, dzięki czemu mogą być w pełni asynchroniczne
pozostając jednowątkowymi.

Ten pakiet zawiera wersję dla GTK+ 2.x.

%package devel
Summary:	Header files for gtk-vnc library (GTK+ 2.x version)
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 2.x)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgvnc-devel = %{version}-%{release}
Requires:	cairo-devel >= 1.2.0
Requires:	gnutls-devel >= 1.4.0
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	xorg-lib-libX11-devel

%description devel
Header files for gtk-vnc library (GTK+ 2.x version).

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 2.x).

%package static
Summary:	Static gtk-vnc library (GTK+ 2.x version)
Summary(pl.UTF-8):	Statyczna biblioteka gtk-vnc (wersja dla GTK+ 2.x)
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libgvnc-static = %{version}-%{release}

%description static
Static gtk-vnc library (GTK+ 2.x version).

%description static -l pl.UTF-8
Statyczna biblioteka gtk-vnc (wersja dla GTK+ 2.x).

%package -n python-gtk-vnc
Summary:	Python bindings for the gtk-vnc library (GTK+ 2.x version)
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki gtk-vnc (wersja dla GTK+ 2.x)
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%requires_eq	python-libs

%description -n python-gtk-vnc
A module allowing use of the GTK+ VNC widget (GTK+ 2.x version) from
Python.

%description -n python-gtk-vnc -l pl.UTF-8
Moduł pozwalający na używanie widgetu GTK+ VNC (w wersji dla GTK+ 2.x)
z poziomu Pythona.

%package -n gtk3-vnc
Summary:	A GTK+ widget for VNC clients (GTK+ 3.x version)
Summary(pl.UTF-8):	Widget GTK+ dla klientów VNC
Group:		X11/Libraries
Requires:	libgvnc = %{version}-%{release}
Requires:	cairo >= 1.2.0
Requires:	gtk+3 >= 3.0.0

%description -n gtk3-vnc
gtk-vnc is a VNC viewer widget for GTK+. It is built using coroutines
allowing it to be completely asynchronous while remaining single
threaded.

This package contains version for GTK+ 3.x.

%description -n gtk3-vnc -l pl.UTF-8
gtk-vnc to widget przeglądarki VNC dla GTK+. Jest skonstruowany z
użyciem korutyn, dzięki czemu mogą być w pełni asynchroniczne
pozostając jednowątkowymi.

Ten pakiet zawiera wersję dla GTK+ 3.x.

%package -n gtk3-vnc-devel
Summary:	Header files for gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	cairo-devel >= 1.2.0
Requires:	gtk+3-devel >= 3.0.0
Requires:	gtk3-vnc = %{version}-%{release}
Requires:	libgvnc-devel = %{version}-%{release}
Requires:	xorg-lib-libX11-devel

%description -n gtk3-vnc-devel
Header files for gtk-vnc library (GTK+ 3.x version).

%description -n gtk3-vnc-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gtk-vnc (wersja dla GTK+ 3.x).

%package -n gtk3-vnc-static
Summary:	Static gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	Statyczna biblioteka gtk-vnc (wersja dla GTK+ 3.x)
Group:		X11/Development/Libraries
Requires:	gtk3-vnc-devel = %{version}-%{release}
Requires:	libgvnc-static = %{version}-%{release}

%description -n gtk3-vnc-static
Static gtk-vnc library (GTK+ 3.x version).

%description -n gtk3-vnc-static -l pl.UTF-8
Statyczna biblioteka gtk-vnc (wersja dla GTK+ 3.x).

%package -n vala-gtk3-vnc
Summary:	Vala API for gtk-vnc library (GTK+ 3.x version)
Summary(pl.UTF-8):	API języka Vala dla biblioteki gtk-vnc (wersja dla GTK+3)
Group:		Development/Languages
Requires:	gtk3-vnc-devel = %{version}-%{release}
Requires:	vala-libgvnc = %{version}-%{release}

%description -n vala-gtk3-vnc
Vala API for gtk-vnc library (GTK+ 3.x version).

%description -n vala-gtk3-vnc -l pl.UTF-8
API języka Vala dla biblioteki gtk-vnc (wersja dla GTK+3).

%package -n libgvnc
Summary:	A library for VNC clients
Summary(pl.UTF-8):	Biblioteka dla klientów VNC
Group:		X11/Libraries
Requires:	glib2 >= 1:2.28.0
Requires:	gdk-pixbuf2 >= 2.10.0
Requires:	gnutls >= 1.4.0

%description -n libgvnc
A library for VNC clients.

%description -n libgvnc -l pl.UTF-8
Biblioteka dla klientów VNC.

%package -n libgvnc-devel
Summary:	Header files for libgvnc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgvnc
Group:		X11/Development/Libraries
Requires:	libgvnc = %{version}-%{release}
Requires:	cyrus-sasl-devel
Requires:	glib2-devel >= 1:2.28.0
Requires:	gdk-pixbuf2-devel >= 2.10.0
Requires:	gnutls-devel >= 1.4.0
Requires:	libgcrypt-devel
Requires:	zlib-devel

%description -n libgvnc-devel
Header files for libgvnc library.

%description -n libgvnc-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgvnc.

%package -n libgvnc-static
Summary:	Static libgvnc library
Summary(pl.UTF-8):	Statyczna biblioteka libgvnc
Group:		X11/Development/Libraries
Requires:	libgvnc-devel = %{version}-%{release}

%description -n libgvnc-static
Static libgvnc library.

%description -n libgvnc-static -l pl.UTF-8
Statyczna biblioteka libgvnc.

%package -n vala-libgvnc
Summary:	Vala API for libgvnc library
Summary(pl.UTF-8):	API języka Vala dla biblioteki libgvnc
Group:		Development/Languages
Requires:	libgvnc-devel = %{version}-%{release}
Requires:	vala

%description -n vala-libgvnc
Vala API for libgvnc library.

%description -n vala-libgvnc -l pl.UTF-8
API języka Vala dla biblioteki libgvnc.

%package tools
Summary:	Command line tools for VNC
Summary(pl.UTF-8):	Narzędzia linii poleceń dla VNC
Group:		Applications/Networking
Requires:	libgvnc = %{version}-%{release}

%description tools
Command line utilities for interacting with VNC servers.

%description tools -l pl.UTF-8
Narzędzia linii poleceń do interakcji z serwerami VNC.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# force enums regeneration
touch src/vncconnection.h src/vncdisplay.h
mkdir gtk{2,3}
cd gtk2
../%configure \
	--with-gtk=2.0 \
	--with-libview \
	--enable-static \
	--disable-plugin \
	--disable-silent-rules
%{__make}
cd ../gtk3
# libview not ported to gtk+3
../%configure \
	--with-gtk=3.0 \
	--without-libview \
	--enable-static \
	--disable-plugin \
	--disable-silent-rules \
	%{!?with_vala:--disable-vala}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C gtk2 -j1 install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C gtk3 -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

install examples/gvncviewer.{c,js} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/gvncviewer.py $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n gtk3-vnc -p /sbin/ldconfig
%postun	-n gtk3-vnc -p /sbin/ldconfig

%post	-n libgvnc -p /sbin/ldconfig
%postun	-n libgvnc -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-1.0.so.0
%{_libdir}/girepository-1.0/GtkVnc-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-1.0.so
%{_includedir}/%{name}-1.0
%{_datadir}/gir-1.0/GtkVnc-1.0.gir
%{_pkgconfigdir}/%{name}-1.0.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-vnc-1.0.a

%files -n python-gtk-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtkvnc.so
%{_examplesdir}/python-%{name}-%{version}

%files -n gtk3-vnc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-vnc-2.0.so.0
%{_libdir}/girepository-1.0/GtkVnc-2.0.typelib

%files -n gtk3-vnc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk-vnc-2.0.so
%{_includedir}/gtk-vnc-2.0
%{_pkgconfigdir}/gtk-vnc-2.0.pc
%{_datadir}/gir-1.0/GtkVnc-2.0.gir

%files -n gtk3-vnc-static
%defattr(644,root,root,755)
%{_libdir}/libgtk-vnc-2.0.a

%if %{with vala}
%files -n vala-gtk3-vnc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gtk-vnc-2.0.deps
%{_datadir}/vala/vapi/gtk-vnc-2.0.vapi
%endif

%files -n libgvnc -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgvnc-1.0.so.0
%{_libdir}/girepository-1.0/GVnc-1.0.typelib

%files -n libgvnc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgvnc-1.0.so
%{_datadir}/gir-1.0/GVnc-1.0.gir
%{_includedir}/gvnc-1.0
%{_pkgconfigdir}/gvnc-1.0.pc

%files -n libgvnc-static
%defattr(644,root,root,755)
%{_libdir}/libgvnc-1.0.a

%if %{with vala}
%files -n vala-libgvnc
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gvnc-1.0.vapi
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gvnccapture
%{_mandir}/man1/gvnccapture.1*
