%define name	gmediaserver
%define version	0.13.0

Name: 	 	%{name}
Summary: 	Sends music to UPnP media devices
Version: 	%{version}
Release: 	%mkrel 4

Source:		http://savannah.nongnu.org/download/gmediaserver/%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/gmediaserver/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libupnp-devel
BuildRequires:  libid3-devel
BuildRequires:	libmagic-devel
BuildRequires:	libtaglib-devel
BuildRequires:  flex
BuildRequires:  bison

%description
GMediaServer is a UPnP music media server. It implements the server component
that provides UPnP media devices with information on available audio files.
GMediaServer uses the built-in http server of libupnp to stream the audio
files to clients.

A number of media devices have been tested and are confirmed to work with
GMediaServer. Among then are NETGEAR MP101, Linksys WMLS11B and WML11B,
Philips Streamium SL300i and RC9800i, and Omnify DMS1.  Other UPnP media
devices (including software based) may work as well.

%prep
%setup -q

%build
cp %_datadir/automake-1.10/mkinstalldirs build-aux
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog README NEWS TODO
%{_bindir}/%name
%{_mandir}/man1/*
%{_infodir}/*



