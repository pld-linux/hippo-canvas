Summary:	Originally built do display the Mugshot stacker
Name:		hippo-canvas
Version:	0.2.30
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hippo-canvas/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	903e4d1c833087fe9f6106712ababdb2
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libtool
BuildRequires:	libcroco-devel >= 0.6
BuildRequires:	pango-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Part of the Mugshot.org project.

%description -l pl.UTF-8
Część projektu Mugshot.org.

%package devel
Summary:	Header files for the hippo-canvas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hippo-canvas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 1.0.0
Requires:	glib2-devel >= 1:2.6.0

%description devel
Header files for the hippo-canvas library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hippo-canvas.

%package static
Summary:	Static hippo-canvas library
Summary(pl.UTF-8):	Statyczna biblioteka hippo-canvas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hippo-canvas library.

%description static -l pl.UTF-8
Statyczna biblioteka hippo-canvas.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhippocanvas-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhippocanvas-1.so.0
%attr(755,root,root) %{py_sitedir}/hippo.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhippocanvas-1.so
%{_libdir}/libhippocanvas-1.la
%{_gtkdocdir}/hippo-canvas
%{_includedir}/hippo-canvas-1
%{_pkgconfigdir}/hippo-canvas-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhippocanvas-1.a
%{py_sitedir}/hippo.a
