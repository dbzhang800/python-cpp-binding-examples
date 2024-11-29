find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

add_library(lib2_pythonapi MODULE lib2_pythonapi.cpp)
target_link_libraries(lib2_pythonapi PRIVATE lib2 Python3::Python)

if (WIN32)
    set_target_properties(lib2_pythonapi PROPERTIES SUFFIX ".pyd") # Windows generate .pyd
endif()

set_target_properties(lib2_pythonapi PROPERTIES
    PREFIX ""  # Remove prefix
)
