# 
%define _legacy_common_support 1

Name:       olive
Version:    0.1.2
Release:    7%{?dist}
Summary:    Free non-linear video editor
License:    GPLv3
URL:        https://www.olivevideoeditor.org
Source0:    https://github.com/olive-editor/%{name}/archive/%{version}.tar.gz 
Source1:    org.olivevideoeditor.olive.metainfo.xml
Patch:      ffmpeg_fix.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  ffmpeg-devel >= 4.2
BuildRequires:  frei0r-devel
# Documentation
BuildRequires:	doxygen
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Provides:	olive-editor = %{version}

%description
Olive is a free non-linear video editor for Windows, macOS, and Linux.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DBUILD_DOXYGEN=ON .
%make_build

%install
%make_install

# Documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/ %{buildroot}%{_docdir}/%{name}

# Metainfo
install -Dm 0644 %{S:1} %{buildroot}/%{_metainfodir}/org.olivevideoeditor.olive.metainfo.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%license LICENSE
%{_bindir}/olive-editor
%{_datadir}/olive-editor/
%{_datadir}/applications/*.desktop
%{_docdir}/olive/
%{_metainfodir}/*.appdata.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/org.olivevideoeditor.olive.metainfo.xml


%changelog

* Fri May 15 2020 - David Va <davidva AT tuta DOT io> 0.1.2-1
- Updated to 0.1.2

* Fri Aug 09 2019 - David Va <davidva AT tuta DOT io> 0.1.0-1
- Initial build
