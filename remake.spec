%define oversion 3.81+dbg-0.2

Summary:	A gnu make version including a debuger
Name:		remake
Version:	3.81_0.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
Url:		http://bashdb.sourceforge.net/remake/
Source0:	http://downloads.sourceforge.net/bashdb/%{name}-%{oversion}.tar.bz2
Patch0:		remake-3.81+dbg-0.2-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	readline-devel
BuildRequires:	emacs
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
remake is a patched and modernized version of GNU make utility that
adds improved error reporting, the ability to trace execution in a
comprehensible way, and a debugger.

%prep
%setup -qn %{name}-%{oversion}
%patch0 -p1

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
%{_datadir}/emacs/site-lisp/mdb.el*
%{_infodir}/*
