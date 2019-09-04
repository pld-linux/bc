Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Summary(de.UTF-8):	GNUs bc (eine Zahlenverarbeitungssprache) und dc (ein Rechner)
Summary(es.UTF-8):	GNU bc (lenguaje para cálculos matemáticos) y dc (calculadora)
Summary(fr.UTF-8):	GNU bc
Summary(pl.UTF-8):	GNU bc (język obliczeń numerycznych) i dc (kalkulator)
Summary(pt_BR.UTF-8):	GNU bc - calculadora de linha de comando
Summary(ru.UTF-8):	GNU bc (язык обработки чисел) и dc (калькулятор)
Summary(tr.UTF-8):	GNU hesap makinası
Summary(uk.UTF-8):	GNU bc (мова обробки чисел) та dc (калькулятор)
Name:		bc
Version:	1.07.1
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	http://ftp.gnu.org/gnu/bc/%{name}-%{version}.tar.gz
# Source0-md5:	cda93857418655ea43590736fc3ca9fc
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ae2cf58a4382d6a0bfeaab3a6a11bd30
Source2:	bc.desktop
Source3:	dc.desktop
Source4:	bc.png
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/bc/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 5.0
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive arbitrary
precision stack based calculator, which can be used as a text mode
calculator. Install the bc package if you need its number handling
capabilities or if you would like to use its text mode calculator.

%description -l de.UTF-8
Das bc-Paket enthält bc und dc. Bc ist eine Zahlenverarbeitungssprache
mit beliebiger Genauigkeit. Dc ist ein interaktiver, Stapelbasierter
Rechner mit beliebiger Genauigkeit, der im Textmodus benutzt werden
kann. Installieren Sie bc, wenn Sie seine
Zahlenverarbeitungsfähigkeiten brauchen, oder wenn Sie einen
Textmodus-Rechner haben wollen.

%description -l pt_BR.UTF-8
bc é uma calculadora modo texto. Ela possui várias características
estendidas como translação de base.

%description -l fr.UTF-8
bc est est un outil de calcul en mode texte. Il a des fonctionnalités
étendues comme la conversion de base. il peut aussi accepter l'entrée
sur stdin et retourner le résultat. dc est la version RPN.

%description -l pl.UTF-8
Pakiet bc zawiera w sobie programy bc i dc. Bc jest oferuje język
obliczeń numerycznych w którym można określić precyzję obliczeń. Dc
jest natomiast interakcyjnym bazującym na notacji RPN kalkulatorem w
którym także można z góry określić precyzję obliczeń.

%description -l ru.UTF-8
Пакет bc включает bc и dc. Bc - это арифметический язык для обработки
чисел произвольной точности. Dc - это интерактивный стековый
калькулятор произвольной точности, который можно использовать как
калькулятор в текстовом режиме.

%description -l tr.UTF-8
bc metin ekranda çalışan bir hesap makinasıdır. Taban dönüşümü gibi
ileri yetenekleri vardır.

%description -l uk.UTF-8
Пакет bc містить bc та dc. Bc - це арифметична мова для обробки чисел
довільної точності. Dc - це інтерактивний стековий калькулятор
довільної точності, який можна використовувати як калькулятор у
текстовому режимі.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README
%attr(755,root,root) %{_bindir}/bc
%attr(755,root,root) %{_bindir}/dc
%{_desktopdir}/bc.desktop
%{_desktopdir}/dc.desktop
%{_pixmapsdir}/bc.png
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/bc.info*
%{_infodir}/dc.info*
