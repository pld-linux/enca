#
# Conditional build:
%bcond_without	recode	# build without recode support
#
Summary:	Extremely Naive Charset Analyser
Summary(pl.UTF-8):   Skrajnie naiwny analizator zestawów znaków
Name:		enca
Version:	1.9
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://trific.ath.cx/Ftp/enca/%{name}-%{version}.tar.bz2
# Source0-md5:	b3581e28d68d452286fb0bfe58bed3b3
Patch0:		%{name}-libdir.patch
URL:		http://trific.ath.cx/software/enca/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	iconv
%{?with_recode:BuildRequires:	recode-devel}
Requires:	/bin/mktemp
Requires:	%{name}-libs = %{version}-%{release}
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
Summary(pl.UTF-8):   Biblioteka współdzielona Enca
Group:		Libraries

%description libs
This package contains shared Enca library other programs can make use
of.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną Enca, która może być
wykorzystywana przez inne programy.

%package devel
Summary:	Header files for ENCA library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki ENCA
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ENCA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ENCA.

%package static
Summary:	Static ENCA library
Summary(pl.UTF-8):   Statyczna biblioteka ENCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ENCA library.

%description static -l pl.UTF-8
Statyczna biblioteka ENCA.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	MKTEMP_PROG=/bin/mktemp \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1
echo '.so enca.1' > $RPM_BUILD_ROOT%{_mandir}/man1/enconv.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libexecdir}/enca
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc README.devel
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/libenca

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
