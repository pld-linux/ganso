Summary:	GNOME Animation Studio
Name:		ganso
Version:	0.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ceu.fi.udc.es/os/linux/gpul/%{name}-%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml-devel
URL:		http://ganso.gpul.org
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

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates"; export CXXFLAGS
gettextize --copy --force
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/ganso/{codecs,plugins}/*.so

gzip -9nf AUTHORS ChangeLog NEWS README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

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
