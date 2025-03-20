### 坑爹的[Keil Assistant](https://marketplace.visualstudio.com/items?itemName=CL.keil-assistant)插件

[CSDN的屎](https://blog.csdn.net/Johnor/article/details/134353311)乱教用别的编译器。

正确的是使用时要添加AC6的库例如

```

"C:\\Users\\87407\\AppData\\Local\\Keil_v5\\ARM\\ARMCLANG\\include"

```

在.vscode/c_cpp_properties.json的includePath添加这个目录记得加","

[Keil Assistant](https://marketplace.visualstudio.com/items?itemName=CL.keil-assistant) 没添加这个库文件，而且开启的目录是MDK的目录，不是上一级目录，其他文件要上git需要换目录才可以

[Keil Assistant](https://marketplace.visualstudio.com/items?itemName=CL.keil-assistant)快捷键还不能调用Build，Rebuild，Download To Device ，只能鼠标去