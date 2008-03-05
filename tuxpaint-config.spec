#
Summary:	Tux Paint Config - GUI to set configuration for TuxPaint
Summary(pl.UTF-8):	Tux Paint Konfigurator - graficzny konfigurator dla TuxPaint
Name:		tuxpaint-config
Version:	0.0.10
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/tuxpaint/%{name}-%{version}.tar.gz
# Source0-md5:	11e705f18176882ec9f2c1a1ee353c9c
URL:		http://www.tuxpaint.org/
BuildRequires:	fltk-devel
BuildRequires:	SDL_Pango-devel
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	gettext-devel
BuildRequires:	libpaper-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The add-on for "Tux Paint" program, a graphical tool can be used
to change Tux Paint's settings.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX="%{_prefix}" \
	CONFDIR="%{_sysconfdir}" \
	DATA_PREFIX="%{_datadir}/tuxpaint" \
	DOC_PREFIX="%{_datadir}/doc" \
	ICON_PREFIX="%{_pixmapsdir}" \
	X11_ICON_PREFIX="%{_pixmapsdir}" \
	LOCALE_PREFIX="%{_datadir}/locale" \
	KDE_ICON_PREFIX="%{_datadir}/icons" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps


%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}/ \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir}/ \
	MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir}/ \
	GNOME_PREFIX=$RPM_BUILD_ROOT%{_prefix}/ \
	KDE_PREFIX=$RPM_BUILD_ROOT%{_desktopdir}/ \
	KDE_ICON_PREFIX=$RPM_BUILD_ROOT%{_datadir}/icons/ \
	X11_ICON_PREFIX=$RPM_BUILD_ROOT%{_pixmapsdir}/ \
	ICON_PREFIX="$RPM_BUILD_ROOT%{_pixmapsdir}/"

#rm a lot of unwanted files and directories:
find docs/ -type d|grep CVS|xargs rm -rf
find docs/ -name "[KC]OP*" -exec rm -f "{}" ";"
find docs/ -name "INS*" -exec rm -f "{}" ";"
find docs/ -name "AUT*" -exec rm -f "{}" ";"
find docs/ -size -50c -type f -exec rm -f "{}" ";"
find docs/ -empty |xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/*.txt
%doc %{_docdir}/%{name}/html/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/*/apps/*.png
#%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
