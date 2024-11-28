add_library(lib1 SHARED lib1.cpp)

if (WIN32)
    target_compile_definitions(lib1 PRIVATE BUILD_LIB1_DLL)
endif()

