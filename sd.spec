%define name sd
%define version 1.0.0
%define release 11%{?dist}

Summary:  Intuitive find & replace CLI (sed alternative)
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/chmln/sd
Source0:  https://github.com/chmln/sd/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}
%undefine _package_note_file

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
install -m 755 target/release/%{name} %{buildroot}/bin/

# Copy Bash completion
install -m 755 gen/completions/%{name}.bash %{buildroot}/etc/bash_completion.d/

# Copy the man page to /usr/share/man/man1 in the buildroot
gzip gen/%{name}.1
install -m 644 gen/%{name}.1.gz %{buildroot}/usr/share/man/man1/

%files
# List all the files to be included in the package
/bin/%{name}
/etc/bash_completion.d/%{name}.bash
/usr/share/man/man1/%{name}.1.gz

%changelog
* Tue Dec 1 2025 Danie de Jager - 1.0.0-11
- Rebuilt using rustc 1.91.1
* Fri Aug 15 2025 Danie de Jager - 1.0.0-10
- Rebuilt using rustc 1.89.0
* Thu May 29 2025 Danie de Jager - 1.0.0-9
- Rebuilt using rustc 1.87.0
* Sun Apr 20 2025 Danie de Jager - 1.0.0-8
- Rebuilt using rustc 1.86.0
* Thu Feb 6 2025 Danie de Jager - 1.0.0-7
- Rebuilt using rustc 1.84.1
* Mon Nov 25 2024 Danie de Jager - 1.0.0-6
- Rebuilt using rustc 1.82
* Mon Aug 5 2024 Danie de Jager - 1.0.0-5
- Rebuilt using rustc 1.80
* Fri Apr 26 2024 Danie de Jager - 1.0.0-4
- Rebuilt using rustc 1.77.2
* Wed Nov 22 2023 Danie de Jager - 1.0.0-3
- Initial RPM build using rustc 1.75.0
