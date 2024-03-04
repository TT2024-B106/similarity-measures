CC = g++
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: build build/libeuclidean.so

build:
	makedir -p build

build/libeuclidean.so: build/euclidean.o
	$(CC) $(LDFLAGS) -o $@ build/euclidean.o

build/euclidean.o: src/euclidean.cpp src/euclidean.h
	$(CC) $(CFLAGS) -c src/euclidean.cpp -o $@

clean:
	rm -f build/euclidean.o build/libeuclidean.so
