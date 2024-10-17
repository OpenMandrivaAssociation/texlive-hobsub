Name:		texlive-hobsub
Version:	52810
Release:	2
Summary:	Construct package bundles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hobsub
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobsub.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hobsub.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Heiko Oberdiek's hobsub package (and hobsub-hyperref and
hobsub-generic packages) defined a mechanism for concatenating
multiple files into a single file for faster loading. The
disadvantage is that it introduces hard dependencies between
the source files that are included and complicates distribution
and updates. It was principally used with hyperref but is not
currently used in any standard packages in TeX Live. The
packages are still distributed as simple stubs that reference
the included packages via \RequirePackage rather than copying
their source. The documented source of the original packages is
available at github, but is not distributed to CTAN.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hobsub
%doc %{_texmfdistdir}/doc/latex/hobsub

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
