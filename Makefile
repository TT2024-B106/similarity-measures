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

test-frechet: librdp.so 
	mkdir -p build
	mv librdp.so build/
	g++ tests/libdrp.cpp $(BFLAGS) -ldrp  $(SFLAGS) -o $@.out

	./$@.out -d

	rm $@.out build/*.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.cpp

libeditdist.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/edit_distance.cpp

librdp.so:
	$(CC) $(CFLAGS) -std=c++20 $(LDFLAGS) -o $@ src/RDP.cpp src/Algoritmo.cpp
	
clean:
	rm -f ./*.so
	rm -f ./*.out
