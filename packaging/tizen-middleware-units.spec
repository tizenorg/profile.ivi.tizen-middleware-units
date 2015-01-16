Name:           tizen-middleware-units
Version:        1
Release:        0
Summary:        Tizen middleware target units
Group:          Automotive/Hardware Adaption
License:        GPL-2.0
BuildArch: 	noarch
Source0:        %{name}-%{version}.tar.gz
Source1001:	tizen-middleware-units.manifest

Requires(post):   /usr/bin/systemctl
Requires(postun): /usr/bin/systemctl

%description
Tizen middleware target units creates a systemd target for all
tizen specific middleware (both system and user services).

%prep
%setup -q
cp %{SOURCE1001} .

%build
#nothing to do

%install
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_unitdir_user}

install -m 644 units/system/* %{buildroot}/%{_unitdir}
install -m 644 units/user/* %{buildroot}/%{_unitdir_user}

%post
systemctl enable tizen-user-services-path-trigger.service
systemctl enable tizen-middleware.timer
systemctl --global enable tizen-user-middleware-services.path
systemctl daemon-reload

%postun
systemctl disable tizen-user-services-path-trigger.service
systemctl disable tizen-middleware.timer
systemctl --global disable tizen-user-middleware-services.path
systemctl daemon-reload

%files
%manifest %{name}.manifest
%{_unitdir}/*
%{_unitdir_user}/*
