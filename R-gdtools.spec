#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-gdtools
Version  : 0.3.3
Release  : 41
URL      : https://cran.r-project.org/src/contrib/gdtools_0.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gdtools_0.3.3.tar.gz
Summary  : Utilities for Graphical Rendering and Fonts Management
Group    : Development/Tools
License  : GPL-3.0
Requires: R-gdtools-lib = %{version}-%{release}
Requires: R-gdtools-license = %{version}-%{release}
Requires: R-Rcpp
Requires: R-curl
Requires: R-fontquiver
Requires: R-gfonts
Requires: R-htmltools
Requires: R-systemfonts
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : R-fontquiver
BuildRequires : R-gfonts
BuildRequires : R-htmltools
BuildRequires : R-systemfonts
BuildRequires : buildreq-R
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(freetype2)

%description
formatted strings and to check the availability of a font. 
  Another set of functions is provided to support the collection 
  of fonts from 'Google Fonts' in a cache. Their use is simple within 
  'R Markdown' documents and 'shiny' applications but also with graphic 
  productions generated with the 'ggiraph', 'ragg' and 'svglite' packages 
  or with tabular productions from the 'flextable' package.

%package lib
Summary: lib components for the R-gdtools package.
Group: Libraries
Requires: R-gdtools-license = %{version}-%{release}

%description lib
lib components for the R-gdtools package.


%package license
Summary: license components for the R-gdtools package.
Group: Default

%description license
license components for the R-gdtools package.


%prep
%setup -q -n gdtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679941428

%install
export SOURCE_DATE_EPOCH=1679941428
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-gdtools
cp %{_builddir}/gdtools/LICENSE %{buildroot}/usr/share/package-licenses/R-gdtools/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gdtools/DESCRIPTION
/usr/lib64/R/library/gdtools/INDEX
/usr/lib64/R/library/gdtools/LICENSE
/usr/lib64/R/library/gdtools/Meta/Rd.rds
/usr/lib64/R/library/gdtools/Meta/features.rds
/usr/lib64/R/library/gdtools/Meta/hsearch.rds
/usr/lib64/R/library/gdtools/Meta/links.rds
/usr/lib64/R/library/gdtools/Meta/nsInfo.rds
/usr/lib64/R/library/gdtools/Meta/package.rds
/usr/lib64/R/library/gdtools/NAMESPACE
/usr/lib64/R/library/gdtools/NEWS
/usr/lib64/R/library/gdtools/R/gdtools
/usr/lib64/R/library/gdtools/R/gdtools.rdb
/usr/lib64/R/library/gdtools/R/gdtools.rdx
/usr/lib64/R/library/gdtools/R/sysdata.rdb
/usr/lib64/R/library/gdtools/R/sysdata.rdx
/usr/lib64/R/library/gdtools/css/liberation-sans.css
/usr/lib64/R/library/gdtools/help/AnIndex
/usr/lib64/R/library/gdtools/help/aliases.rds
/usr/lib64/R/library/gdtools/help/gdtools.rdb
/usr/lib64/R/library/gdtools/help/gdtools.rdx
/usr/lib64/R/library/gdtools/help/paths.rds
/usr/lib64/R/library/gdtools/html/00Index.html
/usr/lib64/R/library/gdtools/html/R.css
/usr/lib64/R/library/gdtools/include/gdtools.h
/usr/lib64/R/library/gdtools/include/gdtools_RcppExports.h
/usr/lib64/R/library/gdtools/include/gdtools_types.cpp
/usr/lib64/R/library/gdtools/include/gdtools_types.h
/usr/lib64/R/library/gdtools/tests/testthat.R
/usr/lib64/R/library/gdtools/tests/testthat/helper-fontconfig.R
/usr/lib64/R/library/gdtools/tests/testthat/test-raster.R
/usr/lib64/R/library/gdtools/tests/testthat/test-str_extents.R
/usr/lib64/R/library/gdtools/tests/testthat/test-str_metrics.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gdtools/libs/gdtools.so
/usr/lib64/R/library/gdtools/libs/gdtools.so.avx2
/usr/lib64/R/library/gdtools/libs/gdtools.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-gdtools/8624bcdae55baeef00cd11d5dfcfa60f68710a02
