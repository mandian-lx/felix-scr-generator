%{?_javapackages_macros:%_javapackages_macros}
%global project   felix
%global bundle    org.apache.felix.scr.generator
Name:          felix-scr-generator
Version:       1.8.2
Release:       2.2
Summary:       Descriptor Generator Implementation
Group:         Development/Java
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: java-devel
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)

BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm-all)

# Test deps
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.mockito:mockito-all)
%if 0
# Circular deps
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.annotations)
%endif

BuildRequires: maven-local
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-site-plugin

BuildArch:     noarch

%description
Provides the implementation to generate Declarative Services and Metatype
Service descriptors from Java 5 Annotations and/or JavaDoc tags.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build

%mvn_file :%{bundle} %{project}/%{bundle}
# tests skipped for circular dependency with org.apache.felix:org.apache.felix.scr.annotations
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE changelog.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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
