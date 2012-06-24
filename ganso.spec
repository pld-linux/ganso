Summary:	GAnSO - Gnome Animation StudiO
Summary(pl):	Studio animacji dla GNOME
Name:		ganso
Version:	0.1.1
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gpul.org/gpul/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_fix.patch
URL:		http://www.gpul.org/proyectos/ganso/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GAnSO is a powerful Animation Studio that lets you create your own
videos with and without sound.

It can write as much formats as codecs you install in your system.

This package includes the core, a MPEG-1 codec and a sample plug-in
which has a filter, a stream editor and a template, just to show how
easy is to extend GAnSO, but which can be usefull to build some
videos, as this filter performs progressive alpha
decreasing/increasing of a stream, effect that is very used in
professional creations to change from one video to another one while
both keep animated.

%description -l pl
GAnSO (Gnome Animation StudiO) to studio animacji pozwalaj�ce tworzy�
w�asne filmy z d�wi�kiem lub bez.

Mo�e zapisywa� w takich formatach, dla jakich codeki masz w systemie.

Ten pakiet zawiera g��wn� cz�� GAnSO, codec MPEG-1 oraz przyk�adow�
wtyczk�, kt�ra zawiera filtr, edytor strumieni i wzorzec, �eby pokaza�
jak �atwo mo�na rozszerza� GAnSO, ale mo�e by� tak�e u�yteczna przy
tworzeniu film�w, jako �e ten filtr przeprowadza progresywne
zmniejszanie/zwi�kszanie kana�u alpha strumienia, co daje efekt cz�sto
u�ywany w profesjonalnych filmach - przej�cie z jednego obrazu do
drugiego podczas gdy oba s� animowane.

%prep
%setup -q
%patch -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%dir %{_sysconfdir}/ganso
%config %{_sysconfdir}/ganso/ganso.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ganso
%dir %{_libdir}/ganso/codecs
%dir %{_libdir}/ganso/plugins
%attr(755,root,root) %{_libdir}/ganso/codecs/*
%attr(755,root,root) %{_libdir}/ganso/plugins/*
%{_mandir}/man1/*
