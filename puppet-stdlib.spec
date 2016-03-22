Name:			puppet-stdlib
Version:		XXX
Release:		XXX
Summary:		Standard library of resources for Puppet modules.
License:		Apache-2.0

URL:			https://github.com/puppetlabs/puppetlabs-stdlib

Source0:		https://github.com/puppetlabs/puppetlabs-stdlib/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet >= 2.7.0

%description
Standard library of resources for Puppet modules.

%prep
%setup -q -n puppetlabs-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib/
cp -r * %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib/



%files
%{_datadir}/openstack-puppet/modules/stdlib/


%changelog

