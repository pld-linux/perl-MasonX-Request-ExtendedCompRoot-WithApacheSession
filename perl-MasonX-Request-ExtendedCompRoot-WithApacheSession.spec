#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Request-ExtendedCompRoot-WithApacheSession
Summary:	Extend functionality of Mason's comp_root and add a session to the Mason Request object
Summary(pl):	Rozszerzenie funkcjonalno¶ci comp_root Masona i dodanie sesji do obiektu Mason Request
Name:		perl-MasonX-Request-ExtendedCompRoot-WithApacheSession
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cad52599a4d033be4ff9b00af96e6cba
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MasonX-Request-ExtendedCompRoot  >= 0.03
BuildRequires:	perl-MasonX-Request-WithApacheSession >= 0.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simply integrates MasonX::Request::ExtendedCompRoot and
MasonX::Request::WithApacheSession.

%description -l pl
Ten modu³ w prosty sposób integruje MasonX::Request::ExtendedCompRoot
oraz MasonX::Request::WithApacheSession.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*/*.pm
%{_mandir}/man3/*
