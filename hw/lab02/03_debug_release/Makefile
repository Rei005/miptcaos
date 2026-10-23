MODE ?= release

TARGET = calculator
GCC = g++
CXXFLAGS = -std=c++17 -MMD -MP

OBJDIR = obj/$(MODE)

ifeq ($(MODE),debug)
    CXXFLAGS += -g -O0
else ifeq ($(MODE),release)
    CXXFLAGS += -O3
else
	$(error Unknown MODE='$(MODE)'. Use MODE=debug or MODE=release)
endif

SRC = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp,$(OBJDIR)/%.o,$(SRC))

all: $(TARGET)

$(TARGET) : $(OBJS)
	$(GCC) $(OBJS) -o $(TARGET)

$(OBJDIR)/%.o : %.cpp | $(OBJDIR)
	$(GCC) $(CXXFLAGS) -c $< -o $@

$(OBJDIR) :
	mkdir -p $(OBJDIR)

-include $(OBJS:.o=.d)

clean :
	rm -rf $(TARGET) obj 

.PHONY : all clean