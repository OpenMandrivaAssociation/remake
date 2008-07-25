%define oversion 3.80+dbg-0.62

Summary:        A gnu make version including a debuger
Name:		remake
Version:        3.80_0.62
Release:        %mkrel 4
License:        GPLv2+
Group:          Development/Other
Url:            http://bashdb.sourceforge.net/remake/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{oversion}.tar.bz2
BuildRequires:  readline-devel
BuildRequires:	emacs
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
remake is a patched and modernized version of GNU make utility that
adds improved error reporting, the ability to trace execution in a
comprehensible way, and a debugger.

%prep
%setup -qn %{name}-%{oversion}

%build
%configure2_5x
%make

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%makeinstall_std
%{__rm} -f %{buildroot}/%{_infodir}/make*

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* COPYING INSTALL NEWS README* TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/emacs/site-lisp/mdb.el
%{_infodir}/*
%{_mandir}/man1/remake.*
