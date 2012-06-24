Summary:     GNU bc
Summary(de): GNU bc 
Summary(fr): GNU bc
Summary(pl): Kalkulator bc GNU
Summary(tr): GNU hesap makinas�
Name:        bc
Version:     1.05a
Release:     3
Copyright:   GPL
Group:       Applications/Math
Source:      ftp://prep.ai.mit.edu/pug/gnu/%{name}-%{version}.tar.gz
Patch0:      bc-info.patch
Prereq:      /sbin/install-info grep
Buildroot:   /tmp/%{name}-%{version}-root

%description
bc is a text mode calculator of sorts.  It has many extended
features such as base translation.  It can also accept input
from stdin and return output. dc is the RPN version.

%description -l de
bc ist eine Art Textmodus-Rechner, der viele erweiterte Funktionen
wie Basis�bersetzung enth�lt. Er kann auch Eingaben von
stdin annehmen und die Ergebnisse ausgeben. dc ist die RPN-Version.

%description -l fr
bc est est un outil de calcul en mode texte. Il a des fonctionnalit�s
�tendues comme la conversion de base. il peut aussi accepter l'entr�e
sur stdin et retourner le r�sultat. dc est la version RPN.

%description -l pl
Bc to kalkulator pracuj�cy w trybie tekstowym, kt�ry posiada wiele 
rozbudowanych funkcji. W czasie pracy mo�e pobiera� dane ze standardowego
wej�cia (stdin) i wysy�a� je na standardowe wyj�cie (stdout).

%description -l tr
bc metin ekranda �al��an bir hesap makinas�d�r. Taban d�n���m� gibi ileri
yetenekleri vard�r.

%prep
%setup -q -n %{name}-1.05
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

make prefix=$RPM_BUILD_ROOT/usr install

gzip -nf9 $RPM_BUILD_ROOT/usr/{info/dc.info,man/man1/*}

%post
/sbin/install-info /usr/info/dc.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/dc.info.gz /etc/info-dir
fi

%files
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
%attr(644, root, root) /usr/info/dc.info.gz

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Dec 29 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.05a-3]
- standarized {un}registering info pages (added bc-info.patch),
- added gzipping man pages.

* Sun Sep 27 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.05a-2]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added "rm -rf $RPM_BUILD_ROOT on top %install,
- simplifications in %files nad %install,
- added full %attr description in %files.

* Wed Jun 17 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- added %defattr support,
- build from non root's account.

* Sun Jun 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.05 with build root.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Erik Troan <ewt@redhat.com>
- got upgrades of info entry working (I hope)

* Sun Apr 05 1998 Erik Troan <ewt@redhat.com>
- fixed incorrect info entry

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- added install-info support

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.03 to 1.04

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
