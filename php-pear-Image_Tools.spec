%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Tools 
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - tool collection for images
Summary(pl):	%{_pearname} - zestaw narzêdzi do obrazków
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	45eabb1247e469516de7ecc79b22a8bc
URL:		http://pear.php.net/package/Image_Tools/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gd
Requires:	php-pear
Requires:	php-pear-Image_Color >= 1.0.1
Requires:	php-pear-PEAR-core >= 1:1.3.3
Requires:	php-pear-PHP_Compat >= 1.4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of common image manipulations.

In PEAR status of this package is: %{_status}.

%description -l pl
Zestaw powszechnie u¿ywanych funkcji do manipulacji obrazkami.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
