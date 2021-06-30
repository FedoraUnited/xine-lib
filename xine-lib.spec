%global         plugin_abi  2.9
%global         codecdir    %{_libdir}/codecs
# 
%define _legacy_common_support 1

%ifarch %{ix86}
    %global     have_vidix  1
%else
    %global     have_vidix  0
%endif # ix86

# commit
# from https://sourceforge.net/p/xine/xine-lib-1.2/ci/default/tree/
%global _commit 09aa41e45228985adf83e87c4a1a55d6e524986c
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Summary:        A multimedia engine
Name:           xine-lib
Version:        1.2.11
Release:        10%{?dist}
License:        GPLv2+
URL:            http://www.xine-project.org/
Source0:        https://github.com/UnitedRPMs/%{name}/releases/download/%{version}/xine-%{name}-1.2-%{_commit}.zip

Provides:       xine-lib(plugin-abi) = %{plugin_abi}
%{?_isa:Provides: xine-lib(plugin-abi)%{?_isa} = %{plugin_abi}}

Obsoletes:      xine-lib-extras-freeworld < 1.1.21-10
Provides:       xine-lib-extras-freeworld = %{version}-%{release}

BuildRequires:  gawk
BuildRequires:  sed
BuildRequires:  gettext-devel
# X11
BuildRequires:	mesa-libEGL-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  libXt-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libGLU-devel
BuildRequires:  libv4l-devel
# BuildRequires:  libxcb-devel
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
# Video
BuildRequires:  SDL-devel
BuildRequires:  libtheora-devel
BuildRequires:  libmng-devel
BuildRequires:  aalib-devel >= 1.4
BuildRequires:  libcaca-devel >= 0.99-0.5.beta14
BuildRequires:  ImageMagick-devel >= 6.2.4.6-1
BuildRequires:  libvpx-devel
%if 0%{?fedora} >= 34
BuildRequires:	libdav1d-devel >= 0.8.0
%else
BuildRequires:	libdav1d-devel >= 0.5.2
%endif
%if 0%{?fedora} >= 34
BuildRequires:  libaom-devel >= 3.1.1
%else
BuildRequires:  libaom-devel
%endif 
%if 0%{?_with_freetype:1}
BuildRequires:  fontconfig-devel
%endif # freetype
# Audio
BuildRequires:  ffmpeg-devel >= 4.3
BuildRequires:  a52dec-devel
BuildRequires:  alsa-lib-devel >= 0.9.0
BuildRequires:  faad2-devel >= 2.9.1
BuildRequires:  flac-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libdca-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libvorbis-devel
BuildRequires:  speex-devel
BuildRequires:  wavpack-devel
# CDs / DVDs
BuildRequires:  libcdio-devel
BuildRequires:  vcdimager-devel >= 0.7.23
%if 0%{?fedora} >= 34
BuildRequires:  libdvdread-devel >= 6.1.1
BuildRequires:  libdvdnav-devel >= 6.1.0
%else
BuildRequires:  libdvdread-devel 
BuildRequires:  libdvdnav-devel
%endif
BuildRequires:  libbluray-devel
# Other
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  gtk2-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh2-devel
BuildRequires:  libnfs-devel
BuildRequires:  gnutls-devel
BuildRequires:  openssl-devel

BuildRequires:	autoconf automake libtool
BuildRequires: 	esound-devel


%description
This package contains the Xine library.  It can be used to play back
various media, decode multimedia files from local disk drives, and display
multimedia streamed over the Internet. It interprets many of the most
common multimedia formats available - and some uncommon formats, too. 

%package        devel
Summary:        Xine library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
%description    devel
This package contains development files for %{name}.

%package        extras
Summary:        Additional plugins for %{name} 
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    extras
This package contains extra plugins for %{name}:
  - JACK
  - GDK-Pixbuf
  - SMB
  - SDL
  - AA-lib
  - Image decoding


%prep
%autosetup -n xine-%{name}-1.2-%{_commit}

autoreconf -ivf

