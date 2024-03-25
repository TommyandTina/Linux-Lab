SHELL=cmd
RMDIR=rmdir /s /q
RM=del /f

OBJDIR	:= obj
DEPDIR	:= dep
OBJS :=
DEPS :=

#-----------------------------------------------------------------
# Test source files include
#-----------------------------------------------------------------
C_SRC    := $(wildcard ./*.c)
C_SRC	 += $(wildcard ./framework/*.c)
C_SRC	 += $(wildcard ./framework/util/*.c)
C_SRC	 += $(wildcard ./ut/*.c)
C_SRC	 += $(wildcard ./ut/stub/*.c)
C_SRC	 += $(wildcard ./ut/config/*.c)
C_SRC	 += $(wildcard ./ut/DMA/*.c)

INCDIR    += -I../src/include
INCDIR    += -I../src
INCDIR   += \
	-Iframework/include \
	-Iframework/util/include \
	-Iut/include \
	-Iut/stub/include \
	-Iut/config/patterns/include \
	-Iut/DMA/patterns/include \

OBJS     += $(subst ./,./$(OBJDIR)/,$(C_SRC:.c=.c.o))
DEPS     += $(subst ./,./$(DEPDIR)/,$(C_SRC:.c=.c.d))

#-----------------------------------------------------------------
# Test Target files include
#-----------------------------------------------------------------
C_DRV_SRC  += $(abspath ../src/DMA.c)

DRV_OBJS  = $(subst $(abspath ../src),./$(OBJDIR)/src,$(C_DRV_SRC:.c=.c.o))
DRV_DEPS  = $(subst $(abspath ../src),./$(DEPDIR)/src,$(C_DRV_SRC:.c=.c.d))

OBJS      += $(DRV_OBJS)
DEPS      += $(DRV_DEPS)

#--------------------------------------------------------------
# For Environment Configurations
#--------------------------------------------------------------
TEST_CONFIGS  += -DTEST_ENV_UT
TEST_CONFIGS  += -DWINDOWS_OS
TEST_CONFIGS  += -DNDEBUG

EXTRA_CFLAGS += -std=c99 -g -O0

CC := gcc
LD := g++

OUTPUT  = UT.exe

# CANTPP_CMD = cppccd "--comp:x86-Win32-gpp8.2-bundled" --no_link
# CANTPP_LD_CMD = cppccd "--comp:x86-Win32-gpp8.2-bundled" 
# CANTPP_TARGET_OPTS = "--parse:--line_directives" "--parse:-W2" "--sm:--call_seq_code" "--ci:--instr:func;call;stmt;decn;log;" "--analyse" 

TEST_CONFIGS += -DWIN32 

all: $(OUTPUT)

$(OUTPUT) : $(OBJS) $(DEPLIB) 
	$(CANTPP_LD_CMD) $(CANTPP_TARGET_OPTS) $(LD) -o $@ $(OBJS)


$(OBJDIR)/%.c.o: ./%.c
	$(eval ODIR=$(dir $@))
	$(eval DDIR=$(subst $(OBJDIR)/,$(DEPDIR)/,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(ODIR)) (mkdir $(subst /,\\,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(DDIR)) (mkdir $(subst /,\\,$(DDIR)))
	$(CC) $(INCDIR) $(EXTRA_CFLAGS) $(TEST_CONFIGS) -MD -MF $(addprefix $(DEPDIR)/,$(subst .c,.c.d,$<)) -c -o $(subst ./$(OBJDIR)/,./,$@)  $<

./obj/src/DMA.c.o: $(abspath ../src/DMA.c)
	$(eval ODIR=$(dir $@))
	$(eval DDIR=$(subst ./$(OBJDIR)/src/obj,./$(OBJDIR)/src/dep,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(ODIR)) (mkdir $(subst /,\\,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(DDIR)) (mkdir $(subst /,\\,$(DDIR)))
	$(CANTPP_CMD) $(CANTPP_TARGET_OPTS) $(CC) $(INCDIR) $(EXTRA_CFLAGS) $(TEST_CONFIGS) -MD -c -o $@ $<

-include $(DEPS)

#--------------------------------------------------------------
# For Coverage Configurations
#--------------------------------------------------------------

OBJDIR_COV	:= obj_cov
DEPDIR_COV	:= dep_cov
OBJS_COV :=
DEPS_COV :=

INCDIR_COV   += -I../../source_coverage/src/include
INCDIR_COV   += -I../../source_coverage/src
INCDIR_COV   += \
	-Iframework/include \
	-Iframework/util/include \
	-Iut/include \
	-Iut/stub/include \
	-Iut/config/patterns/include \
	-Iut/DMA/patterns/include \

C_DRV_SRC_COV  += $(abspath ../../source_coverage/src/DMA.c)

DRV_OBJS_COV  = $(subst $(abspath ../../source_coverage/src),./$(OBJDIR_COV)/src,$(C_DRV_SRC_COV:.c=.c.o))
DRV_DEPS_COV  = $(subst $(abspath ../../source_coverage/src),./$(DEPDIR_COV)/src,$(C_DRV_SRC_COV:.c=.c.d))

OBJS_COV      += $(DRV_OBJS_COV)
DEPS_COV      += $(DRV_DEPS_COV)

OBJS_COV     += $(subst ./,./$(OBJDIR_COV)/,$(C_SRC:.c=.c.o))
DEPS_COV     += $(subst ./,./$(DEPDIR_COV)/,$(C_SRC:.c=.c.d))

COVERAGE_FLAG += -DCHECK_COVERAGE

OUTPUT_COV  = UT_coverage.exe

coverage: $(OUTPUT_COV)

$(OUTPUT_COV) : $(OBJS_COV) $(DEPLIB) 
	$(CANTPP_LD_CMD) $(CANTPP_TARGET_OPTS) $(LD) -o $@ $(OBJS_COV)


$(OBJDIR_COV)/%.c.o: ./%.c
	$(eval ODIR=$(dir $@))
	$(eval DDIR=$(subst $(OBJDIR_COV)/,$(DEPDIR_COV)/,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(ODIR)) (mkdir $(subst /,\\,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(DDIR)) (mkdir $(subst /,\\,$(DDIR)))
	$(CC) $(INCDIR_COV) $(EXTRA_CFLAGS) $(TEST_CONFIGS) $(COVERAGE_FLAG) -MD -MF $(addprefix $(DEPDIR_COV)/,$(subst .c,.c.d,$<)) -c -o $(subst ./$(OBJDIR_COV)/,./,$@)  $<

./obj_cov/src/DMA.c.o: $(abspath ../../source_coverage/src/DMA.c)
	$(eval ODIR=$(dir $@))
	$(eval DDIR=$(subst ./$(OBJDIR_COV)/src/obj,./$(OBJDIR_COV)/src/dep,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(ODIR)) (mkdir $(subst /,\\,$(ODIR)))
	@if NOT EXIST $(subst /,\\,$(DDIR)) (mkdir $(subst /,\\,$(DDIR)))
	$(CANTPP_CMD) $(CANTPP_TARGET_OPTS) $(CC) $(INCDIR_COV) $(EXTRA_CFLAGS) $(TEST_CONFIGS) -MD -c -o $@ $<

-include $(DEPS_COV)
# ########################################################################################################################################

clean:
	@if EXIST $(OBJDIR) $(RMDIR) $(OBJDIR)
	@if EXIST $(DEPDIR) $(RMDIR) $(DEPDIR)
	@if EXIST $(OBJDIR_COV) $(RMDIR) $(OBJDIR_COV)
	@if EXIST $(DEPDIR_COV) $(RMDIR) $(DEPDIR_COV)
	@if EXIST $(OUTPUT) $(RM) $(OUTPUT)
	@if EXIST $(OUTPUT_COV) $(RM) $(OUTPUT_COV)

.PHONY: all clean

ALL_TESTS := 

NUMBER_OF_TESTS := 0