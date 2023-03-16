%global qt_module qtquickcontrols

Name:    opt-qt5-%{qt_module}
Summary: Qt5 - module with set of QtQuick controls
Version: 5.15.8
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: %{name}-%{version}.tar.bz2

# filter qml provides
%global __provides_exclude_from ^%{_opt_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= %{version}
BuildRequires: opt-qt5-qtbase-static >= %{version}
BuildRequires: opt-qt5-qtbase-private-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
BuildRequires: opt-qt5-qtdeclarative-devel

%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %name-%{version}/upstream


%build
%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE.*
%{_opt_qt5_archdatadir}/qml/QtQuick/

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_opt_qt5_examplesdir}/
%endif