Name:          gupnp
Version:       1.0.3
Release:       2
Summary:       UPnP devices & control points creation framework
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz

BuildRequires: gssdp-devel >= 0.14.15 gtk-doc gobject-introspection-devel >= 1.36
BuildRequires: libsoup-devel libxml2-devel libuuid-devel vala
Requires:      dbus

%description
GUPnP is an elegant, object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup. The GUPnP
API is intended to be easy to use, efficient and flexible. It provides the same
set of features as libupnp,but shields the developer from most of UPnP's internals.

%package       devel
Summary:       Libraries/include files package for gupnp
Requires:      %{name} = %{version}-%{release}

%description   devel
Libraries/include files for development with gupnp.

%package       help
Summary:       Help documentations for gupnp
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
Provides:      %{name}-docs = %{version}-%{release}
Obsoletes:     %{name}-docs < %{version}-%{release}

%description   help
This package contains help file and developer documentation for gupnp.

%prep
%setup -q
# Use Python3 rather than Python2
sed -i '1s|^#! /usr/bin/env python$|#!/usr/bin/python3|' tools/gupnp-binding-tool

%build
%configure --disable-static --with-context-manager=network-manager
%make_build V=1

%install
%make_install
%delete_la

%check
make check %{?_smp_mflags} V=1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libgupnp-1.0.so.*
%{_libdir}/girepository-1.0/GUPnP-1.0.typelib

%files         devel
%{_bindir}/gupnp-binding-tool
%{_libdir}/pkgconfig/gupnp-1.0.pc
%{_libdir}/libgupnp-1.0.so
%{_includedir}/gupnp-1.0
%{_datadir}/gir-1.0/GUPnP-1.0.gir
%{_datadir}/vala/vapi/gupnp*

%files         help
%doc README
%doc %{_datadir}/gtk-doc/html/gupnp

%changelog
* Fri Oct 25 2019 Alex Chao <zhaolei746@huawei.com> - 1.0.3-2
- Package init
