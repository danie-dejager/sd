%define name sd
%define version 1.0.0
%define release 5%{?dist}

Summary:  Intuitive find & replace CLI (sed alternative)
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/chmln/sd
Source0:  https://github.com/chmln/sd/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: upx
BuildRequires: gzip

%description
sd is an intuitive find & replace CLI.

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release
upx target/release/%{name}

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/etc/bash_completion.d/
mkdir -p %{buildroot}/usr/share/man/man1

# Copy the binary to /bin in the buildroot
install -m 755 target/release/%{name} %{buildroot}/bin/

# Copy Bash completion
install -m 755 gen/completions/sd.bash %{buildroot}/etc/bash_completion.d/

# Copy the man page to /usr/share/man/man1 in the buildroot
gzip gen/sd.1
install -m 644 gen/sd.1.gz %{buildroot}/usr/share/man/man1/

%files
# List all the files to be included in the package
/bin/sd
/etc/bash_completion.d/sd.bash
/usr/share/man/man1/sd.1.gz

%changelog
* Fri Apr 26 2024 Danie de Jager - 1.0.0.5
- compress final binary with upx.
* Fri Apr 26 2024 Danie de Jager - 1.0.0.4
- Rebuilt using rustc 1.77.2
* Wed Nov 22 2023 Danie de Jager - 1.0.0.3
- Initial RPM build using rustc 1.75.0
