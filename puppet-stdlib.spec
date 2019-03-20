%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-stdlib
%global commit b0dd4c131441603f2a72ab838cf7de39a97840df
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-stdlib
Version:        5.2.0
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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 5.2.0-1.b0dd4c1git
- Update to post 5.2.0 (b0dd4c131441603f2a72ab838cf7de39a97840df)

