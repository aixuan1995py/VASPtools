# VASPtools
# VASP用小脚本 不定期更新···有Bug直接联系aixuan1995@163.com
## 诈尸级更新 21.06.16

### ***利用pymatgen从MP上下载ICSD的cif***

#### 运行方式 python3直接运行

#### 用途  从materials project上下载ICSD的cif

## 诈尸级更新 20.03.31

### ***bader.py***
#### 运行方式 python3直接运行
#### 用途 处理bader电荷运行完之后的ACF.dat文件，把各元素的价电子的数值减去各原子的电荷数，且做平均值输出，并写入bader.dat文件，标准输出为各元素的平均值
## 19.08.01 从先前仓库转移过来，原仓库已经删除，并新建QEtools和PMGtools仓库，便于归档维护，另外增加GPL协议，希望使用或者借鉴本仓库的代码的脚本也能开源
## 先前脚本用法慢慢更新
## 19.06.28 更新两个小脚本
### ***cif2posc_pymatgen.py***
#### 运行方式 python3直接运行
#### 用途 利用pymatgen模块把当前文件夹下所有cif变成POSCAR格式 当只有一个cif的时候 就直接改名POSCAR 如果没有pymatgen··自行解决
### ***orderposcar.py***
#### 运行方式 python3直接运行 中间有个交互式选择顺序
#### 用途 可以根据需要变换POSCAR元素位置 相应坐标也换过来 假如Ba Cr O的顺序 可以变成 Cr O Ba 等顺序 直接读取POSCAR 导出POSCAR.vasp····**另外不兼容带固定原子模式的POSCAR**


## 补档更新
### fsc.sh
#### 运行方式 bash直接运行
#### 用途 删除前文件夹下除了四个vasp输入文件外的所有文件 写了循环判定 因为以前的命令发生过删库 为了数据安全 
### area.py
#### 运行方式 python3直接运行
#### 用途 就是得到Slab模型的表面积···
### gd.sh
#### 运行方式 bash gd.sh 固定的原子时数
#### 用途 其实是经常在slab模型的结构优化后固定底层做频率计算用的 直接读取POSCAR 里面已经是T T T F F F写好的文件··不支持原始格式固定