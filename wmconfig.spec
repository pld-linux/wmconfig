Summary:     Window Manager Configurator
Summary(de): Window Manager Configurator 
Summary(fr): Configurateur de gestionnaires de fenêtres
Summary(tr): Pencere denetleyicisi ayarlarý
Name:        wmconfig
Version:     0.5
Release:     2
Copyright:   GPL
Group:       X11/Window Managers
Source:      ftp://ftp.redhat.com/home/gafton/wmconfig/%{name}-%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a program that will generate menu configurations for different 
window managers available for the X11 system. It is an attempt to gain some
form of abstractization of the menu configuration across some window managers.
Currently it supports: FVWM2, FVWM95, Afterstep, MWM, IceWM, KDE,
WindowMaker.

%prep
%setup -q -c 

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/man/man1}
make install TOP_DIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/man/man1/wmconfig.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) %dir /etc/X11/wmconfig
%attr(755, root, root) /usr/X11R6/bin/wmconfig
%attr(755, root, root) /usr/X11R6/man/man1/wmconfig.1

%changelog
* Sun Sep 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.5-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} in Source,
- removed COPYRIGHT from %doc (copyright statment is in Copyright field),
- updated %description,
- man page for wmconfig moved to /usr/X11R6/man/man1,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 0.4

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- version 0.3 is out...

* Fri Oct 17 1997 Cristian Gafton <gafton@redhat.com>
- updated to 0.2

* Thu Oct 09 1997 Cristian Gafton <gafton@redhat.com>
- build against glibc; first release
