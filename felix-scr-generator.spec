%{?_javapackages_macros:%_javapackages_macros}
# Conditionals to help breaking org.apache.felix.scr.generator <-> org.apache.felix.scr.annotations dependency cycle
%if 0%{?fedora}
%bcond_with annotations
%endif

%global bundle    org.apache.felix.scr.generator

Name:          felix-scr-generator
Version:       1.16.0
Release:       2.1
Summary:       Descriptor Generator Implementation
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
%if %{without annotations}
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr.annotations)
%endif
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.osgi:org.osgi.compendium)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm-all)

%description
Provides the implementation to generate Declarative Services and Metatype
Service descriptors from Java 5 Annotations and/or JavaDoc tags.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}

%build
# tests skipped for circular dependency with org.apache.felix.scr.annotations
%mvn_build \
%if %{with annotations}
 -f \
%endif
 -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Mat Booth <mat.booth@redhat.com> - 1.16.0-1
- Update to latest upstream release and fix the bootstrap mode
- Regenerate BRs

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 gil cattaneo <puntogil@libero.it> 1.13.0-1
- update to 1.13.0

* Sun Feb 01 2015 gil cattaneo <puntogil@libero.it> 1.12.0-2
- introduce license macro

* Fri Jan 23 2015 gil cattaneo <puntogil@libero.it> 1.12.0-1
- update to 1.12.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 19 2013 gil cattaneo <puntogil@libero.it> 1.8.2-1
- update to 1.8.2

* Thu Aug 29 2013 gil cattaneo <puntogil@libero.it> 1.8.0-1
- update to 1.8.0

* Mon Jun 24 2013 gil cattaneo <puntogil@libero.it> 1.7.0-1
- update to 1.7.0

* Tue Apr 02 2013 gil cattaneo <puntogil@libero.it> 1.5.0-1
- update to 1.5.0

* Mon Jan 21 2013 gil cattaneo <puntogil@libero.it> 1.3.0-1
- initial rpm
