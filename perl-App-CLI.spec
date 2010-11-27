%define upstream_name	 App-CLI
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Dispatcher module for command line interface programs 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.bz2

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
%setup -q -n %{upstream_name}-%{upstream_version}
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
