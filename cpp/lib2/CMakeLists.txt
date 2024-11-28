add_library(lib2 SHARED lib2.cpp)

if (WIN32)
    target_compile_definitions(lib2 PRIVATE BUILD_LIB2_DLL)
endif()

