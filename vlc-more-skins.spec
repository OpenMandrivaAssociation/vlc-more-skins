%define name vlc-more-skins
%define version 0.1
%define release %mkrel 6



Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   A collection of 7 skins for vlc
License:   GPL
URL:       http://www.videolan.org/vlc/download-skins2.html
Group:     Video
Source0:   %{name}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: svlc
BuildArch: noarch


%description
A collection of 7 skins for vlc

%prep
rm -rf %buildroot

%setup -n %{name}
%install
rm -rf %buildroot
mkdir -p %buildroot/%_datadir/vlc/skins2/
install -m644 *.vlt %buildroot/%_datadir/vlc/skins2/

%clean
rm -rf %buildroot
%files
%defattr(-,root,root)
%doc COPYING readme.txt
%_datadir/vlc/skins2/chaos.vlt
%_datadir/vlc/skins2/itunes.vlt
%_datadir/vlc/skins2/MediaPlayer.vlt
%_datadir/vlc/skins2/solar.vlt
%_datadir/vlc/skins2/void.vlt
%_datadir/vlc/skins2/vplayer.vlt
%_datadir/vlc/skins2/winamp5.vlt

