Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Summary(de):	GNUs bc (eine Zahlenverarbeitungssprache) und dc (ein Rechner)
Summary(fr):	GNU bc
Summary(pl):	GNU bc (jêzyk obliczeñ numerycznych) i dc (kalkulator)
Summary(tr):	GNU hesap makinasý
Name:		bc
Version:	1.06
Release:	3
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://ftp.gnu.org/pub/gnu/bc/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRequires:	flex
BuildRequires:	bison
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

%description -l fr
bc est est un outil de calcul en mode texte. Il a des fonctionnalités
étendues comme la conversion de base. il peut aussi accepter l'entrée
sur stdin et retourner le résultat. dc est la version RPN.

%description -l pl
Pakiet bc zawiera w sobie programy bc i dc. Bc jest oferuje jêzyk
obliczeñ numerycznych w którym mo¿na okre¶liæ precyzjê obliczeñ. Dc
jest natomiast interakcyjnym bazuj±cym na notacji RPN kalkulatorem w
którym tak¿e mo¿na z góry okre¶liæ precyzjê obliczeñ.

%description -l tr
bc metin ekranda çalýþan bir hesap makinasýdýr. Taban dönüþümü gibi
ileri yetenekleri vardýr.

%prep
%setup -q
%patch0 -p1

%build
aclocal
%configure \
	--with-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog FAQ NEWS README

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/dc.info*

%clean 
rm -rf $RPM_BUILD_ROOT
