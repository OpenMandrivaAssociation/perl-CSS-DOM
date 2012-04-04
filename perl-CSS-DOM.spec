Name:		perl-CSS-DOM
Summary:	Perl module for Document Object Model for Cascading Style Sheets  
Version:	0.14
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~sprout/CSS-DOM/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/CSS-DOM-%{version}.tar.gz
BuildRequires:	perl-Exporter >= 5.57
BuildRequires:	perl-Encode >= 2.10
BuildRequires:	perl-Clone >= 0.09
BuildArch:	noarch

%description
This module implements a CSS-specific subset of the interfaces
described in the W3C DOM specification.

%prep
%setup -q -n CSS-DOM-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/CSS/DOM.pm
%{perl_vendorlib}/CSS/DOM/
%{_mandir}/man3/CSS::DOM*
