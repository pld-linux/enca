Summary:	Extremely Naive Charset Analyser
Summary(pl):	Skrajnie naiwny analizator zestawów znaków
Name:		enca
Version:	1.3
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://trific.ath.cx/Ftp/enca/%{name}-%{version}.tar.bz2
# Source0-md5:	9682a14b429d487bc8fd852941b71d18
URL:		http://trific.ath.cx/software/enca/
BuildRequires:	automake
BuildRequires:	recode-devel
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

This package also contains shared Enca library other programs can make
use of.

%description -l pl
Enca to Extremely Naive Charset Analyser (skrajnie naiwny analizator
zestawów znaków). Wykrywa zestaw znaków i kodowanie plików tekstowych,
mo¿e tak¿e konwertowaæ do innych kodowañ przy u¿yciu wbudowanego
konwertera lub zewnêtrznych bibliotek i narzêdzi takich jak libiconv,
librecode czy cstocs.

Aktualnie obs³ugiwane s± znaki bia³oruskie, bu³garskie, chorwackie,
czeskie, estoñskie, litewskie, ³otewskie, polskie, rosyjskie,
s³owackie, s³oweñskie i ukraiñskie oraz niektóre kodowania
wielobajtowe (g³ównie warianty unikodu) niezale¿nie od jêzyka.

Ten pakiet zawiera tak¿e bibliotekê wspó³dzielon± Enca, która mo¿e byæ
wykorzystywana przez inne programy.

%package devel
Summary:	Header files for ENCA library
Summary(pl):	Pliki nag³ówkowe biblioteki ENCA
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for ENCA library.

%description devel -l pl
Pliki nag³ówkowe biblioteki ENCA.

%package static
Summary:	Static ENCA library
Summary(pl):	Statyczna biblioteka ENCA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static ENCA library.

%description static -l pl
Statyczna biblioteka ENCA.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/enca
%{_mandir}/man1/*

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
