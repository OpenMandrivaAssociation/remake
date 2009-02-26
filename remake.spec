%define oversion 3.80+dbg-0.62

Summary:        A gnu make version including a debuger
Name:		remake
Version:        3.80_0.62
Release:        %mkrel 6
License:        GPLv2+
Group:          Development/Other
Url:            http://bashdb.sourceforge.net/remake/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{oversion}.tar.bz2
Patch0:         remake-3.80+dbg-0.62-fix-format-errors.patch
BuildRequires:  readline-devel
BuildRequires:	emacs
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
remake is a patched and modernized version of GNU make utility that
adds improved error reporting, the ability to trace execution in a
comprehensible way, and a debugger.

%prep
%setup -qn %{name}-%{oversion}
%patch0 -p 1

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}

%makeinstall_std
%{__rm} -f %{buildroot}/%{_infodir}/make*

%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog* COPYING INSTALL NEWS README* TODO
%{_bindir}/%{name}
%{_datadir}/emacs/site-lisp/mdb.el
%{_infodir}/*
%{_mandir}/man1/remake.*
