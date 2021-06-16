# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:45:20 2021

注意：本脚本使用pymatgen 2019.10.16 最新版还没测试


参考自
1. https://github.com/materialsproject/mapidoc/blob/master/index.ipynb
2. https://docs.materialsproject.org/open-apis/the-materials-api/#pymatgen-wrapper
3. https://www.slideshare.net/shyuep/the-materials-api-v1/11-More_information_Materials_API_pymatgen
4. https://github.com/materialsproject/mapidoc

@author: Xuan Ai aixuan1995@163.com
"""

import pymatgen as mg

import pymatgen.io.cif

#这里填上自己申请的API keys 百度一下教程很多
api_keys = "XXXXXXXXXXXX"
mpapi = mg.MPRester(api_keys)

"""
关于关键词keywords
1. Formulae, e.g., "Li2O", "Fe2O3", "*TiO3"
2. Chemical systems, e.g., "Li-Fe-O", "*-Fe-O"
3. Materials ids, e.g., "mp-1234"
上面是官方给出的样例
"""
datas=[]
keywords=["Fe2O3","*TiO3","*-Ti-O"]
for keyword in keywords:
    datas.append(mpapi.get_data(keyword, prop="icsd_ids"))

#datas[0]就是Fe2O3的结果
for i in range(0,len(datas[0])):
    #这里最蛋疼的地方就是没法一次性获得所有信息 但是参考1里面有高级玩法 暂时先套娃吧
    #获得material_id
    material_id=datas[0][i]["material_id"]
    #再根据material_id得到pretty_formula
    pretty_formula_data=mpapi.get_data(material_id ,prop="pretty_formula")
    #这里加了个判据 万一返回的pretty_formula_data列表长度不是一错误
    if len(pretty_formula_data) == 1:
        pretty_formula=pretty_formula_data[0]["pretty_formula"]
    else:
        pretty_formula="Error"
    #得到icsd号的list
    icsd_lists=datas[0][i]['icsd_ids']
    #icsd_lists长度为空不是icsd数据库的
    if len(icsd_lists) == 0:
        icsddata="no"
    else:
    #是的话就选一个作为输出的号 这里选了列表里最小的 应该是最老的记录？
        icsddata=str(min(icsd_lists))
    #structure还要从material_id得到 得到也是个列表数据 
    structure=mpapi.get_data(material_id ,prop="structure")[0]['structure']
    #转化成cif 好像有其他写法
    cif_file_obj=mg.io.cif.CifWriter(structure,symprec=1e-4)
    name=icsddata+'_'+material_id+"_"+pretty_formula+"_"+".cif"
    cif_file_obj.write_file(str(name))
    
    print(icsddata+"\t"+pretty_formula+"\t"+material_id)
