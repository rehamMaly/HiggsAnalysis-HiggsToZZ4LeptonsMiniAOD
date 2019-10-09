#include <vector>
#include <iostream>

/* ArrayMDVector.h
 * Author: Christopher Brainerd - University of California, Davis
 * ArrayMDVector<T,d> creates a d-dimensional vector of T (i.e. ArrayVector<int,3> is basically std::vector<std::vector<std::vector<int> > >)
 * cast_to_vector takes in an ArrayMDVector<T,d>* and casts it to the equivalent std::vector<...>* for functions that need to be passed a std::vector pointer
 * Unlike a std::vector, ArrayMDVector can be assigned to as though it were an C-style array
 * Adds default-constructed elements if assigned past the end. (i.e. ArrayVector<int,1> foo; foo[3]=1; will give the same result as ArrayVector<int,1> foo {0,0,0,1};) Also warns in this case.
 * Usage: 
 *   Variable declaration: ArrayVectorMD<int,1> foo;
 *   Branch declaration: tree->Branch("foo",cast_to_vector(&foo));
 *   Adding elements: for(int i=0;i<bar;++i) foo[i]=i;
 */

template <class T,int d>
class ArrayMDVector : public std::vector<typename ArrayMDVector<T,d-1>::type> {
    public:
        typedef std::vector<typename ArrayMDVector<T,d-1>::vector_type> vector_type;
        typedef typename ArrayMDVector<T,d-1>::type content_type;
        typedef ArrayMDVector<T,d> type;
        typename ArrayMDVector<T,d>::reference operator[](std::size_t pos);
        content_type default_val() { return default_value((ArrayMDVector<T,d>*)nullptr); }
};

template<class T>
class ArrayMDVector<T,0> {
    public:
        typedef T vector_type;
        typedef T type;
};

//When operator[] is called out of bounds, construct defaults up to that point
//For a vector type, this is just the default constructor for the vector
//For a floating point type, this is -999 for backwards compatibility
//For a bool, this is false for backwards compatibility

template <class T,int d>
inline typename ArrayMDVector<T,d>::content_type default_value(ArrayMDVector<T,d>*) { return typename ArrayMDVector<T,d>::content_type(); }

template <class T>
inline T default_value(ArrayMDVector<T,1>*) { return T(-999); }

template <>
inline bool default_value(ArrayMDVector<bool,1>*) { return false; }

template <class T,int d>
typename ArrayMDVector<T,d>::vector_type* cast_to_vector(ArrayMDVector<T,d>* arrayVector) {
    return (typename ArrayMDVector<T,d>::vector_type*) arrayVector;
}

template <class T, int d>
typename ArrayMDVector<T,d>::reference ArrayMDVector<T,d>::operator[](std::size_t pos) {
    std::size_t current_length=this->size();
    if(pos==current_length) {
        this->push_back(ArrayMDVector<T,d>::default_val());
    }
    else if(pos>current_length) {
        std::cout << "Warning: assigned past end of ArrayMDVector. Previous length: " << current_length << " Position: " << pos << ". This is probably a bug.\n";
        for(std::size_t i=0;i<=pos-current_length;++i) {
            this->push_back(ArrayMDVector<T,d>::default_val());
        }
    }
    return std::vector<typename ArrayMDVector<T,d>::content_type>::operator[](pos);
}
