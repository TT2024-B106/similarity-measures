CC = g++

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

BFLAGS = -L./build
SFLAGS = -Wl,-rpath,./build

all: libeuclidean.so libmanhattan.so libeditdist.so

test-edr: libeditdist.so libmanhattan.so
	mkdir -p build
	mv libeditdist.so build/
	mv libmanhattan.so build/ 
	$(CC) tests/test_edr.cpp $(BFLAGS) -leditdist -lmanhattan $(SFLAGS) -o $@.out

	./$@.out -d

	rm $@.out build/*.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.cpp

libeditdist.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/edit_distance.cpp

clean:
	rm -f ./*.so
	rm -f ./*.out
