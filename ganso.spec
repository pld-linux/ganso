# Note that this is NOT a relocatable package
%define ver      0.1.1
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix   /usr

Summary: GNOME Animation Studio
Name: ganso
Version: %ver
Release: %rel
Copyright: GPL
Group: Graphics
Source: ftp://ceu.fi.udc.es/os/linux/gpul/ganso-%{ver}.tar.bz2

BuildRoot: /var/tmp/ganso-%{PACKAGE_VERSION}-root
Obsoletes: gnome

URL: http://ganso.gpul.org
Docdir: %{prefix}/doc


Requires: gnome-libs >= 1.0.0

%description
GAnSO is a powerful Animation Studio that lets you create your own videos
with and without sound.

It can write as much formats as codecs you install in your system.

%changelog
* Fri Jun 30 2000 Ruben Lopez Gomez <ryu@mundivia.es>
- Created 

%prep
%setup

%build
# libtool can't deal with all the alpha variations but and alpha is an alpha
# in this context.
%ifarch alpha
   CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-redhat-linux --prefix=%prefix 
%else
   CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=/etc
%endif
if [ ! -z "$SMP" ]; then
	make -j$SMP MAKE="make -j$SMP"
else
	make
fi

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
make sysconfdir=$RPM_BUILD_ROOT/etc prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-, root, root)
