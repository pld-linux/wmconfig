#
# Conditional build:
# bcond_off_gnome - without GNOME support
#
Summary:	Window Manager Configurator
Summary(de):	Window Manager Configurator 
Summary(fr):	Configurateur de gestionnaires de fenêtres
Summary(pl):	Konfigurator zarz±dców okien
Summary(tr):	Pencere denetleyicisi ayarlarý
Name:		wmconfig
Version:	0.9.9
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://ftp.redhat.com/home/gafton/wmconfig/%{name}-%{version}.tar.gz
Patch0:		wmconfig-GNOME_path.patch
Patch1:		wmconfig-man.patch.gz
Patch2:		wmconfig-config.patch
Patch3:		wmconfig-input.patch
Patch4:		wmconfig-gnomelibs.patch
Patch5:		wmconfig-pre-post.patch
Patch6:		wmconfig-applnk.patch
BuildRequires:	glib-devel
%{!?bcond_off_gnome:BuildRequires:	gnome-libs-static}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a program that will generate menu configurations for different
window managers available for the X11 system. It is an attempt to gain
some form of abstractization of the menu configuration across some
window managers. Currently it supports: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%description -l pl
Ten program u³atwia konfigurowanie menu w ró¿nych zarz±dcach okien
dostêpnych dla systemu X11. W tej chwili jest wspierany przez
nastêpuj±ce programy: FVWM2, FVWM95, AfterStep, MWM, IceWM, KDE i
WindowMaker.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
LDFLAGS="-s -L%{_libdir}"; export LDFLAGS
%configure \
	%{!?bcond_off_gnome:--enable-gnome}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/X11/wmconfig}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/wmconfig
%{_mandir}/man1/*
