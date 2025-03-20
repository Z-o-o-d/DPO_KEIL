# Keil 可执行文件路径
KEIL_PATH := C:/Users/87407/AppData/Local/Keil_v5/UV4/UV4.exe
# Keil 项目文件路径
PROJECT_FILE := MDK-ARM/DPO_KEIL.uvprojx

# 编译目标
all:
    $(KEIL_PATH) -r $(PROJECT_FILE) -j0 -t DPO_KEIL

# 清理目标（删除生成的中间文件和最终可执行文件等）
clean:
    rm -f MDK-ARM/*.axf
    rm -f MDK-ARM/*.hex
    rm -f MDK-ARM/*.elf
    # 可以根据实际情况添加更多需要删除的文件