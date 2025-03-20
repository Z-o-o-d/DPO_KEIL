# 定义目录和文件路径
KEIL_UV4_EXE := C:\Users\87407\AppData\Local\Keil_v5\UV4\UV4.exe
PROJECT_FILE := c:\Users\87407\Keil_prj\DPO_KEIL\DPO_KEIL\MDK-ARM\DPO_KEIL.uvprojx
TARGET_NAME := DPO_KEIL
LOG_FILE := c:\Users\87407\Keil_prj\DPO_KEIL\DPO_KEIL\MDK-ARM\.vscode\uv4.log

.PHONY: build clean

build:
	$(KEIL_UV4_EXE) -r $(PROJECT_FILE) -j0 -t $(TARGET_NAME) -o $(LOG_FILE)

# clean:
# 	@echo "Cleaning is not fully implemented yet."
    
	