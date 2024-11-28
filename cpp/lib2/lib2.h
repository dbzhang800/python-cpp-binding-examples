#pragma once

#ifdef _WIN32
    #ifdef BUILD_LIB2_DLL
        #define LIB2_DLL_EXPORT __declspec(dllexport)
    #else
        #define LIB2_DLL_EXPORT __declspec(dllimport)
    #endif
#else
    #define LIB2_DLL_EXPORT
#endif

LIB2_DLL_EXPORT int add(int a, int b);
