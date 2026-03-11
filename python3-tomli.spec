#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	A lil' TOML parser
Summary(pl.UTF-8):	Malutki parser TOML-a
Name:		python3-tomli
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tomli/
Source0:	https://files.pythonhosted.org/packages/source/t/tomli/tomli-%{version}.tar.gz
# Source0-md5:	10ef5dd352e7dfd2d6ed322cf0280435
URL:		https://pypi.org/project/tomli/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-flit_core >= 3.12
BuildRequires:	python3-flit_core < 4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomli is a Python library for parsing TOML.

Tomli version 2.4.0+ is fully compatible with TOML v1.1.0
<https://toml.io/en/v1.1.0>.

%description -l pl.UTF-8
Tomli to biblioteka Pythona do analizy TOML-a.

Tomli w wersji 2.4.0+ jest w pełni zgodny ze specyfikacją TOML v1.1.0
<https://toml.io/en/v1.1.0>.

%prep
%setup -q -n tomli-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m unittest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/tomli
%{py3_sitescriptdir}/tomli-%{version}.dist-info