%build
export SDL_CFLAGS="$(sdl-config --cflags)" SDL_LIBS="$(sdl-config --libs)"
# Keep list of options in mostly the same order as ./configure --help.
%configure \
	        --enable-static=no \
	        --enable-shared=yes \
	        --enable-fast-install=yes \
	        \
	        --enable-oss \
	        --enable-aalib \
	        --disable-dha-kmod \
	        --enable-dxr3 \
	        --enable-fb \
	        --enable-opengl \
	        --enable-glu \
	        --disable-vidix \
	        --enable-xinerama \
	        --enable-xvmc \
	        --enable-vdpau \
	        --enable-vaapi \
	        --enable-dvb \
	        --enable-samba \
	        --enable-v4l2 \
	        --enable-libv4l \
	        --enable-vcd \
	        --enable-vdr \
	        --enable-bluray \
	        --enable-avformat \
	        --enable-a52dec \
	        --enable-asf \
	        --enable-nosefart \
	        --enable-faad \
	        --enable-gdkpixbuf \
	        --enable-libjpeg \
	        --enable-dts \
	        --enable-mad \
	        --enable-modplug \
	        --enable-libmpeg2new \
	        --enable-musepack \
	        --enable-mng \
	        --enable-vpx \
	        \
	        --with-freetype \
		--enable-antialiasing \
	        --with-fontconfig \
	        --with-x \
	        --with-alsa \
	        --with-esound \
	        --without-fusionsound \
	        --with-jack \
	        --with-pulseaudio \
		--with-caca \
	        --without-linux-path \
	        --without-libstk \
	        --with-sdl \
	        --without-xcb \
	        --with-imagemagick \
	        --with-libflac \
	        --with-speex \
	        --with-theora \
	        --with-vorbis \
	        --with-wavpack \
		--with-external-dvdnav \
		--disable-gnomevfs \
		--enable-ipv6 \
    		--with-real-codecs-path=%{codecdir} \
 		--with-xv-path=%{_libdir} \
    		--with-w32-path=%{codecdir}

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang libxine2
cp -pR $RPM_BUILD_ROOT%{_docdir}/xine-lib __docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/xine-lib

# Removing useless files
rm -Rf $RPM_BUILD_ROOT%{_libdir}/libxine*.la __docs/README \
       __docs/README.{freebsd,irix,macosx,solaris,MINGWCROSS,WIN32}

# Directory for binary codecs
mkdir -p $RPM_BUILD_ROOT%{codecdir}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f libxine2.lang
%doc AUTHORS CREDITS ChangeLog* README TODO
%doc __docs/README.* __docs/faq.*
%license COPYING COPYING.LIB
%dir %{codecdir}/
%{_datadir}/xine-lib/
%{_libdir}/libxine.so.*
%{_mandir}/man5/xine.5*
%dir %{_libdir}/xine/
%dir %{_libdir}/xine/plugins/
%dir %{_libdir}/xine/plugins/%{plugin_abi}/
%{_libdir}/xine/plugins/%{plugin_abi}/mime.types
# Listing every plugin separately for better control over binary packages
# containing exactly the plugins we want, nothing accidentally snuck in
# nor dropped.
%dir %{_libdir}/xine/plugins/%{plugin_abi}/post/
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_audio_filters.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_goom.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_rawvideo.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_vdpau.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_asf.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_audio.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_fli.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_games.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_image.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_mng.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_modplug.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_nsv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_playlist.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_pva.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_slave.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_dmx_video.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_mosaico.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_planar.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_switch.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_tvtime.so
%{_libdir}/xine/plugins/%{plugin_abi}/post/xineplug_post_visualizations.so
%if %{have_vidix}
%dir %{_libdir}/xine/plugins/%{plugin_abi}/vidix/
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/cyberblade_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mach64_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mga_crtc2_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/mga_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/nvidia_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/pm2_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/pm3_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/radeon_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/rage128_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/savage_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/sis_vid.so
%{_libdir}/xine/plugins/%{plugin_abi}/vidix/unichrome_vid.so
%endif # vidix
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_alsa.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_oss.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_pulseaudio.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_a52.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dts.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dvaudio.so
/usr/lib64/xine/plugins/%{plugin_abi}/xineplug_dxr3.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_faad.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_ff.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_gsm610.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libaom.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libjpeg.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libvpx.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_lpcm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mad.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mpeg2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mpc.so
%ifarch %{ix86}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_qt.so
%endif # ix86
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_real.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spu.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spucc.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spucmml.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spudvb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_spuhdmv.so
%ifarch %{ix86}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_w32dll.so
%endif # ix86
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_flac.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_bluray.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_cdda.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_dvb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_dvd.so
#{_libdir}/xine/plugins/{plugin_abi}/xineplug_inp_http.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_mms.so
#{_libdir}/xine/plugins/{plugin_abi}/xineplug_inp_net.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_network.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_nfs.so
#{_libdir}/xine/plugins/{plugin_abi}/xineplug_inp_pnm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_pvr.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_rtp.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_ssh.so
#{_libdir}/xine/plugins/{plugin_abi}/xineplug_inp_rtsp.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_v4l2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_vcd.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_vcdo.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_nsf.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_sputext.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_tls_gnutls.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_tls_openssl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vdr.so
#{_libdir}/xine/plugins/{plugin_abi}/xineplug_vo_out_dxr3.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_fb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_opengl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_opengl2.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_raw.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vaapi.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vdpau.so
%if %{have_vidix}
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_vidix.so
%endif # vidix
# {_libdir}/xine/plugins/{plugin_abi}/xineplug_vo_out_xcbshm.so
# {_libdir}/xine/plugins/{plugin_abi}/xineplug_vo_out_xcbxv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xshm.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xv.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xvmc.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_xxmc.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_wavpack.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_xiph.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_esd.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_libpng.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_glx.so

