%global tl_name amslatex-primer
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.3
Release:	%{tl_revision}.1
Summary:	Getting up and running with AMS-LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/amslatex/primer
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amslatex-primer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amslatex-primer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document aims to get you up and running with AMS-LaTeX as quickly as
possible. These instructions (along with a template file template.tex)
are not a substitute for the full documentation, but they may get you
started quickly enough so that you will only need to refer to the main
documentation occasionally. In addition to 'AMS-LaTeX out of the box',
the document contains: a section describing how to draw commutative
diagrams using Xy-pic; and a section describing how to use amsrefs to
create a bibliography.

