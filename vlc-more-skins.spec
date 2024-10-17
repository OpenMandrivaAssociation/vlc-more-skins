%define name vlc-more-skins
%define version 0.1
%define release 6



Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   A collection of 7 skins for vlc
License:   GPL
URL:       https://www.videolan.org/vlc/download-skins2.html
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



%changelog
* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-5mdv2009.0
+ Revision: 261872
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-4mdv2009.0
+ Revision: 255570
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2008.1
+ Revision: 129189
- kill re-definition of %%buildroot on Pixel's request


* Thu Jun 30 2005 Sebastien Savarin <plouf@mandriva.org> 0.1-2mdk
- Fix bad perms on Source

* Thu Jun 30 2005 Sebastien Savarin <plouf@mandriva.org> 0.1-1mdk
- First Mandriva Linux release

