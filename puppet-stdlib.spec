%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-stdlib
%global commit 6ab03a1260ebac03c20467781dabe03c933a4c5a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-stdlib
Version:        8.4.0
Release:        1%{?alphatag}%{?dist}
Summary:        Standard library of resources for Puppet modules.
License:        ASL 2.0

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
* Fri Sep 30 2022 RDO <dev@lists.rdoproject.org> 8.4.0-1.6ab03a1git
- Update to post 8.4.0 (6ab03a1260ebac03c20467781dabe03c933a4c5a)

