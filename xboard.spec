# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	An X Window System graphical chessboard
Name:		xboard
Version:	4.9.1
Release:	2
Group:		Games/Boards
URL:		http://www.gnu.org/software/xboard/
License:	BSD-like and GPLv2+

Source:		http://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	xboard.sh.bz2
Source2:	xboard-pxboard.man.bz2
Source3:	XBoard.ad.bz2

Requires:	chessengine
Conflicts:	gnuchess <= 5.06
BuildRequires:	flex
BuildRequires:	groff-for-man
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	texinfo

%description
Xboard is an X Window System based graphical chessboard which can be used with
the GNUchess and Crafty chess programs, with Internet Chess Servers (ICSs),
with chess via email, or with your own saved games.

%prep
%setup -q 
%apply_patches

chmod 0644 ChangeLog*

%build
%configure2_5x --bindir=%{_gamesbindir}
# Xaw3d kinda conflicts with Conectiva patch; no tooltip will be
# shown - Abel
# --with-Xaw3d
%make

%install
%makeinstall bindir=%{buildroot}%{_gamesbindir}

mv %{buildroot}%{_gamesbindir}/%{name} %{buildroot}%{_gamesbindir}/%{name}.real

bzip2 -dc %{SOURCE1} > %{buildroot}%{_gamesbindir}/%{name}
chmod 755 %{buildroot}%{_gamesbindir}/%{name}

# install pxboard manpage
bzip2 -dc %{SOURCE2} > %{buildroot}%{_mandir}/man6/pxboard.6

# install X resource
mkdir -p %{buildroot}%{_sysconfdir}/X11/app-defaults
bzip2 -dc %{SOURCE3} > %{buildroot}%{_sysconfdir}/X11/app-defaults/XBoard

# remove useless files
rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog* COPYRIGHT NEWS README zippy.README
%doc *.txt *.html
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XBoard
%config(noreplace) %{_sysconfdir}/xboard.conf
%{_datadir}/applications/*.desktop
%{_datadir}/games/%{name}
%{_datadir}/icons/*/*/*/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_gamesbindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 4.2.7-14mdv2011.0
+ Revision: 671273
- mass rebuild

* Fri Dec 03 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 4.2.7-13mdv2011.0
+ Revision: 606899
- Replace X11-devel BR for libxaw-devel
- Update package URL (moved)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.7-12mdv2010.1
+ Revision: 524372
- rebuilt for 2010.1

* Sat Mar 28 2009 Funda Wang <fwang@mandriva.org> 4.2.7-11mdv2009.1
+ Revision: 361873
- rediff entry patch
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 4.2.7-10mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 4.2.7-10mdv2008.1
+ Revision: 179545
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 4.2.7-9mdv2008.0
+ Revision: 76357
- rebuild for 2008
- don't package COPYING
- correct xdg menu categories
- use Fedora license policy
- bunzip2 patches
- Import xboard



* Fri Sep  1 2006 Olivier Blin <blino@mandriva.com> 4.2.7-8mdv2007.0
- XDG menu

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 4.2.7-7mdk
- Rebuild

* Thu Jul 14 2005 Abel Cheung <deaddog@mandriva.org> 4.2.7-6mdk
- Extend wrapper to launch sjeng too if other engines are not found

* Fri Jun 03 2005 Abel Cheung <deaddog@mandriva.org> 4.2.7-5mdk
- Extend wrapper to launch phalanx too if gnuchess not found
- Use small board by default, to fit small screens (Conectiva)
- Source2: pxboard man page (Debian)
- Source3: X resource file that adds tooltip to buttons, and adds
  3D feel even to Xaw widgets, without need of Xaw3d! (Conectiva)
- Patch1: properly quote variables inside cmail (Debian)
- Patch2: display timer in another color if time is tight (Debian)
- Patch3: use xvt script instead of xterm to display manpage/info
- Patch4: allow changing the label of some buttons (Conectiva)
- Patch5: highlight legal moves and threatened pieces, modified from
  http://members.optushome.com.au/stelliosk/xboard/

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 4.2.7-4mdk
- Rebuild with new menu

* Sat Aug 07 2004 Abel Cheung <deaddog@deaddog.org> 4.2.7-3mdk
- Requires chessengine instead of gnuchess only
- Wrapper script becomes longer, so place it in another file

* Thu Jul 15 2004 Michael Scherer <misc@mandrake.org> 4.2.7-2mdk 
- correct Requires

* Tue Dec 02 2003 Abel Cheung <deaddog@deaddog.org> 4.2.7-1mdk
- 4.2.7

* Wed Nov 19 2003 Abel Cheung <deaddog@deaddog.org> 4.2.6-8mdk
- Remove patch1 (gnuchessx is back)
- Add missing BuildRequires

* Wed Nov 12 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 4.2.6-7mdk
- fix Olivier Thauvin not even testing his package :) (#6320)

* Thu Oct 30 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.2.6-6mdk
- use %%_gamesbindir
- add wrapper to xboard to set correct path

* Thu Apr 24 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 4.2.6-5mdk
- fix %%doc section thx to stefan's robot

* Sat Jul 20 2002 Daouda LO <daouda@mandrakesoft.com> 4.2.6-4mdk
- apply patch from Olivier Thauvin

* Fri Mar 01 2002 David BAUDENS <baudens@mandrakesoft.com> 4.2.6-3mdk
- Don't hardcode icon PATH in menu
- Use standard boards_section.png for icons (so don't break E menu)

* Wed Feb 06 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.6-2mdk
- Use License: tag (sorry I missed that on first try).

* Wed Feb 06 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.6-1mdk
- 4.2.6 out for general consumption.
- Add a URL.

* Tue May  8 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 4.2.3-1mdk
- version 4.2.3

* Wed Feb 07 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.2-1mdk
- another new and shiny source.

* Tue Feb 06 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.1-1mdk
- new and shiny source.

* Sun Oct 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.1.0-1mdk
- new and shiny source.

* Wed Aug 16 2000 David BAUDENS <baudens@mandrakesoft.com> 4.0.7-5mdk
- Fix menu entry

* Wed Aug 16 2000 Enzo Maggi <enzo@mandrakesoft.com> 4.0.7-4mdk
- Minor bug fix in the spec

* Tue Aug 14 2000 Enzo Maggi <enzo@mandrakesoft.com> 4.0.7-3mdk
- introduced the %%{_mandir}, %%{_bindir}, %%{_infodir} etc.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.7-2mdk
- automatically added BuildRequires

* Thu Jun 13 2000 Florin Grad <florin@mandrakesoft.com> 4.0.7-1mdk
- "new" release

* Fri May 05 2000 Florin Grad <florin@mandrakesoft.com> 4.0.5-2mdk
- fix the menu integration

* Sat Apr 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.5-1mdk
- Updated to 4.0.5
- New groups
- Added docs
- added menu funtions to spec file

* Fri Nov 12 1999 Damien Kroktine <damien@mandrakesoft.com>
- Mandrake release

* Wed Sep  8 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.3

* Sat Aug 14 1999 Bill Nottingham <notting@redhat.com>
- change requires: to virtual 'chessprogram'

* Thu Aug 12 1999 Bill Nottingham <notting@redhat.com>
- require gnuchess so it will work out of the box

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.0.2

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file
- built package for 6.0

* Sat Jul 11 1998 Mike Wangsmo <wanger@redhat.com>
- updated to a new version
- buildrooted the package too

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
