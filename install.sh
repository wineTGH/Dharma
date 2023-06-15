#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root!"
  exit
fi

DIST="Fedora"

function install_glass_dependencies {
case `uname` in
	Linux )
	LINUX=1
	which dnf >> /dev/null && {
		DIST="Fedora"
		dnf install cmake gcc gcc-c++ \
		libglvnd-devel fontconfig-devel \
		spice-protocol make nettle-devel \
		pkgconf-pkg-config binutils-devel \
		libXi-devel libXinerama-devel \
		libXcursor-devel libXpresent-devel \
		libxkbcommon-x11-devel wayland-devel \
		wayland-protocols-devel libXScrnSaver-devel \
		libXrandr-devel dejavu-sans-mono-fonts \
		pipewire-devel libsamplerate-devel \
		pulseaudio-libs-devel -y    	
		return;
	}
     
	which apt-get >> /dev/null && {
		DIST="Debian" 
		apt-get install binutils-dev cmake fonts-dejavu-core libfontconfig-dev \
		gcc g++ pkg-config libegl-dev libgl-dev libgles-dev libspice-protocol-dev \
		nettle-dev libx11-dev libxcursor-dev libxi-dev libxinerama-dev \
		libxpresent-dev libxss-dev libxkbcommon-dev libwayland-dev wayland-protocols \
		libpipewire-0.3-dev libpulse-dev libsamplerate0-dev -y
		return; 
	}
	;;
esac
}

function install_looking_glass {
	install_glass_dependencies
	echo "Downloading looking glass..."
	wget -O /tmp/looking-glass.tar.gz https://looking-glass.io/artifact/stable/source
	tar -xzvf /tmp/looking-glass.tar.gz -C /tmp
	echo "Installing looking glass..."
	cd /tmp/looking-glass-*
	mkdir client/build
	cd client/build 
	cmake ../
	make install
}


! which looking-glass-client >> /dev/null && install_looking_glass
"d /dev/shm 0755 ${NORMAL_USER} kvm - " >> /etc/tmpfiles.d/10-looking-glass.conf
"/dev/shm/* rw," >> /etc/apparmor.d/local/abstractions/libvirt-qemu