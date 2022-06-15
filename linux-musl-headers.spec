%define	basever	4.19.88
%define	postver	1
Summary:	Linux kernel headers for use with musl libc
Summary(pl.UTF-8):	Nagłówki jądra Linuksa do użytku z biblioteką musl
Name:		linux-musl-headers
Version:	%{basever}_%{postver}
Release:	1
License:	GPL v2
Group:		Development
Source0:	https://github.com/sabotage-linux/kernel-headers/releases/download/v%{basever}-%{postver}/linux-headers-%{basever}-%{postver}.tar.xz
# Source0-md5:	cf06522cb02523e8aa11646b0c252f88
URL:		https://github.com/sabotage-linux/kernel-headers
AutoReqProv:	no
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.568
BuildRequires:	rsync
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(pretrans):	coreutils
Obsoletes:	alsa-driver-devel
Obsoletes:	glibc-kernel-headers
Obsoletes:	glibc-kernheaders
Conflicts:	lm_sensors-devel < 2.8.2-2
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch ppc ppc64
%define	target_arch powerpc
%else
%ifarch x32
%define	target_arch x86_64
%else
%ifarch aarch64
%define	target_arch arm64
%else
%define	target_arch %{_target_base_arch}
%endif
%endif
%endif

# no objects to extract debug info from
%define		_enable_debug_packages	0

%description
This package includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs. The
header files define structures and constants that are needed for
building most standard programs with musl library.

%description -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe C, które definiują interfejs
między jądrem Linuksa a bibliotekami i programami działającymi w
przestrzeni użytkownika. Pliki nagłówkowe definiują struktury i stałe
potrzebne do zbudowania większości standardowych programów linkowanych
z biblioteką musl.

%prep
%setup -q -n linux-headers-%{basever}-%{postver}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix}-musl \
	DESTDIR=$RPM_BUILD_ROOT \
	ARCH=%{target_arch}

install -d $RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT%{_prefix}-musl/include $RPM_BUILD_ROOT%{_includedir}/musl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/musl
