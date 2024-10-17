%define upstream_name	 App-CLI
%define upstream_version 0.313

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dispatcher module for command line interface programs 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Simple)
BuildRequires:	perl(Locale::Maketext::Simple)
BuildArch:	noarch

%description
App::CLI dispatches CLI (command line interface) based commands into command 
classes. It also supports subcommand and per-command options.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's/auto_install\(\)\;//' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/App
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.313.0-2mdv2011.0
+ Revision: 680469
- mass rebuild

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.313.0-1mdv2011.0
+ Revision: 612043
- update to new version 0.313

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 601858
- update to new version 0.31

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.103.0-1mdv2011.0
+ Revision: 595071
- update to new version 0.103

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 405955
- rebuild using %%perl_convert_version

* Fri Feb 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 345429
- update to new version 0.08

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 255317
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.07-1mdv2008.1
+ Revision: 136658
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.07-1mdv2008.0
+ Revision: 19182
-New version


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.06-1mdv2007.0
+ Revision: 73273
- import perl-App-CLI-0.06-1mdv2007.0

* Sun Jul 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.0
- New version 0.06

* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- New release 0.05

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdk
- New release 0.04
- spec cleanup
- better source URL
- better URL
- better buildrequires syntax

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-3mdk
- rebuild

* Thu Jan 19 2006 Michael Scherer <misc@mandriva.org> 0.03-2mdk
- Remove autoinstaller ( filling lbd system disk )
- fix BuildRequires

* Wed Jan 04 2006 Michael Scherer <misc@mandriva.org> 0.03-1mdk
- New release 0.03

* Wed Dec 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.02-3mdk
- Add BuildRequires

* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.02-2mdk
- Do not ship empty dir

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.02-1mdk
- New release 0.02

* Thu Sep 22 2005 Michael Scherer <misc@mandriva.org> 0.01-1mdk
- First mandriva package

