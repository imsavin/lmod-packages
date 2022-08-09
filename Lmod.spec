Name:           Lmod
Version:        8.7.11 
Release:        1%{?dist}
Summary:        Lmod: An Environment Module System based on Lua, Reads TCL Modules, Supports a Software Hierarchy

License:        MIT
URL:            https://github.com/TACC/Lmod
Source0:       %{version}.tar.gz 

BuildRequires: lua-devel tcl-devel 
Requires:      lua lua-bitop lua-devel lua-json lua-lpeg lua-posix lua-term tcl tcl-devel

%description
Lmod is a Lua based module system that easily handles the MODULEPATH Hierarchical problem. Environment Modules provide a convenient way to dynamically change the users’ environment through modulefiles. This includes easily adding or removing directories to the PATH environment variable. Modulefiles for Library packages provide environment variables that specify where the library and header files can be found.

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1


%build
cd %{name}-%{version}

%configure

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%make_install

%files
%{_prefix}/lmod/8.7.11/init/R
%{_prefix}/lmod/8.7.11/init/bash
%{_prefix}/lmod/8.7.11/init/cmake
%{_prefix}/lmod/8.7.11/init/csh
%{_prefix}/lmod/8.7.11/init/cshrc
%{_prefix}/lmod/8.7.11/init/env_modules_python.py
%{_prefix}/lmod/8.7.11/init/env_modules_python.pyc
%{_prefix}/lmod/8.7.11/init/env_modules_python.pyo
%{_prefix}/lmod/8.7.11/init/env_modules_ruby.rb
%{_prefix}/lmod/8.7.11/init/fish
%{_prefix}/lmod/8.7.11/init/fish_tab_completion/module.fish
%{_prefix}/lmod/8.7.11/init/ksh
%{_prefix}/lmod/8.7.11/init/ksh_funcs/clearLmod
%{_prefix}/lmod/8.7.11/init/ksh_funcs/clearMT
%{_prefix}/lmod/8.7.11/init/ksh_funcs/ml
%{_prefix}/lmod/8.7.11/init/ksh_funcs/module
%{_prefix}/lmod/8.7.11/init/ksh_funcs/settarg
%{_prefix}/lmod/8.7.11/init/lisp
%{_prefix}/lmod/8.7.11/init/lmod_bash_completions
%{_prefix}/lmod/8.7.11/init/lmodrc.lua
%{_prefix}/lmod/8.7.11/init/perl
%{_prefix}/lmod/8.7.11/init/profile
%{_prefix}/lmod/8.7.11/init/profile.fish
%{_prefix}/lmod/8.7.11/init/profile.rc
%{_prefix}/lmod/8.7.11/init/rc
%{_prefix}/lmod/8.7.11/init/sh
%{_prefix}/lmod/8.7.11/init/tcsh
%{_prefix}/lmod/8.7.11/init/zsh
%{_prefix}/lmod/8.7.11/lib/lfs.so
%{_prefix}/lmod/8.7.11/lib/lfs.so.1
%{_prefix}/lmod/8.7.11/lib/lfs.so.1.0.1
%{_prefix}/lmod/8.7.11/lib/tcl2lua.so
%{_prefix}/lmod/8.7.11/lib/tcl2lua.so.1
%{_prefix}/lmod/8.7.11/lib/tcl2lua.so.1.0.1
%{_prefix}/lmod/8.7.11/libexec/CTimer.lua
%{_prefix}/lmod/8.7.11/libexec/Cache.lua
%{_prefix}/lmod/8.7.11/libexec/Configuration.lua
%{_prefix}/lmod/8.7.11/libexec/DirTree.lua
%{_prefix}/lmod/8.7.11/libexec/Exec.lua
%{_prefix}/lmod/8.7.11/libexec/FrameStk.lua
%{_prefix}/lmod/8.7.11/libexec/Hook.lua
%{_prefix}/lmod/8.7.11/libexec/HookArray.lua
%{_prefix}/lmod/8.7.11/libexec/LocationT.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Access.lua
%{_prefix}/lmod/8.7.11/libexec/MC_CheckSyntax.lua
%{_prefix}/lmod/8.7.11/libexec/MC_ComputeHash.lua
%{_prefix}/lmod/8.7.11/libexec/MC_DependencyCk.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Load.lua
%{_prefix}/lmod/8.7.11/libexec/MC_MgrLoad.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Refresh.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Show.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Spider.lua
%{_prefix}/lmod/8.7.11/libexec/MC_Unload.lua
%{_prefix}/lmod/8.7.11/libexec/MN_Between.lua
%{_prefix}/lmod/8.7.11/libexec/MN_Exact.lua
%{_prefix}/lmod/8.7.11/libexec/MN_Latest.lua
%{_prefix}/lmod/8.7.11/libexec/MN_Match.lua
%{_prefix}/lmod/8.7.11/libexec/MName.lua
%{_prefix}/lmod/8.7.11/libexec/MRC.lua
%{_prefix}/lmod/8.7.11/libexec/MT.lua
%{_prefix}/lmod/8.7.11/libexec/Master.lua
%{_prefix}/lmod/8.7.11/libexec/MasterControl.lua
%{_prefix}/lmod/8.7.11/libexec/ModuleA.lua
%{_prefix}/lmod/8.7.11/libexec/Options.lua
%{_prefix}/lmod/8.7.11/libexec/Pkg.lua
%{_prefix}/lmod/8.7.11/libexec/PkgBase.lua
%{_prefix}/lmod/8.7.11/libexec/PkgTACC.lua
%{_prefix}/lmod/8.7.11/libexec/RC2lua.tcl
%{_prefix}/lmod/8.7.11/libexec/ReadLmodRC.lua
%{_prefix}/lmod/8.7.11/libexec/SitePackage.lua
%{_prefix}/lmod/8.7.11/libexec/Spider.lua
%{_prefix}/lmod/8.7.11/libexec/StandardPackage.lua
%{_prefix}/lmod/8.7.11/libexec/Timer.lua
%{_prefix}/lmod/8.7.11/libexec/Var.lua
%{_prefix}/lmod/8.7.11/libexec/Version.lua
%{_prefix}/lmod/8.7.11/libexec/addto
%{_prefix}/lmod/8.7.11/libexec/check_module_tree_syntax
%{_prefix}/lmod/8.7.11/libexec/clearLMOD_cmd
%{_prefix}/lmod/8.7.11/libexec/cmdfuncs.lua
%{_prefix}/lmod/8.7.11/libexec/collectionFileA.lua
%{_prefix}/lmod/8.7.11/libexec/colorize.lua
%{_prefix}/lmod/8.7.11/libexec/computeHashSum
%{_prefix}/lmod/8.7.11/libexec/convertSh2MF.lua
%{_prefix}/lmod/8.7.11/libexec/lmod
%{_prefix}/lmod/8.7.11/libexec/loadModuleFile.lua
%{_prefix}/lmod/8.7.11/libexec/ml_cmd
%{_prefix}/lmod/8.7.11/libexec/modfuncs.lua
%{_prefix}/lmod/8.7.11/libexec/mrc_funcs.lua
%{_prefix}/lmod/8.7.11/libexec/mrc_load.lua
%{_prefix}/lmod/8.7.11/libexec/mrc_sandbox.lua
%{_prefix}/lmod/8.7.11/libexec/myGlobals.lua
%{_prefix}/lmod/8.7.11/libexec/pager.lua
%{_prefix}/lmod/8.7.11/libexec/parseVersion.lua
%{_prefix}/lmod/8.7.11/libexec/printEnvT.lua
%{_prefix}/lmod/8.7.11/libexec/print_os.sh
%{_prefix}/lmod/8.7.11/libexec/sandbox.lua
%{_prefix}/lmod/8.7.11/libexec/sh_to_modulefile
%{_prefix}/lmod/8.7.11/libexec/spider
%{_prefix}/lmod/8.7.11/libexec/spiderCacheSupport
%{_prefix}/lmod/8.7.11/libexec/tcl2lua.tcl
%{_prefix}/lmod/8.7.11/libexec/update_lmod_system_cache_files
%{_prefix}/lmod/8.7.11/libexec/utils.lua
%{_prefix}/lmod/8.7.11/messageDir/de.lua
%{_prefix}/lmod/8.7.11/messageDir/en.lua
%{_prefix}/lmod/8.7.11/messageDir/es.lua
%{_prefix}/lmod/8.7.11/messageDir/fr.lua
%{_prefix}/lmod/8.7.11/messageDir/template.lua
%{_prefix}/lmod/8.7.11/messageDir/zh.lua
%{_prefix}/lmod/8.7.11/modulefiles/Core/lmod.lua
%{_prefix}/lmod/8.7.11/modulefiles/Core/settarg.lua
%{_prefix}/lmod/8.7.11/settarg/Bare.lua
%{_prefix}/lmod/8.7.11/settarg/BaseShell.lua
%{_prefix}/lmod/8.7.11/settarg/Bash.lua
%{_prefix}/lmod/8.7.11/settarg/BuildTarget.lua
%{_prefix}/lmod/8.7.11/settarg/CmdLineOptions.lua
%{_prefix}/lmod/8.7.11/settarg/Csh.lua
%{_prefix}/lmod/8.7.11/settarg/ModifyPath.lua
%{_prefix}/lmod/8.7.11/settarg/Output.lua
%{_prefix}/lmod/8.7.11/settarg/ProcessModuleTable.lua
%{_prefix}/lmod/8.7.11/settarg/STT.lua
%{_prefix}/lmod/8.7.11/settarg/TargValue.lua
%{_prefix}/lmod/8.7.11/settarg/Version.lua
%{_prefix}/lmod/8.7.11/settarg/getUname.lua
%{_prefix}/lmod/8.7.11/settarg/settarg_cmd
%{_prefix}/lmod/8.7.11/settarg/settarg_rc.lua
%{_prefix}/lmod/8.7.11/settarg/targ
%{_prefix}/lmod/8.7.11/settarg/utils.lua
%{_prefix}/lmod/8.7.11/share/man/cat1/module.1
%{_prefix}/lmod/8.7.11/shells/Bare.lua
%{_prefix}/lmod/8.7.11/shells/BaseShell.lua
%{_prefix}/lmod/8.7.11/shells/Bash.lua
%{_prefix}/lmod/8.7.11/shells/CMake.lua
%{_prefix}/lmod/8.7.11/shells/Csh.lua
%{_prefix}/lmod/8.7.11/shells/Fish.lua
%{_prefix}/lmod/8.7.11/shells/Lisp.lua
%{_prefix}/lmod/8.7.11/shells/Perl.lua
%{_prefix}/lmod/8.7.11/shells/Python.lua
%{_prefix}/lmod/8.7.11/shells/R.lua
%{_prefix}/lmod/8.7.11/shells/Rc.lua
%{_prefix}/lmod/8.7.11/shells/Ruby.lua
%{_prefix}/lmod/8.7.11/tools/Banner.lua
%{_prefix}/lmod/8.7.11/tools/BeautifulTbl.lua
%{_prefix}/lmod/8.7.11/tools/ColumnTable.lua
%{_prefix}/lmod/8.7.11/tools/Cosmic.lua
%{_prefix}/lmod/8.7.11/tools/Dbg.lua
%{_prefix}/lmod/8.7.11/tools/MF_Base.lua
%{_prefix}/lmod/8.7.11/tools/MF_Lua.lua
%{_prefix}/lmod/8.7.11/tools/MF_TCL.lua
%{_prefix}/lmod/8.7.11/tools/Optiks.lua
%{_prefix}/lmod/8.7.11/tools/Optiks_Option.lua
%{_prefix}/lmod/8.7.11/tools/TermWidth.lua
%{_prefix}/lmod/8.7.11/tools/base64.lua
%{_prefix}/lmod/8.7.11/tools/capture.lua
%{_prefix}/lmod/8.7.11/tools/declare.lua
%{_prefix}/lmod/8.7.11/tools/deepcopy.lua
%{_prefix}/lmod/8.7.11/tools/fileOps.lua
%{_prefix}/lmod/8.7.11/tools/haveTermSupport.lua
%{_prefix}/lmod/8.7.11/tools/i18n/init.lua
%{_prefix}/lmod/8.7.11/tools/i18n/interpolate.lua
%{_prefix}/lmod/8.7.11/tools/i18n/plural.lua
%{_prefix}/lmod/8.7.11/tools/i18n/variants.lua
%{_prefix}/lmod/8.7.11/tools/i18n/version.lua
%{_prefix}/lmod/8.7.11/tools/inherits.lua
%{_prefix}/lmod/8.7.11/tools/json.lua
%{_prefix}/lmod/8.7.11/tools/lmod_system_execute.lua
%{_prefix}/lmod/8.7.11/tools/pairsByKeys.lua
%{_prefix}/lmod/8.7.11/tools/replaceStr.lua
%{_prefix}/lmod/8.7.11/tools/serializeTbl.lua
%{_prefix}/lmod/8.7.11/tools/strict.lua
%{_prefix}/lmod/8.7.11/tools/string_utils.lua
%{_prefix}/lmod/lmod


%doc


%changelog
