#define BOOST_PYTHON_STATIC_LIB
#define BOOST_NUMPY_STATIC_LIB
#include <boost/python/numpy.hpp>

namespace py = boost::python;
namespace np = boost::python::numpy;

void hcpe_decode_with_result(np::ndarray ndhcpe, np::ndarray ndfeatures1, np::ndarray ndfeatures2, np::ndarray ndresult);
void hcpe_decode_with_move(np::ndarray ndhcpe, np::ndarray ndfeatures1, np::ndarray ndfeatures2, np::ndarray ndmove);
void hcpe_decode_with_move_result(np::ndarray ndhcpe, np::ndarray ndfeatures1, np::ndarray ndfeatures2, np::ndarray ndmove, np::ndarray ndresult);
void hcpe_decode_with_value(np::ndarray ndhcpe, np::ndarray ndfeatures1, np::ndarray ndfeatures2, np::ndarray ndmove, np::ndarray ndresult, np::ndarray ndvalue);
