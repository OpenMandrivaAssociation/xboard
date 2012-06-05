Summary:	An X Window System graphical chessboard
Name:		xboard
Version:	4.6.2
Release:	1
Group:		Games/Boards
URL:		http://www.gnu.org/software/xboard/
License:	BSD-like and GPLv2+
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	xboard.sh.bz2
Source2:	xboard-pxboard.man.bz2
Source3:	XBoard.ad.bz2

Requires:	chessengine
Conflicts:	gnuchess <= 5.06
BuildRequires:	flex
BuildRequires:	groff-for-man
BuildRequires:	libxaw-devel
BuildRequires:	xpm-devel

%description
Xboard is an X Window System based graphical chessboard which can be used with
the GNUchess and Crafty chess programs, with Internet Chess Servers (ICSs),
with chess via email, or with your own saved games.

%prep
%setup -q 

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
%doc AUTHORS ChangeLog* COPYRIGHT NEWS zippy.README
%doc *.txt *.html
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XBoard
%{_gamesbindir}/*
%{_mandir}/man?/*
%{_infodir}/*.info*
%{_datadir}/applications/*.desktop
%{_datadir}/games/%{name}/sounds/*
%{_datadir}/games/%{name}/bitmaps/
%{_datadir}/games/%{name}/pixmaps/
%{_datadir}/mime/packages/xboard.xml
%{_sysconfdir}/%{name}.conf
%{_iconsdir}/hicolor/*/apps/*.*
