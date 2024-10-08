CC = g++

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

BFLAGS = -L./build
SFLAGS = -Wl,-rpath,./build

all: libeuclidean.so libmanhattan.so

test-edr: libeditdist.so libmanhattan.so
	mkdir -p build
	mv libeditdist.so build/
	mv libmanhattan.so build/ 
	g++ tests/test_edr.cpp $(BFLAGS) -leditdist -lmanhattan $(SFLAGS) -o $@.out

	./$@.out -d

test-dtw: libdtw.so
	mkdir -p build
	mv libdtw.so build/
	$(CC) tests/test_dtw.cpp $(BFLAGS) -ldtw $(RPATH) -o $@.out

	./$@.out -d


ctypes:
	$(CC) $(CFLAGS) $(LDFLAGS) -o libeuclidean.so src/euclidean.cpp

cppyy: libeuclidean.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.cpp

libeditdist.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/edit_distance.cpp

libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/DTW.cpp src/Algoritmo.cpp
	
clean:
	rm -f ./*.so
	rm -f ./*.out
