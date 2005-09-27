%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Tools 
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - tool collection for images
Summary(pl):	%{_pearname} - zestaw narzêdzi do obrazków
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	2.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fbf6f44385b86e687366edb95b25c619
URL:		http://pear.php.net/package/Image_Tools/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
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
rm -f ./%{php_pear_dir}/generate_package_xml.php # junk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/doc/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
