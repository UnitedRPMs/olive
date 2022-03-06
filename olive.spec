# 
%define _legacy_common_support 1


%global commit0 3e12fb1f963a9bfa304f4d659fed2f21111ef937
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:       olive
Version:    0.2.0
Release:    7%{?dist}
Summary:    Free non-linear video editor
License:    GPLv3
URL:        https://www.olivevideoeditor.org
Source0:    https://github.com/olive-editor/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:    org.olivevideoeditor.olive.metainfo.xml
Patch:      ffmpeg_fix.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	qt5-linguist
BuildRequires:  ffmpeg-devel >= 4.2
BuildRequires:  frei0r-devel
BuildRequires:  OpenColorIO-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  openexr-devel
BuildRequires:  pkgconfig(portaudio-2.0)
# Documentation
BuildRequires:	doxygen
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Provides:	olive-editor = %{version}

%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.


%prep
%autosetup -n %{name}-%{commit0} -p1 

%build
mkdir -p build
%cmake -B build -DBUILD_DOXYGEN=ON .
%make_build -C build

%install
%make_install -C build

# Metainfo
install -Dm 0644 %{S:1} %{buildroot}/%{_metainfodir}/org.olivevideoeditor.olive.metainfo.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%license LICENSE
%{_bindir}/olive-editor
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.metainfo.xml


%changelog

* Fri Mar 04 2022 - David Va <davidva AT tuta DOT io> 0.2.0-7
- Updated to 0.2.0

* Fri May 15 2020 - David Va <davidva AT tuta DOT io> 0.1.2-1
- Updated to 0.1.2

* Fri Aug 09 2019 - David Va <davidva AT tuta DOT io> 0.1.0-1
- Initial build
