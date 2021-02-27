#
# Conditional build:
%bcond_without	apidocs	# disable gtk-doc
%bcond_without	recode	# build without recode support

Summary:	Extremely Naive Charset Analyser
Summary(pl.UTF-8):	Skrajnie naiwny analizator zestawów znaków
Name:		enca
Version:	1.19
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.cihar.com/enca/%{name}-%{version}.tar.xz
# Source0-md5:	a7a0c152658e012db701a48ae8b79525
URL:		http://cihar.com/software/enca/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.0}
BuildRequires:	iconv
BuildRequires:	libtool
%{?with_recode:BuildRequires:	recode-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
Requires:	/bin/mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enca is an Extremely Naive Charset Analyser. It detects character set
and encoding of text files and can also convert them to other
encodings using either a built-in converter or external libraries and
tools like libiconv, librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, and
Ukrainian and some multibyte encodings (mostly variants of Unicode)
independently on the language.

%description -l pl.UTF-8
Enca to Extremely Naive Charset Analyser (skrajnie naiwny analizator
zestawów znaków). Wykrywa zestaw znaków i kodowanie plików tekstowych,
może także konwertować do innych kodowań przy użyciu wbudowanego
konwertera lub zewnętrznych bibliotek i narzędzi takich jak libiconv,
librecode czy cstocs.

Aktualnie obsługiwane są znaki białoruskie, bułgarskie, chorwackie,
czeskie, estońskie, litewskie, łotewskie, polskie, rosyjskie,
słowackie, słoweńskie i ukraińskie oraz niektóre kodowania
wielobajtowe (głównie warianty unikodu) niezależnie od języka.

%package libs
Summary:	Shared Enca library
Summary(pl.UTF-8):	Biblioteka współdzielona Enca
Group:		Libraries

%description libs
This package contains shared Enca library other programs can make use
of.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną Enca, która może być
wykorzystywana przez inne programy.

%package devel
Summary:	Header files for ENCA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ENCA
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ENCA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ENCA.

%package static
Summary:	Static ENCA library
Summary(pl.UTF-8):	Statyczna biblioteka ENCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ENCA library.

%description static -l pl.UTF-8
Statyczna biblioteka ENCA.

%package apidocs
Summary:	ENCA library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki ENCA
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
ENCA library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki ENCA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	MKTEMP_PROG=/bin/mktemp \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1
echo '.so enca.1' > $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/enca
%attr(755,root,root) %{_bindir}/enconv
%attr(755,root,root) %{_libexecdir}/enca
%{_mandir}/man1/enca.1*
%{_mandir}/man1/enconv.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libenca.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libenca.so.0

%files devel
%defattr(644,root,root,755)
%doc DEVELOP.md
%attr(755,root,root) %{_libdir}/libenca.so
%{_libdir}/libenca.la
%{_includedir}/enca.h
%{_pkgconfigdir}/enca.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libenca.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libenca
%endif
