Summary:	Menu generation tool
Summary(pl):	Narz�dzie do generowania menu
Name:		wmconfig
Version:	1.2.4
Release:	1
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.arrishq.net/downloads/%{name}-%{version}.tar.bz2
URL:		http://www.arrishq.net
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmconfig is a menu generation tool for various window managers and
desktop environments. See "wmconfig --help" for a list of 
supported window managers. It reads configuration files and outputs 
the menu file to stdout or - if supported - to files.

%description -l pl
Wmconfig jest narz�dziem do generowania menu dla r�nych zarz�dc�w
okien i �rodowisk. Aby zobaczy� list� obs�ugiwanych manager�w 
wykonaj polecenie "wmconfig --help". Wmconfig czyta pliki
konfiguracyjne i wy�wietla menu na ekranie lub (je�li jest to
obs�ugiwane) skierowuje je do pliku.

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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*

%{_mandir}/man1/*

%attr(755,root,root) %{_bindir}/*
