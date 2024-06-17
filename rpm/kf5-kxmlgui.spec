%global kf5_version 5.116.0

Name:    opt-kf5-kxmlgui
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for user-configurable main windows

# Library LGPLv2+, ksendbugmail is GPLv2+
License: GPLv2+ and LGPLv2+
URL:     https://invent.kde.org/frameworks/kxmlgui

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
#BuildRequires:  opt-kf5-attica-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kcoreaddons-devel >= %{kf5_version}
#BuildRequires:  opt-kf5-kglobalaccel-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kguiaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kitemviews-devel >= %{kf5_version}
BuildRequires:  opt-kf5-ktextwidgets-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  opt-kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros

BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel
BuildRequires:  opt-qt5-qtbase-private-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kconfig >= %{kf5_version}
Requires: opt-kf5-kconfigwidgets >= %{kf5_version}
Requires: opt-kf5-kcoreaddons >= %{kf5_version}
Requires: opt-kf5-kguiaddons >= %{kf5_version}
Requires: opt-kf5-ki18n >= %{kf5_version}
Requires: opt-kf5-kiconthemes >= %{kf5_version}
Requires: opt-kf5-kitemviews >= %{kf5_version}
Requires: opt-kf5-kwidgetsaddons >= %{kf5_version}


%description
KDE Frameworks 5 Tier 3 solution for user-configurable main windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-kf5-kconfig-devel >= %{kf5_version}
Requires:       opt-kf5-kconfigwidgets-devel >= %{kf5_version}
Requires:       opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5 -DFORCE_DISABLE_KGLOBALACCEL=ON
%cmake_build

%install
%cmake_install

%find_lang_kf5 kxmlgui5_qt

# Own the kxmlgui directory
mkdir -p %{buildroot}%{_opt_kf5_datadir}/kxmlgui5/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSES/*.txt
%dir %{_opt_kf5_sysconfdir}/xdg/ui/
%config %{_opt_kf5_sysconfdir}/xdg/ui/ui_standards.rc
%{_opt_kf5_datadir}/qlogging-categories5/kxmlgui.*
%{_opt_kf5_libdir}/libKF5XmlGui.so.*
%{_opt_qt5_libexecdir}/kf5/ksendbugmail
%dir %{_opt_kf5_datadir}/kxmlgui5/
%{_opt_kf5_qtplugindir}/designer/*5widgets.so
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KXmlGui/
%{_opt_kf5_libdir}/libKF5XmlGui.so
%{_opt_kf5_libdir}/cmake/KF5XmlGui/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KXmlGui.pri
