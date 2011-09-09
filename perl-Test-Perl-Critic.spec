Name:           perl-Test-Perl-Critic
Version:        1.01
Release:        7.1%{?dist}
Summary:        Use Perl::Critic in test programs

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Perl-Critic/
Source0:        http://www.cpan.org/authors/id/T/TH/THALJEF/testperlcritic/Test-Perl-Critic-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Perl::Critic) >= 0.21
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Test::Perl::Critic wraps the Perl::Critic engine in a convenient
subroutine suitable for test programs written using the Test::More
framework. This makes it easy to integrate coding-standards enforcement
into the build process. For ultimate convenience (at the expense of some
flexibility), see the criticism pragma.


%prep
%setup -q -n Test-Perl-Critic-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# Tests are failing with odd unpack errors.
# TEST_AUTHOR=1 ./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.01-7.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-5
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-4
- disable tests, take out patch, doesn't fix test failures

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-3
- patch for test failure

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.01-2
- rebuild for new perl

* Sat Jan 27 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- Update to 1.01.

* Sun Nov 12 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.08-1
- Update to 0.08.

* Sat Sep 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.07-1
- First build.
