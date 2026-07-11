%global tl_name hobsub
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Construct package bundles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hobsub
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobsub.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hobsub.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Heiko Oberdiek's hobsub package (and hobsub-hyperref and hobsub-generic
packages) defined a mechanism for concatenating multiple files into a
single file for faster loading. The disadvantage is that it introduces
hard dependencies between the source files that are included and
complicates distribution and updates. It was principally used with
hyperref but is not currently used in any standard packages in TeX Live.
The packages are still distributed as simple stubs that reference the
included packages via \RequirePackage rather than copying their source.
The documented source of the original packages is available at github,
but is not distributed to CTAN.

