#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jpeg
Version  : 0.1.10
Release  : 53
URL      : https://cran.r-project.org/src/contrib/jpeg_0.1-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jpeg_0.1-10.tar.gz
Summary  : Read and write JPEG images
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-jpeg-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : libjpeg-turbo-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-jpeg package.
Group: Libraries

%description lib
lib components for the R-jpeg package.


%prep
%setup -q -n jpeg
cd %{_builddir}/jpeg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669828923

%install
export SOURCE_DATE_EPOCH=1669828923
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
/usr/lib64/R/library/jpeg/DESCRIPTION
/usr/lib64/R/library/jpeg/INDEX
/usr/lib64/R/library/jpeg/Meta/Rd.rds
/usr/lib64/R/library/jpeg/Meta/features.rds
/usr/lib64/R/library/jpeg/Meta/hsearch.rds
/usr/lib64/R/library/jpeg/Meta/links.rds
/usr/lib64/R/library/jpeg/Meta/nsInfo.rds
/usr/lib64/R/library/jpeg/Meta/package.rds
/usr/lib64/R/library/jpeg/NAMESPACE
/usr/lib64/R/library/jpeg/NEWS
/usr/lib64/R/library/jpeg/R/jpeg
/usr/lib64/R/library/jpeg/R/jpeg.rdb
/usr/lib64/R/library/jpeg/R/jpeg.rdx
/usr/lib64/R/library/jpeg/help/AnIndex
/usr/lib64/R/library/jpeg/help/aliases.rds
/usr/lib64/R/library/jpeg/help/jpeg.rdb
/usr/lib64/R/library/jpeg/help/jpeg.rdx
/usr/lib64/R/library/jpeg/help/paths.rds
/usr/lib64/R/library/jpeg/html/00Index.html
/usr/lib64/R/library/jpeg/html/R.css
/usr/lib64/R/library/jpeg/img/Rlogo.jpg
/usr/lib64/R/library/jpeg/tests/jpeg.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jpeg/libs/jpeg.so
/usr/lib64/R/library/jpeg/libs/jpeg.so.avx2
/usr/lib64/R/library/jpeg/libs/jpeg.so.avx512
