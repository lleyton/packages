# Generated by go2rpm 1.9.0
# The check requires go(xyproto/env) which conflicts with go(xyproto/env/v2)
#bcond_without check
%define debug_package %nil

# https://github.com/xyproto/gendesk
%global goipath         github.com/xyproto/gendesk
Version:                1.0.10
%global tag             1.0.9
%global commit          f074161864697100fdc21a99e09b567e82aeb1b9

%gometa -f


%global common_description %{expand:
:herb: Generate .desktop files and download .png icons by specifying a minimum
of information.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%?dist
Summary:        Generate .desktop files and download .png icons

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}
BuildRequires:  git-core gcc
Provides:       gendesk

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
go mod download

%build
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w -extldflags '--static-pie'" -buildmode=pie -tags 'osusergo,netgo,static_build' -v -x -o %{gobuilddir}/bin/gendesk .
go tool buildid -w %{gobuilddir}/bin/gendesk

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
