Summary:	Breton dictionary for aspell
Summary(br):	Geriadur brezhonek evit aspell
Summary(pl):	Bretoñski s³ownik dla aspella
Name:		aspell-br
Version:	0.50
%define	subv	2
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/br/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	800c7a28e09bd7734d1501cb7a91ad8f
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Breton dictionary (i.e. word list) for aspell.

%description -l br
Geriadur brezhonek evit aspell.

%description -l pl
Bretoñski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
