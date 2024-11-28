#pragma once

#ifdef _WIN32
    #ifdef BUILD_LIB1_DLL
        #define LIB1_DLL_EXPORT __declspec(dllexport)
    #else
        #define LIB1_DLL_EXPORT __declspec(dllimport)
    #endif
#else
    #define LIB1_DLL_EXPORT
#endif

extern "C" {
    LIB1_DLL_EXPORT int add(int a, int b);
}
