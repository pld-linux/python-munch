#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A dot-accessible dictionary (a la JavaScript objects)
Summary(pl.UTF-8):	Słownik dostępny przez kropkę (jak obiekty JavaScriptu)
Name:		python-munch
# keep 2.x here for python2 support
Version:	2.5.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/munch/
Source0:	https://files.pythonhosted.org/packages/source/m/munch/munch-%{version}.tar.gz
# Source0-md5:	ed84c3718416c8d4d03d0a6ef46e8e0c
URL:		https://pypi.org/project/munch/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0
BuildRequires:	python-setuptools >= 1:17.1
%if %{with tests}
BuildRequires:	python-PyYAML >= 5.1.0
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pbr >= 3.0
BuildRequires:	python3-setuptools >= 1:17.1
%if %{with tests}
BuildRequires:	python3-PyYAML >= 5.1.0
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Munch is a dictionary that supports attribute-style access, a la
JavaScript.

%description -l pl.UTF-8
Munch to słownik obsługujący dostęp w stylu atrybutów, jak w
JavaScripcie.

%package -n python3-munch
Summary:	A dot-accessible dictionary (a la JavaScript objects)
Summary(pl.UTF-8):	Słownik dostępny przez kropkę (jak obiekty JavaScriptu)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-munch
Munch is a dictionary that supports attribute-style access, a la
JavaScript.

%description -n python3-munch -l pl.UTF-8
Munch to słownik obsługujący dostęp w stylu atrybutów, jak w
JavaScripcie.

%prep
%setup -q -n munch-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md ChangeLog LICENSE.txt README.md
%{py_sitescriptdir}/munch
%{py_sitescriptdir}/munch-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-munch
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md ChangeLog LICENSE.txt README.md
%{py3_sitescriptdir}/munch
%{py3_sitescriptdir}/munch-%{version}-py*.egg-info
%endif
