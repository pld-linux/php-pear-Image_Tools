%define		_class		Image
%define		_subclass	Tools
%define		_status		beta
%define		_pearname	Image_Tools
%define		subver	RC1
%define		rel		3
Summary:	%{_pearname} - tool collection for images
Summary(pl.UTF-8):	%{_pearname} - zestaw narzędzi do obrazków
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	0.%{subver}.%{rel}
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	8db5b93e8a2d61d7e494ccef8fef4e7b
URL:		http://pear.php.net/package/Image_Tools/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
Requires:	php-pear
Requires:	php-pear-Image_Color >= 1.0.1
Requires:	php-pear-PEAR-core >= 1:1.4.0
Requires:	php-pear-PHP_Compat >= 1.4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of common image manipulations.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zestaw powszechnie używanych funkcji do manipulacji obrazkami.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/docs/demo examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Image/Tools
%{php_pear_dir}/Image/*.php
%{php_pear_dir}/Image/Tools/*.php

%{_examplesdir}/%{name}-%{version}
