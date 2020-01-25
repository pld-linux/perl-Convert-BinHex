%define	pdir	Convert
%define	pnam	BinHex
Summary:	Convert::BinHex Perl module - support for BinHex format used on Macs
Summary(pl.UTF-8):	Moduł Perla Convert::PEM - obsługa formatu BinHex używanego na Macach
Name:		perl-Convert-BinHex
Version:	1.119
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba70ad1772abac6270078f28197a7961
URL:		http://search.cpan.org/dist/Convert-BinHex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BinHex is a format used by Macintosh for transporting Mac files safely
through electronic mail, as short-lined, 7-bit, semi-compressed data
streams. Ths module provides a means of converting those data streams
back into into binary data.

%description -l pl.UTF-8
BinHex jest formatem używanym na Macintoshach do bezpiecznego
przesyłania plików przez pocztę elektroniczną jako zakodowanych
7-bitowych strumieni danych. Moduł dostarcza funkcjonalność
pozwalającą zamienić te strumienie danych z powrotem na pliki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs
%{perl_vendorlib}/Convert/BinHex.pm
%{_mandir}/man3/*
