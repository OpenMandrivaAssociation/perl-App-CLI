%define module	App-CLI
%define name	perl-%{module}
%define version 0.07
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Dispatcher module for command line interface programs 
Url:            http://search.cpan.org/dist/%module/
Source:		http://www.cpan.org/modules/by-module/App/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
App::CLI dispatches CLI (command line interface) based commands into command 
classes. It also supports subcommand and per-command options.

%prep
%setup -q -n %{module}-%{version}
perl -pi -e 's/auto_install\(\)\;//' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/App
%{_mandir}/man3/*



