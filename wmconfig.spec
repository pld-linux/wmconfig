Summary:	Window Manager Configurator
Summary(de):	Window Manager Configurator 
Summary(fr):	Configurateur de gestionnaires de fen�tres
Summary(pl):	Konfigurator zarz�dc�w okien
Summary(tr):	Pencere denetleyicisi ayarlar�
Name:		wmconfig
Version:	0.9.3
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source:		ftp://ftp.redhat.com/home/gafton/wmconfig/%{name}-%{version}.tar.gz
Patch0:		wmconfig-GNOME_path.patch
Patch1:		wmconfig-man.patch.gz
Patch2:		wmconfig-config.patch
Buildroot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is a program that will generate menu configurations for different 
window managers available for the X11 system. It is an attempt to gain some
form of abstractization of the menu configuration across some window managers.
Currently it supports: FVWM2, FVWM95, Afterstep, MWM, IceWM, KDE,
WindowMaker.

%description -l pl
Ten program u�atwia konfigurowanie menu w r�nych zarz�dcach okien
dost�pnych dla systemu X11. W tej chwili jest wspierany przez nast�puj�ce
programy: FVWM2, FVWM95, AfterStep, MWM, IceWM, KDE i WindowMaker.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s -L/usr/X11R6/lib" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-gnome
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/X11/wmconfig}

make DESTDIR=$RPM_BUILD_ROOT install-strip

gzip -9nf AUTHORS README TODO ChangeLog \
	$RPM_BUILD_ROOT%{_mandir}/man1/wmconfig.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/wmconfig
%{_mandir}/man1/wmconfig.1.*

%dir /etc/X11/wmconfig
