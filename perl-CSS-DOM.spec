%define upstream_name CSS-DOM
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Summary:	Perl module for Document Object Model for Cascading Style Sheets  
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~sprout/CSS-DOM/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Encode) >= 2.10
BuildRequires:	perl(Clone) >= 0.09
BuildArch:	noarch

%description
This module implements a CSS-specific subset of the interfaces
described in the W3C DOM specification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.14-1
+ Revision: 789154
- imported package perl-CSS-DOM

