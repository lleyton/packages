# Generated by rust2rpm 23
%bcond_without check

%global crate gitoxide

Name:           rust-gitoxide
Version:        0.21.0
Release:        1%{?dist}
Summary:        Command-line application for interacting with git repositories

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gitoxide
Source:         %{crates_source}

BuildRequires:  openssl-devel cmake anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Command-line application for interacting with git repositories.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%doc CHANGELOG.md
%doc README.md
%{_bindir}/ein
%{_bindir}/gix

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
