%define version 4.2.7
%define release %mkrel 8

Summary:	An X Window System graphical chessboard
Name:		xboard
Version:	%{version}
Release:	%{release}
Group:		Games/Boards
URL:		http://www.tim-mann.org/xboard.html
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Source:		ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:	xboard.sh.bz2
Source2:	xboard-pxboard.man.bz2
Source3:	XBoard.ad.bz2
Patch0:		xboard-4.0.5-entry.patch.bz2
Patch1:		xboard-4.2.7-cmail-quote.patch.bz2
Patch2:		xboard-4.2.7-lowtime-warning.patch.bz2
Patch3:		xboard-4.2.7-xvt.patch.bz2
Patch4:		xboard-4.2.7-xtname.patch.bz2
Patch5:		xboard-4.2.7-hilight-threatened-pieces.patch.bz2

Requires:	chessengine
Conflicts:	gnuchess <= 5.06
BuildRequires:	flex
BuildRequires:	groff-for-man
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel

%description
Xboard is an X Window System based graphical chessboard which can be used with
the GNUchess and Crafty chess programs, with Internet Chess Servers (ICSs),
with chess via email, or with your own saved games.

%prep
%setup -q 
%patch0 -p1 -b .info-entry
%patch1 -p1 -b .quote
%patch2 -p1 -b .lowtime
%patch3 -p1 -b .xvt
%patch4 -p1 -b .xtname
%patch5 -p1 -b .hilite

chmod 0644 ChangeLog*

%build
%configure2_5x --bindir=%{_gamesbindir}
# Xaw3d kinda conflicts with Conectiva patch; no tooltip will be
# shown - Abel
# --with-Xaw3d
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_gamesbindir}

mv %{buildroot}%{_gamesbindir}/%{name} %{buildroot}%{_gamesbindir}/%{name}.real

bzip2 -dc %{SOURCE1} > %{buildroot}%{_gamesbindir}/%{name}
chmod 755 %{buildroot}%{_gamesbindir}/%{name}

# install pxboard manpage
bzip2 -dc %{SOURCE2} > %{buildroot}%{_mandir}/man6/pxboard.6

# install X resource
mkdir -p %{buildroot}%{_sysconfdir}/X11/app-defaults
bzip2 -dc %{SOURCE3} > %{buildroot}%{_sysconfdir}/X11/app-defaults/XBoard

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XBoard
Comment=GUI chessboard game
Exec=%{_gamesbindir}/xboard
Icon=strategy_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

# remove useless files
rm -f %{buildroot}%{_infodir}/dir

%post
%update_menus
%_install_info %{name}.info

%postun
%clean_menus
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog* COPYING COPYRIGHT FAQ NEWS READ_ME zippy.README
%doc *.txt *.html
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XBoard
%{_datadir}/applications/mandriva-%{name}.desktop
%{_gamesbindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
