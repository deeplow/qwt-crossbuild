Name:		qubes-windows-tools
Version:	4.0
Release:	209
Summary:	Qubes Tools for Windows VMs
Group:		Qubes
License:	GPL
Obsoletes:	qubes-core-dom0-pvdrivers
BuildRequires:	genisoimage
BuildArch:	noarch
Source0:	qubes-tools-x64.msi
Source1:	qubes-tools-x86.msi
Source2:	iso-README.txt

%prep
%setup -c -T

%description
PV Drivers and Qubes Tools for Windows AppVMs. Bundled for Windows 7 64bit.

%build

mkdir -p iso-content
cp %{SOURCE0} iso-content/
cp %{SOURCE1} iso-content/
cp %{SOURCE2} iso-content/
genisoimage -o qubes-windows-tools-%{version}.%{release}.iso -m .gitignore -JR iso-content


%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/qubes/
cp qubes-windows-tools-%{version}.%{release}.iso $RPM_BUILD_ROOT/usr/lib/qubes/
ln -s qubes-windows-tools-%{version}.%{release}.iso $RPM_BUILD_ROOT/usr/lib/qubes/qubes-windows-tools.iso

%files
/usr/lib/qubes/qubes-windows-tools-%{version}.%{release}.iso
/usr/lib/qubes/qubes-windows-tools.iso

%changelog

