TARGET = calculator
GCC = g++
CXXFLAGS = -std=c++17

OBJDIR = obj

SRC = $(wildcard *.cpp)
OBJ = $(patsubst %.cpp, $(OBJDIR)/%.o, $(SRC))

all: $(TARGET)

$(TARGET) : $(OBJ)
	$(GCC) $(OBJ) -o $(TARGET)

$(OBJDIR)/%.o : %.cpp | $(OBJDIR)
	$(GCC) $(CXXFLAGS) -c $< -o $@

$(OBJDIR) :
	mkdir -p $(OBJDIR)

clean :
	rm -rf $(TARGET) $(OBJDIR)

.PHONY : all clean