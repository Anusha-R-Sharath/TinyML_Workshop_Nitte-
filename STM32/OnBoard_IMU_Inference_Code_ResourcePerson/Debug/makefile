################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (13.3.rel1)
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include X-CUBE-AI/App/subdir.mk
-include Drivers/STM32L4xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := OnBoard_IMU_Inference_Code_ResourcePerson
BUILD_ARTIFACT_EXTENSION := elf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
OnBoard_IMU_Inference_Code_ResourcePerson.elf \

MAP_FILES += \
OnBoard_IMU_Inference_Code_ResourcePerson.map \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
OnBoard_IMU_Inference_Code_ResourcePerson.list \


# All Target
all: main-build

# Main-build Target
main-build: OnBoard_IMU_Inference_Code_ResourcePerson.elf secondary-outputs

# Tool invocations
OnBoard_IMU_Inference_Code_ResourcePerson.elf OnBoard_IMU_Inference_Code_ResourcePerson.map: $(OBJS) $(USER_OBJS) D:\Anusha_TinyML_FDP\TinyML_Workshop_Nitte-\STM32\OnBoard_IMU_Inference_Code_ResourcePerson\STM32L4S5VITX_FLASH.ld makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-gcc -o "OnBoard_IMU_Inference_Code_ResourcePerson.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m4 -T"D:\Anusha_TinyML_FDP\TinyML_Workshop_Nitte-\STM32\OnBoard_IMU_Inference_Code_ResourcePerson\STM32L4S5VITX_FLASH.ld" --specs=nosys.specs -Wl,-Map="OnBoard_IMU_Inference_Code_ResourcePerson.map" -Wl,--gc-sections -static -L../Middlewares/ST/AI/Lib --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -u _printf_float -u _scanf_float -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

OnBoard_IMU_Inference_Code_ResourcePerson.list: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "OnBoard_IMU_Inference_Code_ResourcePerson.list"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) OnBoard_IMU_Inference_Code_ResourcePerson.elf OnBoard_IMU_Inference_Code_ResourcePerson.list OnBoard_IMU_Inference_Code_ResourcePerson.map default.size.stdout
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST)

fail-specified-linker-script-missing:
	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'
	@exit 2

warn-no-linker-script-specified:
	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'

.PHONY: all clean dependents main-build fail-specified-linker-script-missing warn-no-linker-script-specified

-include ../makefile.targets
