set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Python3 interpreter and development components
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Debug: Print Python3 executable path
message("Python3_EXECUTABLE: ${Python3_EXECUTABLE}")

# Attempt to retrieve the Shiboken6 installation path dynamically
execute_process(
    COMMAND python -c "import shiboken6; print(shiboken6.__path__[0])"
    OUTPUT_VARIABLE SHIBOKEN6_PATH
    ERROR_VARIABLE SHIBOKEN6_ERROR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Debug: Print the result of execute_process
message("SHIBOKEN6_PATH: ${SHIBOKEN6_PATH}")
message("SHIBOKEN6_ERROR: ${SHIBOKEN6_ERROR}")

# Set paths for Shiboken6 tool, headers, and library
set(shiboken_include_dir ${SHIBOKEN6_PATH}/../shiboken6_generator/include)
message("shiboken include path: " ${shiboken_include_dir})

# Configure platform-specific library settings
if(WIN32)
    set(shiboken_library ${SHIBOKEN6_PATH}/shiboken6.abi3.lib)
    set(module_suffix ".pyd")
elseif(APPLE)
    set(shiboken_library ${SHIBOKEN6_PATH}/libshiboken6.abi3.dylib)
    set(module_suffix ".so")
else()
    set(shiboken_library ${SHIBOKEN6_PATH}/libshiboken6.abi3.so)
    set(module_suffix ".so")
endif()

# Specify the C++ header and typesystem file for the binding
set(wrapped_header ${CMAKE_CURRENT_SOURCE_DIR}/../../cpp/lib2/lib2.h)
set(typesystem_file ${CMAKE_CURRENT_SOURCE_DIR}/lib2_shiboken.xml)

# Use Shiboken6 to generate the binding source code
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/lib2_shiboken/lib2_shiboken_module_wrapper.cpp
    COMMAND shiboken6
    --output-directory=${CMAKE_CURRENT_BINARY_DIR}
    --include-paths=${CMAKE_CURRENT_SOURCE_DIR}/../../cpp/lib2
    --typesystem-paths=${shiboken_include_dir}
    ${wrapped_header}
    ${typesystem_file}
    DEPENDS lib2 ${wrapped_header} ${typesystem_file}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Create the Python module
add_library(lib2_shiboken MODULE
    ${CMAKE_CURRENT_BINARY_DIR}/lib2_shiboken/lib2_shiboken_module_wrapper.cpp
)

# Link the Shiboken6 runtime library and include the headers
target_include_directories(lib2_shiboken PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../../cpp/lib2 ${shiboken_include_dir})
target_link_libraries(lib2_shiboken PRIVATE
    lib2
    ${shiboken_library}
    Python3::Python
)

# Set the module properties
set_target_properties(lib2_shiboken PROPERTIES
    PREFIX "" # Remove default 'lib' prefix
    SUFFIX ${module_suffix} # Use platform-specific suffix
)
