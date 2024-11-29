
add_custom_target(lib2_sip ALL
    COMMAND sip-build --verbose
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS lib2
    COMMENT "Building lib2's python bindings using SIP"
)
