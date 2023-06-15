#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root!"
  exit
fi

function install_glass_dependencies {
	which dnf >> /dev/null && {
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
		apt-get install binutils-dev cmake fonts-dejavu-core libfontconfig-dev \
		gcc g++ pkg-config libegl-dev libgl-dev libgles-dev libspice-protocol-dev \
		nettle-dev libx11-dev libxcursor-dev libxi-dev libxinerama-dev \
		libxpresent-dev libxss-dev libxkbcommon-dev libwayland-dev wayland-protocols \
		libpipewire-0.3-dev libpulse-dev libsamplerate0-dev -y
		return; 
	}
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

function install_dharma_dependencies {
	which dnf >> /dev/null && {
		dnf install gobject-introspection-devel cairo-gobject-devel pkg-config python3-devel gtk4 -y
		return;
	}
     
	which apt-get >> /dev/null && {
		apt-get install libgirepository1.0-dev libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0 -y
		return; 
	}
}

function install_virt_dependencies {
	which dnf >> /dev/null && {
		dnf install @virtualization -y
		return;
	}
     
	which apt-get >> /dev/null && {
		apt-get install apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
		return; 
	}

	sudo systemctl enable libvirtd
	sudo systemctl start libvirtd
}

function add_modules {
	which dnf >> /dev/null && {
		echo "kvmgt vfio_mdev" > /etc/modules-load.d/gvt-g.conf
		return;
	}
     
	which apt-get >> /dev/null && {
		#Adding kernel modules
		echo "vfio_mdev" >> /etc/modules
		echo "kvmgt" >> /etc/modules

		#Updating initramfs
		update-initramfs -u
		return; 
	}

	sudo systemctl enable libvirtd
	sudo systemctl start libvirtd
}

! which looking-glass-client >> /dev/null && install_looking_glass
"d /dev/shm 0755 ${NORMAL_USER} kvm - " >> /etc/tmpfiles.d/10-looking-glass.conf
"/dev/shm/* rw," >> /etc/apparmor.d/local/abstractions/libvirt-qemu
install_virt_dependencies
install_dharma_dependencies
pip install .
add_modules
echo "Update grub and reboot your PC"