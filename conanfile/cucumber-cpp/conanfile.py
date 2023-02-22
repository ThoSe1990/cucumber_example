from conans import ConanFile, CMake, tools
import os
import functools


required_conan_version = ">=1.33.0"


class CucumberConan(ConanFile):
    name = "cucumber-cpp"
    url = "https://github.com/cucumber/cucumber-cpp.git"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    _source_subfolder = "source_subfolder"
    options = { "no_main":[True, False]}
    default_options = { "no_main": False}

    def requirements(self):
        self.requires("boost/1.80.0")
        self.requires("gtest/1.10.0")

    def source(self):
        self.run("git clone {} ./{}".format(self.url, self._source_subfolder))
        if self.version != "latest":
            self.run("git -C ./{} checkout v{}".format(self._source_subfolder, self.version))


    @functools.lru_cache(1)
    def _configure_cmake(self):
        cmake = CMake(self)
        if self.settings.os == "Windows" and self.settings.compiler == "gcc":
            cmake.generator="Unix Makefiles"
        if self.settings.build_type == "Debug":
            cmake.definitions['CMAKE_BUILD_TYPE'] = "Debug"
            if self.settings.compiler == "Visual Studio":
                cmake.definitions['CMAKE_CXX_FLAGS'] = "/MT /EHsc" 
                cmake.definitions['CMAKE_CXX_FLAGS_RELEASE'] = "/MT /EHsc" 
                cmake.definitions['CMAKE_CXX_FLAGS_DEBUG'] = "/MTd /EHsc"
                cmake.definitions['GTEST_LIBRARY'] = os.path.join(self.deps_cpp_info['gtest'].rootpath, 'lib', 'gtestd.lib')
                cmake.definitions['GTEST_MAIN_LIBRARY'] = os.path.join(self.deps_cpp_info['gtest'].rootpath, 'lib', 'gtest_maintd.lib')
                cmake.definitions['GMOCK_LIBRARY'] = os.path.join(self.deps_cpp_info['gtest'].rootpath, 'lib', 'gmockd.lib')
                cmake.definitions['GMOCK_MAIN_LIBRARY'] = os.path.join(self.deps_cpp_info['gtest'].rootpath, 'lib', 'gmock_maintd.lib')
        if self.settings.build_type == "Release":
            cmake.definitions['CMAKE_BUILD_TYPE'] = "Release"
            if self.settings.compiler == "Visual Studio":
                cmake.definitions['CMAKE_CXX_FLAGS'] = "/MTd /EHsc" 
                cmake.definitions['CMAKE_CXX_FLAGS_RELEASE'] = "/MT /EHsc" 
                cmake.definitions['CMAKE_CXX_FLAGS_DEBUG'] = "/MTd /EHsc"        
        cmake.definitions['BOOST_ROOT'] = self.deps_cpp_info['boost'].rootpath
        cmake.definitions['GTEST_ROOT'] = self.deps_cpp_info['gtest'].rootpath
        cmake.definitions['GMOCK_ROOT'] = self.deps_cpp_info['gtest'].rootpath
        print(self.deps_cpp_info['gtest'].rootpath)
        cmake.definitions['CMAKE_INSTALL_PREFIX'] = "{}/out".format(self._source_subfolder)
        cmake.definitions['Boost_USE_STATIC_RUNTIME'] = True
        cmake.definitions['BUILD_SHARED_LIBS'] = False
        cmake.definitions['CUKE_USE_STATIC_BOOST'] = True
        cmake.definitions['CUKE_USE_STATIC_GTEST'] = True
        cmake.definitions['CUKE_ENABLE_BOOST_TEST'] = False
        cmake.definitions['CUKE_DISABLE_BOOST_TEST'] = True
        cmake.definitions['CUKE_ENABLE_GTEST'] = False
        cmake.definitions['CUKE_ENABLE_QT'] = False
        cmake.definitions['CUKE_TESTS_E2E'] = False
        cmake.definitions['CUKE_TESTS_UNIT'] = False
        cmake.definitions['CUKE_TESTS_VALGRIND'] = False
        cmake.definitions['BUILD_SHARED_LIBS'] = False
        cmake.definitions['CUKE_DISABLE_GTEST'] = False
        cmake.definitions['CUKE_DISABLE_UNIT_TESTS'] = False
        cmake.definitions['CUKE_DISABLE_E2E_TESTS'] = False
        cmake.definitions['CUKE_ENABLE_EXAMPLES'] = True
        cmake.definitions['CUKE_DISABLE_QT'] = False
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        if self.options.no_main:
            cmake.build(target="cucumber-cpp-nomain")
        else:
            cmake.build(target="cucumber-cpp")
        

    def package(self):
        print(os.getcwd())
        self.copy(pattern="*", src="lib", dst="lib")
        self.copy(pattern="*", src=os.path.join(self._source_subfolder, "include"), dst="include")
        self.copy(pattern="*", src=os.path.join(self._source_subfolder, "src", "cucumber-cpp", "internal"), dst="include/cucumber-cpp/internal")

    def package_info(self):
        self.cpp_info.includedirs = ['include'] 
        self.cpp_info.libdirs = ['lib'] 
        self.cpp_info.libs = tools.collect_libs(self)