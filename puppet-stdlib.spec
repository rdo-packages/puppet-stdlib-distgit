%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-stdlib

Name:           puppet-stdlib
Version:        8.1.0
Release:        1%{?dist}
Summary:        Standard library of resources for Puppet modules.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-stdlib

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/v%{upstream_version}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

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
* Wed Dec 22 2021 RDO <dev@lists.rdoproject.org> 8.1.0-1
- Update to 8.1.0

* Mon Sep 27 2021 RDO <dev@lists.rdoproject.org> 8.0.0-1.21132c8git
- Update to post 8.0.0 (21132c835ae7dad55759389ad5b6e96efe4f292e)

