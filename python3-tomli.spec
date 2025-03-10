#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	A lil' TOML parser
Summary(pl.UTF-8):	Malutki parser TOML-a
Name:		python3-tomli
Version:	2.0.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tomli/
Source0:	https://files.pythonhosted.org/packages/source/t/tomli/tomli-%{version}.tar.gz
# Source0-md5:	d4341621d423a7ca6822e23d6d52bb9a
URL:		https://pypi.org/project/tomli/
BuildRequires:	python3-modules >= 1:3.7
# TODO:
#BuildRequires:	python3-flit_core >= 3.2.0
BuildRequires:	python3-setuptools >= 1:61
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomli is a Python library for parsing TOML.

Tomli is fully compatible with TOML v1.0.0
<https://toml.io/en/v1.0.0>.

%description -l pl.UTF-8
Tomli to biblioteka Pythona do analizy TOML-a.

Tomli jest w pełni zgodny z TOM v1.0.0 <https://toml.io/en/v1.0.0>.

%prep
%setup -q -n tomli-%{version}

# stub for setuptools until we have flit
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/tomli
%{py3_sitescriptdir}/tomli-%{version}-py*.egg-info
