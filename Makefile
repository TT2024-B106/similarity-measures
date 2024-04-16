CC = g++
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so libmanhattan.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.cpp

clean:
	rm -f ./*.so
	rm -f ./*.out
