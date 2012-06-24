Summary:	GAnSO - GNOME Animation StudiO
Summary(pl):	Studio animacji dla GNOME
Name:		ganso
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/ganso/%{name}-%{version}.tar.bz2
# Source0-md5:	629daa8af0dc91efd1dd617858102415
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-build.patch
URL:		http://ganso.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

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
GAnSO (GNOME Animation StudiO) to studio animacji pozwalaj�ce tworzy�
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
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/ganso/{*,*/*,*/*/*}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/ganso
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganso/ganso.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ganso
%dir %{_libdir}/ganso/codecs
%dir %{_libdir}/ganso/codecs/input
%dir %{_libdir}/ganso/codecs/input/video
%dir %{_libdir}/ganso/codecs/output
%dir %{_libdir}/ganso/plugins
%attr(755,root,root) %{_libdir}/ganso/codecs/input/video/*.so
%attr(755,root,root) %{_libdir}/ganso/codecs/output/*.so
%attr(755,root,root) %{_libdir}/ganso/plugins/*.so
%{_mandir}/man1/*
