CC = g++
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.cpp

clean:
	rm -f ./*.so
