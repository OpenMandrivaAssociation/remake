%define oversion 3.81+dbg-0.2

Summary:	A gnu make version including a debuger
Name:		remake
Version:	3.81_0.2
Release:	3
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


%changelog
* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 3.81_0.2-2mdv2011.0
+ Revision: 653311
- rebuild

* Sun Jun 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.81_0.2-1mdv2010.0
+ Revision: 383539
- update to new version 3.81+dbg-0.2
- Patch0: fix format not a string literal and no format arguments error
- spec file clean

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.80_0.62-6mdv2009.1
+ Revision: 345229
- rebuild for latest readline
- fix format errors

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 3.80_0.62-5mdv2009.0
+ Revision: 260210
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 3.80_0.62-4mdv2009.0
+ Revision: 248346
- rebuild

* Wed Mar 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.80_0.62-2mdv2008.1
+ Revision: 187168
- remove conflicting files with make (#38801)
- add buildrequires on emacs

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.80_0.62-1mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode bz2 extension


* Wed Feb 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.80_0.62-1mdv2007.0
+ Revision: 127051
- Import remake

