%define _disable_ld_no_undefined 1

Summary:	A computational backend of FEniCS and implementation of the FEniCS Problem Solving Environment
Name:		dolfin
Version:	2017.1.0
Release:	1
License:	LGPLv3+
Group:		Sciences/Mathematics
URL:		https://fenicsproject.org
Source0:	https://bitbucket.org/fenics-project/dolfin/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-2017.1.0-unicode.patch

BuildRequires:	cmake
BuildRequires:	gcc-gfortran
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	hdf5-devel
BuildRequires:	suitesparse-devel
BuildRequires:	#libscotch-dev
BuildRequires:	vtk-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	mpi-devel
BuildRequires:	#petsc-dev
BuildRequires:	#slepc-dev
BuildRequires:	#python-petsc4py
BuildRequires:	#python-slepc4py
BuildRequires:	pkgconfig(python)
BuildRequires:	python-ffc
BuildRequires:	python-dijitso
BuildRequires:	python3egg(numpy)
BuildRequires:	python3egg(ply)
BuildRequires:	swig

%description
DOLFIN is the computational backend of FEniCS and implements the FEniCS
Problem Solving Environment in Python and C++.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc doc/epstool.htm doc/gsview.css
%doc COPYING.LESSER
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .unicode

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo	\
	-DBUILD_SHARED_LIBS:BOOL=ON			\
	-DCMAKE_SKIP_RPATH:BOOL=ON			\
	-DDOLFIN_ENABLE_TRILINOS:BOOL=OFF		\
	-DDOLFIN_ENABLE_GTEST:BOOL=OFF			\
	-DDOLFIN_ENABLE_VTK:BOOL=OFF			\
	%{nil}
%make

%install
%makeinstall_std

