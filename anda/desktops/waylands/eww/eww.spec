# Generated by rust2rpm 27
%global commit b6b7bc8453a5deecae0f0f4cc0c5f8639df97964
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250205
%global ver v0.6.0
%bcond check 0

Name:           eww
Version:        %ver^%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Widgets for everyone!

SourceLicense:  MIT
License:        MIT

URL:            https://elkowar.github.io/eww
Source0:		https://github.com/elkowar/eww/archive/%commit.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
Requires:       (%name-x11 or %name-wayland)

%global _description %{expand:
Widgets for everyone!.}

%description %{_description}

%package x11
Summary:        eww for x11
Conflicts:      eww-wayland
SourceLicense:  MIT
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CC0-1.0 AND ISC AND LGPL-3.0-only AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
RemovePathPostFixes: .x11

%description x11 %{_description}

%package wayland
Summary:        eww for wayland
Conflicts:      eww-x11
SourceLicense:  MIT
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CC0-1.0 AND ISC AND LGPL-3.0-only AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
RemovePathPostFixes: .wayland

%description wayland %{_description}

%prep
%autosetup -n eww-%{commit} -p1
%cargo_prep_online

%build
%{cargo_license_summary_online -n -f x11}
%{cargo_license_online -n -f x11} > LICENSE.dependencies.x11
%{cargo_license_summary_online -n -f wayland}
%{cargo_license_online -n -f wayland} > LICENSE.dependencies.wayland
%cargo_build -n -f x11
mv target/rpm/eww   target/rpm/eww.x11
mv target/rpm/eww.d target/rpm/eww.d.x11
%cargo_build -n -f wayland
mv target/rpm/eww   target/rpm/eww.wayland
mv target/rpm/eww.d target/rpm/eww.d.wayland

%install
install -Dpm755 target/rpm/eww.* -t %buildroot%_bindir

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc YUCK_MIGRATION.md

%files x11
%license LICENSE.dependencies.x11
%{_bindir}/eww.x11
%{_bindir}/eww.d.x11

%files wayland
%license LICENSE.dependencies.wayland
%{_bindir}/eww.wayland
%{_bindir}/eww.d.wayland

%changelog
%autochangelog
