CC = g++

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
RPATH = -Wl,-rpath,'$$ORIGIN'

BFLAGS = -L./build

all: libeuclidean.so libmanhattan.so libeditdist.so libdtw.so

test-edr: libeditdist.so libmanhattan.so
	mkdir -p build
	mv libeditdist.so build/
	mv libmanhattan.so build/
	$(CC) tests/test_edr.cpp $(BFLAGS) -leditdist -lmanhattan $(RPATH) -o $@.out

	LD_LIBRARY_PATH=./build ./$@.out -d

	#rm $@.out build/*.so

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

libeditdist.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/edit_distance.cpp

libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) $(RPATH) -o $@ src/DTW.cpp src/Algoritmo.cpp

clean:
	rm -f ./*.so
	rm -f ./*.out
	rm -rf build

