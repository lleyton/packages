# Generated by rust2rpm 22
%global debug_package %{nil}
%bcond_without check

%global crate zellij

Name:           rust-zellij
Version:        0.38.0
Release:        1%{?dist}
Summary:        Terminal workspace with batteries included

License:        MIT
URL:            https://crates.io/crates/zellij
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  anda-srpm-macros
BuildRequires:  rust-packaging
BuildRequires:  openssl-devel

#BuildRequires:  external:crate:sccache

%global _description %{expand:
Terminal workspace with batteries included.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%doc README.md
%{_bindir}/zellij

%prep
%autosetup -n %{crate}-%{version_no_tilde}
%cargo_prep_online


%build
%cargo_build

%install
%cargo_install

%changelog
%autochangelog
