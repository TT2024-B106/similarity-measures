CC = g++

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
RPATH = -Wl,-rpath,'$$ORIGIN'

BFLAGS = -L./build

all: libeuclidean.so libmanhattan.so libdtw.so



test-dtw: libdtw.so
	mkdir -p build
	mv libdtw.so build/
	$(CC) tests/test_dtw.cpp $(BFLAGS) -ldtw $(RPATH) -o $@.out

	LD_LIBRARY_PATH=./build ./$@.out -d

	#rm $@.out build/*.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/manhattan.cpp

libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/DTW.cpp src/Algoritmo.cpp

clean:
	rm -f ./*.so
	rm -f ./*.out
	rm -rf build

