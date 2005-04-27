Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Summary(de):	GNUs bc (eine Zahlenverarbeitungssprache) und dc (ein Rechner)
Summary(es):	GNU bc (lenguaje para cálculos matemáticos) y dc (calculadora)
Summary(fr):	GNU bc
Summary(pl):	GNU bc (jêzyk obliczeñ numerycznych) i dc (kalkulator)
Summary(pt_BR):	GNU bc - calculadora de linha de comando
Summary(ru):	GNU bc (ÑÚÙË ÏÂÒÁÂÏÔËÉ ÞÉÓÅÌ) É dc (ËÁÌØËÕÌÑÔÏÒ)
Summary(tr):	GNU hesap makinasý
Summary(uk):	GNU bc (ÍÏ×Á ÏÂÒÏÂËÉ ÞÉÓÅÌ) ÔÁ dc (ËÁÌØËÕÌÑÔÏÒ)
Name:		bc
Version:	1.06
Release:	15
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.gnu.org/pub/gnu/bc/%{name}-%{version}.tar.gz
# Source0-md5:	d44b5dddebd8a7a7309aea6c36fda117
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ae2cf58a4382d6a0bfeaab3a6a11bd30
Source2:	bc.desktop
Source3:	dc.desktop
Source4:	bc.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-readline.patch
Patch2:		%{name}-flex.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive arbitrary
precision stack based calculator, which can be used as a text mode
calculator. Install the bc package if you need its number handling
capabilities or if you would like to use its text mode calculator.

%description -l de
Das bc-Paket enthält bc und dc. Bc ist eine Zahlenverarbeitungssprache
mit beliebiger Genauigkeit. Dc ist ein interaktiver, Stapelbasierter
Rechner mit beliebiger Genauigkeit, der im Textmodus benutzt werden
kann. Installieren Sie bc, wenn Sie seine
Zahlenverarbeitungsfähigkeiten brauchen, oder wenn Sie einen
Textmodus-Rechner haben wollen.

%description -l pt_BR
bc é uma calculadora modo texto. Ela possui várias características
estendidas como translação de base.

%description -l fr
bc est est un outil de calcul en mode texte. Il a des fonctionnalités
étendues comme la conversion de base. il peut aussi accepter l'entrée
sur stdin et retourner le résultat. dc est la version RPN.

%description -l pl
Pakiet bc zawiera w sobie programy bc i dc. Bc jest oferuje jêzyk
obliczeñ numerycznych w którym mo¿na okre¶liæ precyzjê obliczeñ. Dc
jest natomiast interakcyjnym bazuj±cym na notacji RPN kalkulatorem w
którym tak¿e mo¿na z góry okre¶liæ precyzjê obliczeñ.

%description -l pt_BR
bc é uma calculadora modo texto. Ela possui várias características
estendidas como translação de base.

%description -l ru
ðÁËÅÔ bc ×ËÌÀÞÁÅÔ bc É dc. Bc - ÜÔÏ ÁÒÉÆÍÅÔÉÞÅÓËÉÊ ÑÚÙË ÄÌÑ ÏÂÒÁÂÏÔËÉ
ÞÉÓÅÌ ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ. Dc - ÜÔÏ ÉÎÔÅÒÁËÔÉ×ÎÙÊ ÓÔÅËÏ×ÙÊ
ËÁÌØËÕÌÑÔÏÒ ÐÒÏÉÚ×ÏÌØÎÏÊ ÔÏÞÎÏÓÔÉ, ËÏÔÏÒÙÊ ÍÏÖÎÏ ÉÓÐÏÌØÚÏ×ÁÔØ ËÁË
ËÁÌØËÕÌÑÔÏÒ × ÔÅËÓÔÏ×ÏÍ ÒÅÖÉÍÅ.

%description -l tr
bc metin ekranda çalýþan bir hesap makinasýdýr. Taban dönüþümü gibi
ileri yetenekleri vardýr.

%description -l uk
ðÁËÅÔ bc Í¦ÓÔÉÔØ bc ÔÁ dc. Bc - ÃÅ ÁÒÉÆÍÅÔÉÞÎÁ ÍÏ×Á ÄÌÑ ÏÂÒÏÂËÉ ÞÉÓÅÌ
ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦. Dc - ÃÅ ¦ÎÔÅÒÁËÔÉ×ÎÉÊ ÓÔÅËÏ×ÉÊ ËÁÌØËÕÌÑÔÏÒ
ÄÏ×¦ÌØÎÏ§ ÔÏÞÎÏÓÔ¦, ÑËÉÊ ÍÏÖÎÁ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ ÑË ËÁÌØËÕÌÑÔÏÒ Õ
ÔÅËÓÔÏ×ÏÍÕ ÒÅÖÉÍ¦.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar -xf - -C $RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} %{SOURCE3} \
	$RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%{_infodir}/*.info*
