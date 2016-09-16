%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-stdlib
%global commit 66830ac66ac4d435c56c5f3fc93592c32c087726
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-stdlib
Version:        4.12.0
Release:        1%{?alphatag}%{?dist}
Summary:        Standard library of resources for Puppet modules.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-stdlib

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Standard library of resources for Puppet modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/stdlib/



%files
%{_datadir}/openstack-puppet/modules/stdlib/


%changelog
* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 4.12.0-1.66830ac.git
- Newton update 4.12.0 (66830ac66ac4d435c56c5f3fc93592c32c087726)

