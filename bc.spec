Summary:     	GNU bc
Summary(de): 	GNU bc 
Summary(fr): 	GNU bc
Summary(pl): 	Kalkulator bc GNU
Summary(tr): 	GNU hesap makinasý
Name:        	bc
Version:     	1.05a
Release:     	7
Copyright:   	GPL
Group:       	Applications/Math
Group(pl):	Aplikacje/Matematyczne
Source:      	ftp://prep.ai.mit.edu/pug/gnu/%{name}-%{version}.tar.gz
Patch0:      	bc-info.patch
Patch1:      	bc-DESTDIR.patch
Prereq:      	/sbin/install-info 
Buildroot:   	/tmp/%{name}-%{version}-root

%description
bc is a text mode calculator of sorts.  It has many extended
features such as base translation.  It can also accept input
from stdin and return output. dc is the RPN version.

%description -l de
bc ist eine Art Textmodus-Rechner, der viele erweiterte Funktionen
wie Basisübersetzung enthält. Er kann auch Eingaben von
stdin annehmen und die Ergebnisse ausgeben. dc ist die RPN-Version.

%description -l fr
bc est est un outil de calcul en mode texte. Il a des fonctionnalités
étendues comme la conversion de base. il peut aussi accepter l'entrée
sur stdin et retourner le résultat. dc est la version RPN.

%description -l pl
Bc to kalkulator pracuj±cy w trybie tekstowym, który posiada wiele 
rozbudowanych funkcji. W czasie pracy mo¿e pobieraæ dane ze standardowego
wej¶cia (stdin) i wysy³aæ je na standardowe wyj¶cie (stdout).

%description -l tr
bc metin ekranda çalýþan bir hesap makinasýdýr. Taban dönüþümü gibi ileri
yetenekleri vardýr.

%prep
%setup  -q -n %{name}-1.05
%patch0 -p1
%patch1 -p1

%build
aclocal
LDFLAGS="-s"; export LDFLAGS
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make \
    DESTDIR=$RPM_BUILD_ROOT \
    install

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/dc.info,%{_mandir}/man1/*}

%post
/sbin/install-info %{_infodir}/dc.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/dc.info.gz /etc/info-dir
fi

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/dc.info.gz

%clean 
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat May 29 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.05a-7]
- based on RH spec,
- spec rewrited by PLD team,
- pl translation Wojtek ¦lusarczyk <wojtek@shadow.eu.org>.
