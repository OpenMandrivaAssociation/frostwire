# Spec is based on Nicolo' Costanza's and Francesco Mancuso's work in MIB

#Get rid of this annoying lib requirement
%define _requires_exceptions libgtksuperwin.so\\|libgtkembedmoz.so\\|libxpcom.so

Name:		frostwire
Version:	5.3.2
Release:	%mkrel 1
Summary:	Java-based Gnutella client
Group:		Networking/WWW
License:	GPLv3
URL:		http://www.frostwire.com/
Source0:	%{name}-%{version}.noarch.tar.gz
Source2: 	frostwire_icons.tar.bz2
Requires:	java >= 1.5
BuildArch:	noarch

%description
FrostWire is a Java Gnutella P2P client.

%prep
%setup -q -n %{name}-%{version}.noarch
tar --bzip2 -xf %{SOURCE2}

%install
export DONT_STRIP=1
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_miconsdir} \
	%{buildroot}%{_liconsdir} \
	%{buildroot}%{_iconsdir}

#icons
%__install -m 644 frostwire-16.png %{buildroot}%{_miconsdir}/%{name}.png
%__install -m 644 frostwire-32.png %{buildroot}%{_iconsdir}/%{name}.png
%__install -m 644 frostwire-48.png %{buildroot}%{_liconsdir}/%{name}.png
%__install -m 644 frostwire-64.png %{buildroot}%{_miconsdir}/%{name}.png
%__install -m 644 frostwire-96.png %{buildroot}%{_iconsdir}/%{name}.png
%__install -m 644 frostwire-128.png %{buildroot}%{_liconsdir}/%{name}.png
%__install -m 644 frostwire-192.png %{buildroot}%{_miconsdir}/%{name}.png
%__install -m 644 frostwire-256.png %{buildroot}%{_iconsdir}/%{name}.png
%__cp -af *.jar *.gif *.py *.icns *.properties %{name} %{buildroot}%{_datadir}/%{name}/

#xdg menu
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=FrostWire
Comment=Gnutella Client
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Network;
EOF

#make Excutable
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/bash
pushd %{_datadir}/%{name}
./%{name}
popd
EOF

%__chmod 0755 %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING changelog EULA.txt
%{_bindir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


