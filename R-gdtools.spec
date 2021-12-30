#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gdtools
Version  : 0.2.3
Release  : 26
URL      : https://cran.r-project.org/src/contrib/gdtools_0.2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gdtools_0.2.3.tar.gz
Summary  : Utilities for Graphical Rendering
Group    : Development/Tools
License  : GPL-3.0
Requires: R-gdtools-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-systemfonts
BuildRequires : R-Rcpp
BuildRequires : R-systemfonts
BuildRequires : buildreq-R
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(freetype2)

%description
# gdtools
<!-- badges: start -->
[![CRAN
status](https://www.r-pkg.org/badges/version/gdtools)](https://CRAN.R-project.org/package=gdtools)
[![R build
status](https://github.com/davidgohel/gdtools/workflows/R-CMD-check/badge.svg)](https://github.com/davidgohel/gdtools/actions)
[![Coverage
Status](https://img.shields.io/codecov/c/github/davidgohel/gdtools/master.svg)](https://codecov.io/github/davidgohel/gdtools?branch=master)
<!-- badges: end -->

%package lib
Summary: lib components for the R-gdtools package.
Group: Libraries

%description lib
lib components for the R-gdtools package.


%prep
%setup -q -c -n gdtools
cd %{_builddir}/gdtools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620763914

%install
export SOURCE_DATE_EPOCH=1620763914
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdtools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gdtools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gdtools || :


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
