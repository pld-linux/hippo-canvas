Summary:	A canvas widget
Summary(pl.UTF-8):	Widget canvas
Name:		hippo-canvas
Version:	0.3.1
Release:	8
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hippo-canvas/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	dc19b95faef7daceb3c827d490bff8c3
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libcroco-devel >= 0.6
BuildRequires:	librsvg-devel >= 2.16.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.14.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pycairo-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The hippo-canvas library contains a canvas widget developed by the
Mugshot team for displaying GTK+ UI across multiple platforms.

%description -l pl.UTF-8
Biblioteka hippo-canvas zawiera widget canvas rozwijany przez zespół
Mugshot w celu wyświetlania UI w GTK+ na wielu platformach.

%package devel
Summary:	Header files for the hippo-canvas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hippo-canvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.0

%description devel
Header files for the hippo-canvas library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hippo-canvas.

%package static
Summary:	Static hippo-canvas library
Summary(pl.UTF-8):	Statyczna biblioteka hippo-canvas
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hippo-canvas library.

%description static -l pl.UTF-8
Statyczna biblioteka hippo-canvas.

%package apidocs
Summary:	The hippo-canvas library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki hippo-canvas
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
The hippo-canvas library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki hippo-canvas.

%package -n python-hippo-canvas
Summary:	hippo-canvas Python bindings
Summary(pl.UTF-8):	Wiązania Pythona dla hippo-canvas
Group:		Development/Languages/Python

%description -n python-hippo-canvas
hippo-canvas Python bindings.

%description -n python-hippo-canvas -l pl.UTF-8
Wiązania Pythona dla hippo-canvas.

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
	--enable-gtk-doc \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT{%{_libdir}/libhippocanvas*.la,%{py_sitedir}/hippo.{la,a}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhippocanvas-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhippocanvas-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhippocanvas-1.so
%{_includedir}/hippo-canvas-1
%{_pkgconfigdir}/hippo-canvas-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhippocanvas-1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/hippo-canvas

%files -n python-hippo-canvas
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/hippo.so
