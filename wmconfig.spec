Summary:	Window Manager Configurator
Summary(de):	Window Manager Configurator 
Summary(fr):	Configurateur de gestionnaires de fenêtres
Summary(pl):	Konfigurator zarz±dców okien
Summary(tr):	Pencere denetleyicisi ayarlarý
Name:		wmconfig
Version:	0.9.3
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		ftp://ftp.redhat.com/home/gafton/wmconfig/%{name}-%{version}.tar.gz
Patch0:		wmconfig-GNOME_patch.patch
Patch1:		wmconfig-man.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a program that will generate menu configurations for different 
window managers available for the X11 system. It is an attempt to gain some
form of abstractization of the menu configuration across some window managers.
Currently it supports: FVWM2, FVWM95, Afterstep, MWM, IceWM, KDE,
WindowMaker.

%description -l pl
Ten program u³atwia konfigurowanie menu w ró¿nych zarz±dcach okien
dostêpnych dla systemu X11. W tej chwili jest wspierany przez nastêpuj±ce
programy: FVWM2, FVWM95, AfterStep, MWM, IceWM, KDE i WindowMaker.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

make DESTDIR=$RPM_BUILD_ROOT install-strip

gzip -9nf AUTHORS README TODO ChangeLog \
	$RPM_BUILD_ROOT/usr/X11R6/man/man1/wmconfig.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO,ChangeLog}.gz

%attr(755,root,root) /usr/X11R6/bin/wmconfig
/usr/X11R6/man/man1/wmconfig.1.*

%changelog
* Wed Mar 31 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.9.2-2]
- fixed patch to GNOME application description (wmconfig-GNOME_patch.patch).

* Wed Mar 31 1999 Piotr Czerwiñski <pius@pld.org.pl>
- removed "%dir /etc/X11/wmconfig" from %files 
  (it comes with the filesystem package now).

* Tue Mar 30 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.9.2-1]
- updated to 0.9.2,
- removed -c %setup parameter,
- added using ./configure in %build,
- simplifications in %install,
- added using DESTDIR,
- added full %defattr description in %files,
- fixed %attr description,
- added documentation,
- cosmetic changes.

* Thu Feb 10 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.5-3]
- added Group(pl)
- added LDFLAGS=-s
- added pl translations
- added gzipping man page

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
