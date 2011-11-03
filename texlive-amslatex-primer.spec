# revision 22612
# category Package
# catalog-ctan /info/amslatex/primer
# catalog-date 2011-05-25 00:58:45 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-amslatex-primer
Version:	2.2
Release:	1
Summary:	Getting up and running with AMS-LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/amslatex/primer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amslatex-primer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amslatex-primer.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The document aims to get you up and running with AMS-LaTeX as
quickly as possible. These instructions (along with a template
file template.tex) are not a substitute for the full
documentation, but they may get you started quickly enough so
that you will only need to refer to the main documentation
occasionally. In addition to 'AMS-LaTeX out of the box', the
document contains: - a section describing how to draw
commutative diagrams using Xy-pic; and - a section describing
how to use amsrefs to create a bibliography.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/amslatex-primer/README
%doc %{_texmfdistdir}/doc/latex/amslatex-primer/amshelp.md5
%doc %{_texmfdistdir}/doc/latex/amslatex-primer/amshelp.pdf
%doc %{_texmfdistdir}/doc/latex/amslatex-primer/amshelp.tex
%doc %{_texmfdistdir}/doc/latex/amslatex-primer/template.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
