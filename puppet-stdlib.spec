%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-stdlib
%global commit 7c1ae256a70045473ebf2f50a61c8c082b926f29
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-stdlib
Version:        6.6.0
Release:        1%{?alphatag}%{?dist}
Summary:        Standard library of resources for Puppet modules.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-stdlib

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz
Patch0:         0001-Replacing-URI.escape-with-URI-DEFAULT_PARSER.patch

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Standard library of resources for Puppet modules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1


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
* Fri Nov 10 2023 RDO <dev@lists.rdoproject.org> 6.6.0-1.7c1ae25git
- Update to 6.6.0

* Thu Dec 23 2021 Joel Capitao <jcapitao@redhat.com> 6.3.0-3.7c1ae25git
- Replacing URI.escape with URI-DEFAULT_PARSER

* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 6.3.0-2.7c1ae25git
- Update to post 6.3.0 (7c1ae256a70045473ebf2f50a61c8c082b926f29)

