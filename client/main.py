# Python file template

# By wineT (Anatoly Bogomolov)
import wmi

def main():
	c = wmi.WMI()
	for cdrom in c.Win32_CDROMDrive():
		print(cdrom.Drive, cdrom.MediaLoader)

if __name__ == "__main__":
	main()
