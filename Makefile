CXX=       	g++
CXXFLAGS= 	-g -gdwarf-2 -std=gnu++11 -Wall -fPIC
LDFLAGS=	-pthread

all:    test1 test1-nopic test2 test2-nopic test3 test3-nopic test4 test4-nopic test5 test5-nopic test6 test6-nopic test7 test7-nopic

%.o:	%.cpp uthread.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

%-nopic.o:	%.cpp uthread.h
	$(CXX) $(filter-out -fPIC,$(CXXFLAGS)) -c -o $@ $<

test1:	uthread.o test1.o
	$(CXX) $(LDFLAGS) -o $@ $^

test1-nopic: uthread-nopic.o test1-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test2:	uthread.o test2.o
	$(CXX) $(LDFLAGS) -o $@ $^

test2-nopic: uthread-nopic.o test2-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test3:	uthread.o test3.o
	$(CXX) $(LDFLAGS) -o $@ $^

test3-nopic: uthread-nopic.o test3-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test4:	uthread.o test4.o
	$(CXX) $(LDFLAGS) -o $@ $^

test4-nopic: uthread-nopic.o test4-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test5:	uthread.o test5.o
	$(CXX) $(LDFLAGS) -o $@ $^

test5-nopic: uthread-nopic.o test5-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test6:	uthread.o test6.o
	$(CXX) $(LDFLAGS) -o $@ $^

test6-nopic: uthread-nopic.o test6-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

test7:	uthread.o test7.o
	$(CXX) $(LDFLAGS) -o $@ $^

test7-nopic: uthread-nopic.o test7-nopic.o
	$(CXX) $(LDFLAGS) -o $@ $^

clean:
	$(RM) -f test1 test2 test3 test4 test5 test6 test7
	$(RM) -f test1-nopic test2-nopic test3-nopic test4-nopic test5-nopic test6-nopic test7-nopic
	$(RM) -f *.o

.PHONY: all clean

