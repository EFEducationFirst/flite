Name:           flite
Version:        2.0.0
Release:        1%{?dist}
Summary:        Small, fast speech synthesis engine (text-to-speech)

Group:          Applications/Multimedia
License:        MIT
URL:            http://www.speech.cs.cmu.edu/flite/
Source0:        http://www.speech.cs.cmu.edu/flite/packed/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch4:         0001-auserver.c-Only-write-audio-data-to-a-file-in-debug-.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?el4}
# there is no texi2html for RHEL 4
%else
BuildRequires:  texi2html
%endif
BuildRequires:  ed alsa-lib-devel autoconf


%description
Flite (festival-lite) is a small, fast run-time speech synthesis engine
developed at CMU and primarily designed for small embedded machines and/or
large servers. Flite is designed as an alternative synthesis engine to
Festival for voices built using the FestVox suite of voice building tools.


%package devel
Summary: Development files for flite
Group: Development/Libraries
Requires: flite = %{version}-%{release}


%description devel
Development files for Flite, a small, fast speech synthesis engine.


%prep
%setup -q -n %{name}-%{version}
%patch4 -p1


%build
autoconf
%configure --enable-shared --with-audio=none
# This package fails parallel make (thus cannot be built using "_smp_flags")
make
# Build documentation
%if 0%{?el4}
# there is no texi2html for RHEL 4
%else
cd doc
make flite.html
%endif


%install
rm -rf %{buildroot}
make install INSTALLBINDIR=%{buildroot}%{_bindir} INSTALLLIBDIR=%{buildroot}%{_libdir}  INSTALLINCDIR=%{buildroot}%{_includedir}/flite
rm -rf %{buildroot}%{_libdir}/*.a


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%if 0%{?el4}
# there is no texi2html for RHEL 4
%doc ACKNOWLEDGEMENTS README COPYING README-ALSA.txt
%else
%doc ACKNOWLEDGEMENTS README COPYING doc/html
%endif
%{_libdir}/*.so.*
%{_bindir}/*


%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/flite
%{_libdir}/pkgconfig/flite.pc

%changelog
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan  6 2014 Rui Matos <rmatos@redhat.com> - 1.3-21
- Resolves: (CVE-2014-0027) flite: insecure temporary file use

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 14 2011 Francois Aucamp <faucamp@fedoraproject.org> - 1.3-16
- Added patch declaring explicit libm linking dependency (RHBZ #564899)
- Updated source and URL tags

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> - 1.3-13
- Removed moving of non-existing documentation flite directory

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 11 2008 Peter Lemenkov <lemenkov@gmail.com> - 1.3-11
- Fix for RHEL 4
 
* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-10
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-9
- Autorebuild for GCC 4.3

* Tue Nov 14 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-8
- Added comment to %%build stating why "_smp_flags" isn't used with make

* Mon Nov 13 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-7
- Modified alsa support patch file to patch "configure.in" instead of "configure"
- Added "autoconf" step to %%build
- Added BuildRequires: autoconf
- Fixed patch backup file suffixes
- Renamed patch files to a more standard format
- Moved header files from /usr/include to /usr/include/flite
- Added -p option to all cp operations (to preserve timestamps)

* Sun Nov 12 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-6
- Recreated patch to allow shared libraries to build correctly (sharedlibs.patch)
- "flite" and "flite_time" binaries now link to flite shared libraries (sharedlibs.patch)
- Simplified the documentation patch filename
- Modified patch steps in %%prep to create backup files with different suffixes
- Removed "_smp_flags" macro from %%build for all archs

* Fri Oct 20 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-5
- Modified "build" so that "_smp_flags" is only used for i386 arch

* Tue Oct 10 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-4
- Removed "_smp_flags" macro from "build" for x86_64 arch

* Tue Sep 26 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-3
- Added README-ALSA.txt (Source1)
- Removed subpackage: flite-devel-static
- Modified shared libraries patch (Patch0) to prevent building static libraries
- Renamed patch files: Patch0, Patch1

* Tue Sep 26 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-2
- Added flite 1.3 ALSA patch (Patch2) by Lukas Loehrer - thanks Anthony Green for pointing it out
- Added configure option: --with-audio=alsa
- Added BuildRequires: alsa-lib-devel

* Fri Sep 22 2006 Francois Aucamp <faucamp@csir.co.za> - 1.3-1
- Initial RPM build
