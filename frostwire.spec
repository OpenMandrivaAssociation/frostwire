# Spec is based on Nicolo' Costanza's and Francesco Mancuso's work in MIB

Summary:	Java-based BitTorrent client
Name:		frostwire
Version:	5.7.3
Release:	1
License:	GPLv3+
Group:		Networking/WWW
Url:		https://www.frostwire.com/
Source0:	http://downloads.sourceforge.net/frostwire/frostwire_%{version}.orig.tar.gz
BuildRequires:	ant
BuildRequires:	locales
Requires:	java >= 1.7
BuildArch:	noarch

%description
FrostWire is a peer-to-peer file sharing program for the BitTorrent protocol.
It is forked from Limewire and written in Java.

%files
%doc README.txt
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export LC_ALL=en_US.utf-8
ant everything

#Copy frostwire.jar
cp -p -v dist/*.jar lib/jars
#Copy all component jars too
cp -p -v components/*/dist/*.jar lib/jars

%install
export DONT_STRIP=1

mkdir -p %{buildroot}%{_datadir}/%{name} %{buildroot}%{_datadir}/applications %{buildroot}%{_iconsdir} %{buildroot}%{_bindir}

install -m0644 lib/jars/*.jar %{buildroot}%{_datadir}/frostwire/
install -m0755 resources/frostwire.sh %{buildroot}%{_datadir}/frostwire/
install -m0644 resources/EULA.txt %{buildroot}%{_datadir}/frostwire/
install -m0644 resources/VERSION %{buildroot}%{_datadir}/frostwire/
install -m0755 resources/frostwire %{buildroot}%{_bindir}/
install -m0644 resources/frostwire.desktop %{buildroot}%{_datadir}/applications/
cp -fr lib/icons/hicolor %{buildroot}%{_iconsdir}

