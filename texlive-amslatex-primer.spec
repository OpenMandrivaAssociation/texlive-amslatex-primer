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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/amslatex-primer
%doc %{_datadir}/texmf-dist/doc/latex/amslatex-primer/README
%doc %{_datadir}/texmf-dist/doc/latex/amslatex-primer/amshelp.md5
%doc %{_datadir}/texmf-dist/doc/latex/amslatex-primer/amshelp.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amslatex-primer/amshelp.tex
%doc %{_datadir}/texmf-dist/doc/latex/amslatex-primer/template.tex
