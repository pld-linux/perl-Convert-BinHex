%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	BinHex
Summary:	Convert::BinHex Perl module - support for BinHex format used on Macs
Summary(pl):	Modu³ Perla Convert::PEM - wsparcie dla formatu BinHex u¿ywanego na Macach
Name:		perl-Convert-BinHex
Version:	1.119
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba70ad1772abac6270078f28197a7961
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BinHex is a format used by Macintosh for transporting Mac files safely
through electronic mail, as short-lined, 7-bit, semi-compressed data
streams. Ths module provides a means of converting those data streams
back into into binary data.

%description -l pl
BinHex jest formatem u¿ywanym na Macintoshach do bezpiecznego
przesy³ania plików przez pocztê elektroniczn± jako zakodowanych
7-bitowych strumieni danych. Modu³ dostarcza funkcjonalno¶æ
pozwalaj±c± zamieniæ te strumienie danych z powrotem na pliki.

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
