#
# Conditional build:
# _without_gnome - without GNOME support
#
Summary:	Window Manager Configurator
Summary(de):	Window Manager Configurator
Summary(es):	Configurador de Administradores de ventanas
Summary(fr):	Configurateur de gestionnaires de fenêtres
Summary(pl):	Konfigurator zarz±dców okien
Summary(pt_BR):	Configurador de gerenciadores de janelas
Summary(tr):	Pencere denetleyicisi ayarlarý
Name:		wmconfig
Version:	0.9.10
Release:	11
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.redhat.com/home/gafton/wmconfig/%{name}-%{version}.tar.gz
Source1:	%{name}-README.PLD
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-GNOME_path.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-input.patch
Patch4:		%{name}-gnomelibs.patch
Patch5:		%{name}-applnk.patch
Patch6:		%{name}-unicode.patch
Patch7:		%{name}-fvwm2-dynamic_menus.patch
Patch8:		%{name}-fvwm2-no_percent.patch
Patch9:		%{name}-blackbox_common.patch
Patch10:	%{name}-mwm.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
%{!?_without_gnome:BuildRequires:	gnome-libs-static}
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

%description -l es
Este es un programa que crea configuraciones de menú para diferentes
administradores de ventana disponibles para el sistema X11. Es un
intento de abstraer una configuración única entre estos diferentes
administradores. Actualmente soporta: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%description -l pl
Ten program u³atwia konfigurowanie menu w ró¿nych zarz±dcach okien
dostêpnych dla systemu X11. W tej chwili wspiera nastêpuj±ce programy:
FVWM2, FVWM95, Afterstep, MWM, IceWM, KDE, WindowMaker.

%description -l pt_BR
Este é um programa que gera configurações de menu para diferentes
gerenciadores de janela disponíveis para o sistema X11. É uma
tentativa de abstrair uma configuração única entre esses diferentes
gerenciadores. Atualmente suporta: FVWM2, FVWM95, Afterstep, MWM,
IceWM, KDE, WindowMaker.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0

%build
rm -f acinclude.m4 missing
aclocal
%{__autoconf}
%{__automake}
LDFLAGS="%{rpmldflags} -L%{_libdir}"
%configure \
	%{!?_without_gnome:--enable-gnome}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/X11/wmconfig}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
cp %{SOURCE1} README.PLD
gzip -9nf AUTHORS README TODO ChangeLog README.PLD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/wmconfig
%{_mandir}/man1/*
