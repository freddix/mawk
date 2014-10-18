%define		snap	20100625

Summary:	An interpreter for the awk programming language
Name:		mawk
Version:	1.3.4
Release:	0.%{snap}.2
License:	GPL
Group:		Applications/Text
Source0:	ftp://invisible-island.net/mawk/%{name}-%{version}-%{snap}.tgz
# Source0-md5:	447e7c322fa1e58141f5085bae87351f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mawk is a version of the awk programming language. Awk interprets a
special-purpose programming language to do quick text pattern matching
and reformatting. Mawk improves on awk in certain ways and can
sometimes outperform gawk, the standard awk program for Linux. Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

%prep
%setup -qn %{name}-%{version}-%{snap}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

#ln -sf mawk $RPM_BUILD_ROOT%{_bindir}/awk
#echo ".so mawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGMENT CHANGES README
%attr(755,root,root) %{_bindir}/mawk
%{_mandir}/man1/*

