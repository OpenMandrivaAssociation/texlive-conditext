%global tl_name conditext
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Define and manage conditional content
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conditext
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conditext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conditext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some commands to define and manage conditional
content in a LaTeX source document. A conditional content, in the sense
within this is understood in this package, is a text (including
mathematical or other formulas) and/or a graphical element (diagram,
figure, image...) as substitutable forms, which, according to a
condition test, may or may not appear in the generated document. One of
the most common forms of conditional content management is multilingual
; but it can also include versioning, confidentiality levels, and so on.
The philosophy of this package is based on the respective notions of
condition field, condition property and condition space. With this
package, any substitutable form in a source document is identified by a
condition field and a condition property. The condition field is a
functional theme that allows you to group together substitutable forms
for the same conditional management. The condition property is a
functional characterization specific to each substitutable form of a
single condition domain. The condition space is used to designate the
substitutable form(s) that must appear in the generated document. A
condition space is defined by specifying a condition domain and a
condition property to match with one or more substitutable forms.

