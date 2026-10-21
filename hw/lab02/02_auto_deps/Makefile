TARGET = calculator
GCC = g++
CXXFLAGS = -std=c++17 -MMD -MP

OBJDIR = obj

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
	rm -rf $(TARGET) $(OBJDIR)

.PHONY : all clean