%define name sd
%define version 1.0.0
%define release 3%{?dist}

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

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/etc/bash_completion.d/
mkdir -p %{buildroot}/usr/share/man/man1

# Copy the binary to /bin in the buildroot
install -m 755 target/release/sd %{buildroot}/bin/

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
* Wed Nov 22 2023 Danie de Jager - 1.0.0.3
- Initial RPM build