%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_egl_wl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_gl_egl_x11.so

%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_dav1d.so

%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_to_spdif.so

%files extras
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_ao_out_jack.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_gdk_pixbuf.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_image.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_inp_smb.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_aa.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_caca.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_vo_out_sdl.so
%{_libdir}/xine/plugins/%{plugin_abi}/xineplug_decode_mpeg2new.so

%files devel
%doc __docs/hackersguide/*
%{_bindir}/xine-config
%{_bindir}/xine-list*
%{_datadir}/aclocal/xine.m4
%{_includedir}/xine.h
%{_includedir}/xine/
%{_libdir}/libxine.so
%{_libdir}/pkgconfig/libxine.pc
%{_mandir}/man1/xine-config.1*
%{_mandir}/man1/xine-list*.1*


%changelog

* Fri Jun 18 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.11-10
- Rebuilt for aom

* Sun Dec 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.11-7
- Updated to 1.2.11

* Tue Dec 15 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-16
- Rebuilt for dav1d

* Wed Nov 04 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-14
- Rebuilt 

* Sun Nov 01 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-13
- Rebuilt for libdvdread

* Wed Jul 08 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-12
- Rebuilt for aom

* Tue Jun 23 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-11
- Rebuilt for ffmpeg

* Sun May 24 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-10
- Updated to current commit

* Thu Apr 09 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-9
- Updated to current commit

* Wed Feb 19 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-8
- Updated to current commit

* Sat Dec 14 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.10-7
- Updated to 1.2.10-7
- Abi bump

* Tue Nov 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-18
- Rebuilt for libdvdread
- Updated to current commit

* Mon Nov 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-17
- Updated to current commit

* Fri Nov 08 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-16
- Rebuilt for faad2

* Mon Sep 09 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-15
- Rebuilt for libnfs

* Mon Sep 09 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-14
- Updated to current commit

* Tue Mar 19 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-13
- Updated to current commit

* Thu Dec 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-12
- We are using mercurial commits
- Enabled libaom and others missed plugins

* Thu Dec 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-11  
- Rebuilt for ffmpeg

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-10  
- Automatic Mass Rebuild

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-9  
- Automatic Mass Rebuild

* Tue Feb 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-8  
- Rebuilt for libcdio

* Fri Jan 12 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.9-7  
- Updated to 1.2.9

* Wed Oct 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-11  
- Automatic Mass Rebuild

* Wed Oct 11 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-10  
- Rebuilt for ImageMagick

* Fri Aug 25 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-9  
- Automatic Mass Rebuild
- ImageMagic patch

* Mon Jul 31 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-7  
- Automatic Mass Rebuild

* Tue Apr 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-5  
- Automatic Mass Rebuild

* Sat Mar 18 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.2.8-4
- Updated to 1.2.8-4

* Wed Mar 15 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.8-3  
- Automatic Mass Rebuild

* Sat Feb 25 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 1.2.8-2
- Updated to 1.2.8-2

* Fri Sep 02 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.2.6-11
- Rebuilt for libvpx

* Thu Jul 07 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.2.6-10
- Rebuilt for FFmpeg 3.1
- Disabled xcb 
- Enabled esound

* Sun May 01 2016 Sérgio Basto <sergio@serjux.com> - 1.2.6-9
- Add patch to build with ffmpeg3
