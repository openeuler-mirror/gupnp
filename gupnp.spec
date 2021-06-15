Name:          gupnp
Version:       1.2.4
Release:       1
Summary:       UPnP devices & control points creation framework
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/1.2/%{name}-%{version}.tar.xz
Patch0:        CVE-2021-33516.patch

BuildRequires: gssdp-devel >= 1.2.3 gtk-doc gobject-introspection-devel >= 1.36
BuildRequires: libsoup-devel libxml2-devel libuuid-devel vala meson
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
%autosetup -n %{name}-%{version} -p1

%build
%meson \
  -Dcontext_manager=network-manager \
  -Dgtk_doc=true
%meson_build

%install
%meson_install
%delete_la

%check
%meson_test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libgupnp-1.2.so.*
%{_libdir}/girepository-1.0/GUPnP-1.2.typelib

%files         devel
%{_bindir}/gupnp-binding-tool-1.2
%{_libdir}/pkgconfig/gupnp-1.2.pc
%{_libdir}/libgupnp-1.2.so
%{_includedir}/gupnp-1.2
%{_datadir}/gir-1.0/GUPnP-1.2.gir
%{_datadir}/vala/vapi/gupnp*

%files         help
%doc README
%doc %{_datadir}/gtk-doc/html/gupnp
%{_mandir}/man1/gupnp-binding-tool-*

%changelog
* Mon Jun 7 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 1.2.4-1
- Upgrade to 1.2.4
- Update Version, Release, Source0, BuildRequires
- Delete sed operation which existed in this version
- Add patch for fix CVE-2021-33516
- Update stage 'prep', 'build', 'install', 'check', 'files'

* Fri Oct 25 2019 Alex Chao <zhaolei746@huawei.com> - 1.0.3-2
- Package init
