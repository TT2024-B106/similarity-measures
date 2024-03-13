CC = g++
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: build ctypes

build:
	makedir -p build

ctypes:
	$(CC) $(CFLAGS) $(LDFLAGS) -o build/libeuclidean.so src/euclidean.cpp

cppyy: build/libeuclidean.so

build/libeuclidean.so: build/euclidean.o
	$(CC) $(LDFLAGS) -o $@ build/euclidean.o

build/euclidean.o: src/euclidean.cpp src/euclidean.h
	$(CC) $(CFLAGS) -c src/euclidean.cpp -o $@

clean:
	rm -f build/*
