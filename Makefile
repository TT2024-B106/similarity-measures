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

	rm $@.out build/*.so

test-dtw: libeditdist.so libmanhattan.so
	mkdir -p build
	mv libdtw.so build/
	g++ tests/test_dtw.cpp $(BFLAGS) -ldtw $(SFLAGS) -o $@.out

	./$@.out -d

	rm $@.out build/*.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.cpp

libdtw.so:
	$(CC) $(CFLAGS) -std=c++20 $(LDFLAGS) -o $@ src/DTW.cpp src/Algoritmo.cpp

clean:
	rm -f ./*.so
	rm -f ./*.out
