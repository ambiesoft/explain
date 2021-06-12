#!/usr/bin/env python3
from _ast import arg

def printcmd(arg, explanation):
    print('{}: {}'.format(arg,explanation))
    
    
        
def expose_clang_cl(commands):
    print('clang-cl')
    
    i=0
    count = len(commands)
    while i < count:
      arg = commands[i]
      if False:
        pass
      elif arg in ['/nologo']:
        printcmd(arg, '''
  no logo
        ''')
        
      i += 1  

            
        
            
        
def printLine():
    print('-' * 70)
    
if __name__ == '__main__':
    expose_clang_cl(
r'''/nologo /showIncludes  "-imsvcC:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC    ools\MSVC\14.14.26428\ATLMFC\include" "-imsvcC:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC    ools\MSVC\14.14.26428\include" "-imsvcC:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\include\um" "-imsvcC:\Program Files (x86)\Windows Kits\10\include\10.0.17134.0\ucrt" "-imsvcC:\Program Files (x86)\Windows Kits\10\include\10.0.17134.0\shared" "-imsvcC:\Program Files (x86)\Windows Kits\10\include\10.0.17134.0\um" "-imsvcC:\Program Files (x86)\Windows Kits\10\include\10.0.17134.0\winrt" "-imsvcC:\Program Files (x86)\Windows Kits\10\include\10.0.17134.0\cppwinrt" -DV8_DEPRECATION_WARNINGS -DUSE_AURA=1 -DNO_TCMALLOC -DFULL_SAFE_BROWSING -DSAFE_BROWSING_CSD -DSAFE_BROWSING_DB_LOCAL -DCHROMIUM_BUILD -DFIELDTRIAL_TESTING_ENABLED "-DCR_CLANG_REVISION=\"336424-1\"" -D_HAS_NODISCARD -D_HAS_EXCEPTIONS=0 -DCOMPONENT_BUILD -D__STD_C -D_CRT_RAND_S -D_CRT_SECURE_NO_DEPRECATE -D_SCL_SECURE_NO_DEPRECATE -D_ATL_NO_OPENGL -D_WINDOWS -DCERT_CHAIN_PARA_HAS_EXTRA_FIELDS -DPSAPI_VERSION=1 -DWIN32 -D_SECURE_ATL -D_USING_V110_SDK71_ -DWINAPI_FAMILY=WINAPI_FAMILY_DESKTOP_APP -DWIN32_LEAN_AND_MEAN -DNOMINMAX -D_UNICODE -DUNICODE -DNTDDI_VERSION=0x0A000002 -D_WIN32_WINNT=0x0A00 -DWINVER=0x0A00 -DNDEBUG -DNVALGRIND -DDYNAMIC_ANNOTATIONS_ENABLED=0 -DUSING_V8_SHARED -DBLINK_CORE_IMPLEMENTATION=1 -DWEBP_EXTERN=extern -DUSE_EGL -DBLINK_IMPLEMENTATION=1 -DINSIDE_BLINK -DU_USING_ICU_NAMESPACE=0 -DU_ENABLE_DYLOAD=0 -DICU_UTIL_DATA_IMPL=ICU_UTIL_DATA_FILE -DUCHAR_TYPE=wchar_t -DGOOGLE_PROTOBUF_NO_RTTI -DGOOGLE_PROTOBUF_NO_STATIC_INITIALIZER -DPROTOBUF_USE_DLLS -DBORINGSSL_SHARED_LIBRARY -DSK_IGNORE_LINEONLY_AA_CONVEX_PATH_OPTS -DSK_HAS_PNG_LIBRARY -DSK_HAS_WEBP_LIBRARY -DSK_HAS_JPEG_LIBRARY -DSKIA_DLL -DGR_GL_IGNORE_ES3_MSAA=0 -DSKCMS_API=__declspec(dllexport) -DSK_SUPPORT_GPU=1 "-DSK_GPU_WORKAROUNDS_HEADER=\"gpu/config/gpu_driver_bug_workaround_autogen.h\"" -DGR_GL_FUNCTION_TYPE=__stdcall -D__STD_C -D_CRT_SECURE_NO_DEPRECATE -D_SCL_SECURE_NO_DEPRECATE -DWTF_USE_WEBAUDIO_FFMPEG=1 -DWTF_USE_DEFAULT_RENDER_THEME=1 -DUSE_LIBJPEG_TURBO=1 -DUSING_V8_SHARED -DWEBRTC_NON_STATIC_TRACE_EVENT_HANDLERS=0 -DGTEST_RELATIVE_PATH -DWEBRTC_CHROMIUM_BUILD -DWEBRTC_WIN -DABSL_ALLOCATOR_NOTHROW=1 -DNO_MAIN_THREAD_WRAPPING -DPNG_USE_DLL -DPNG_NO_MODULEDEF -DUSING_V8_SHARED -DLIBXSLT_STATIC -I. -I../.. -Igen -I../../third_party/libwebp/src -I../../third_party/wtl/include -I../../third_party/khronos -I../../gpu -I../../third_party/libyuv/include -I../../third_party/ced/src -I../../third_party/icu/source/common -I../../third_party/icu/source/i18n -I../../third_party/protobuf/src -I../../third_party/protobuf/src -Igen/protoc_out -I../../third_party/boringssl/src/include -I../../skia/config -I../../skia/ext -I../../third_party/skia/include/c -I../../third_party/skia/include/config -I../../third_party/skia/include/core -I../../third_party/skia/include/effects -I../../third_party/skia/include/encode -I../../third_party/skia/include/gpu -I../../third_party/skia/include/images -I../../third_party/skia/include/lazy -I../../third_party/skia/include/pathops -I../../third_party/skia/include/pdf -I../../third_party/skia/include/pipe -I../../third_party/skia/include/ports -I../../third_party/skia/include/utils -I../../third_party/skia/src/gpu -I../../third_party/skia/src/sksl -I../../third_party/angle/include -I../../third_party/angle/src/common/third_party/base -Igen/angle -I../../third_party/blink/renderer/platform/wtf/os-win32 -I../../third_party/libjpeg_turbo -I../../v8/include -Igen/v8/include -I../../third_party/webrtc_overrides -I../../third_party/webrtc -I../../third_party/iccjpeg -I../../third_party/libpng -I../../third_party/zlib -I../../third_party/ots/include -I../../v8/include -Igen/v8/include -I../../third_party/libxml/src/include -I../../third_party/libxml/win32/include -I../../third_party/libxslt/src -I../../third_party/snappy/src -I../../third_party/snappy/win32 /utf-8 /X -Wno-builtin-macro-redefined -D__DATE__= -D__TIME__= -D__TIMESTAMP__= -fcolor-diagnostics -fmerge-all-constants -Xclang -mllvm -Xclang -instcombine-lower-dbg-declare=0 -no-canonical-prefixes -fcomplete-member-pointers /Gy /FS /bigobj /d2FastFail /Zc:sizedDealloc- -fmsc-version=1911 -m32 /Brepro /W4 -Wimplicit-fallthrough -Wthread-safety /WX /wd4091 /wd4127 /wd4251 /wd4275 /wd4312 /wd4324 /wd4351 /wd4355 /wd4503 /wd4589 /wd4611 /wd4100 /wd4121 /wd4244 /wd4505 /wd4510 /wd4512 /wd4610 /wd4838 /wd4995 /wd4996 /wd4456 /wd4457 /wd4458 /wd4459 /wd4200 /wd4201 /wd4204 /wd4221 /wd4018 /wd4245 /wd4267 /wd4305 /wd4389 /wd4702 /wd4701 /wd4703 /wd4661 /wd4706 /wd4715 /wd4267 /wd4702 -Wno-missing-field-initializers -Wno-unused-parameter -Wno-c++11-narrowing -Wno-covered-switch-default -Wno-unneeded-internal-declaration -Wno-undefined-var-template -Wno-address-of-packed-member -Wno-nonportable-include-path -Wno-user-defined-warnings -Wno-unused-lambda-capture -Wno-null-pointer-arithmetic -Wno-enum-compare-switch -Wno-ignored-pragma-optimize /O1 /Ob2 /Oy- /Zc:inline /Gw /Oi /MD -Xclang -add-plugin -Xclang find-bad-constructs -Xclang -plugin-arg-find-bad-constructs -Xclang enforce-in-thirdparty-webkit -Xclang -plugin-arg-find-bad-constructs -Xclang check-enum-max-value -Wheader-hygiene -Wstring-conversion -Wtautological-overlap-compare /wd4305 /wd4324 /wd4714 /wd4800 /wd4996 -Xclang -add-plugin -Xclang blink-gc-plugin -Wglobal-constructors /FI../../third_party/blink/renderer/core/precompile_core.h -Wno-inconsistent-missing-override /wd4344 /wd4706 /wd4291 -imsvc ../../third_party/abseil-cpp -DLIBXML_STATIC= /Fpobj/third_party/blink/renderer/bindings/core/v8/bindings_core_impl_cc.pch /Yu../../third_party/blink/renderer/core/precompile_core.h /TP /wd4577 /GR- /c gen/third_party/blink/renderer/bindings/core/v8/bindings_core_impl_jumbo_4.cc /Foobj/third_party/blink/renderer/bindings/core/v8/bindings_core_impl/bindings_core_impl_jumbo_4.obj /Fd"obj/third_party/blink/renderer/bindings/core/v8/bindings_core_impl_cc.pdb"
'''.split())
    printLine()
