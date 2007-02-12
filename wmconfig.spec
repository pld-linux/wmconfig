Summary:	Menu generation tool
Summary(pl.UTF-8):	Narzędzie do generowania menu
Name:		wmconfig
Version:	1.2.4
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.arrishq.net/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	60712272d1b31c871916459a10e4ffbc
URL:		http://www.arrishq.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmconfig is a menu generation tool for various window managers and
desktop environments. See "wmconfig --help" for a list of supported
window managers. It reads configuration files and outputs the menu
file to stdout or - if supported - to files.

%description -l pl.UTF-8
Wmconfig jest narzędziem do generowania menu dla różnych zarządców
okien i środowisk. Aby zobaczyć listę obsługiwanych zarządców okien
należy wydać polecenie "wmconfig --help". Wmconfig czyta pliki
konfiguracyjne i wyświetla menu na ekranie lub (jeśli jest to
obsługiwane) zapisuje menu do pliku.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure

%{__make} \
        CFLAGS="%{rpmcflags}" \
        LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
