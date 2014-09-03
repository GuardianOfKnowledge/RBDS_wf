# RPM package for RBDS_wf
# This file is regularly AUTO-GENERATED by the IDE. DO NOT MODIFY.

# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %define _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

Name: RBDS_wf
Summary: Waveform RBDS_wf
Version:        1.0.0
Release:        1%{?dist}
License: None
Group: REDHAWK/Waveforms
Source: %{name}-%{version}.tar.gz
# Require the controller whose SPD is referenced
Requires: FMDemodulator
# Require each referenced component
Requires: FMDemodulator FilterDecimate Mixer FrequencyDivider BPSK DifferentialDecoder RBDSDecoder
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Component %{name}
 * Commit: __REVISION__
 * Source Date/Time: __DATETIME__


%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dom/waveforms/%{name}"
%__install -m 644 RBDS_wf.sad.xml $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/%{name}/RBDS_wf.sad.xml

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/waveforms/%{name}
%{_prefix}/dom/waveforms/%{name}/RBDS_wf.sad.xml
