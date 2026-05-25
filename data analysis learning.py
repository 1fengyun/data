import numpy as np
'''arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim)#维度
print(arr.shape)#形状
print(arr.size)#总数
print(arr.dtype)#类型
a=arr.T#转置
print(a)
print(a.shape)'''
'''lst=[1,2,3]
arr=np.array(lst,dtype=str)
arr1=np.copy(arr)#复制
arr1[0]=5
print(arr1)
print(arr)
arr2=np.zeros([2,3],dtype=int)#0数组
arr3=np.ones([2,3],dtype=int)#1数组
arr4=np.empty([4,2])#空(随机数字)数组
arr5=np.ones_like(arr2)#empty_like(arr2) or zeros_like(arr2)
arr6=np.full([2,3],56)#2行3列值为56的数组
arr7=np.eye(3,2,dtype=int)#单位矩阵
arr8=np.diag([5,8,1,9])#对角矩阵
arr9=np.arange(10,0,-1)#等差
arr10=np.linspace(10,1,5)#等间隔(两边都包括)
arr11=np.logspace(10,1,5,base=5)#对数间隔(两边都包括),5的幂函数
arr12=np.random.rand(3,2)#0-1随机浮点数
arr13=np.random.uniform(10,1,[2,3])#指定范围随机浮点数
arr14=np.random.randint(1,11,[2,3])#指定范围随机整数
arr15=np.random.randn(2,3)#正态分布
np.random.seed(5)#种子
arr=np.random.randint(1,100,[3,4])
print(arr)
print(arr[:2:1,:3:2])
print(arr[(arr>10)&(arr<50)])#布尔索引
print(arr[:2:1,1:4:2][arr[:2:1,1:4:2]<50])'''
'''#广播机制(形状相同或同行/列为1,则先复制矩阵内元素为形状相同)
arr1=np.ones([1,3],dtype=int)
arr2=np.full([3,1],2)
print(arr1-arr2)
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr4=np.array([[10,11,12]])
arr5=arr4.T
print(arr3@arr5)'''
'''print(np.sqrt([[1,4,9],[16,25,36]]))#根号
print(np.exp([[2,5],[7,9]]))#e的幂函数
print(np.log([[3,4],[5,8]]))#ln5
print(np.sin([[np.pi/2,np.pi],[1,np.pi/4]]))#sin
print(np.cos([[np.pi/2,np.pi],[1,np.pi/4]]))#cos
print(np.tan([[np.pi/2,np.pi],[1,np.pi/4]]))#tan
print(np.abs([[-3.1415926535+3.1516,-4.5],[-1.1*1.1,0]]))#绝对值
print(np.power([[2],[3]],[[3],[4]]))#幂函数
print(np.round([[-3.1415926535+3.1416,-3.5-3.6],[-3.4*4.5,4.6/4.4]]))#4舍5入
print(np.ceil([[-3.1415926535+3.1416,-3.5-3.6],[-3.4*4.5,4.6/4.4]]))#向上取整
print(np.floor([[-3.1415926535+3.1416,-3.5-3.6],[-3.4*4.5,4.6/4.4]]))#向下取整
print(np.isnan([[1,0,np.nan],[8,-4,0]]))#检测缺失值
arr6=np.random.uniform(1,100,[2,3])
print(np.sum(arr6))#求和
np.random.seed(1)
arr7=np.random.randint(1,100,[5,3])
print(arr7)
print(np.mean(arr7))#平均值
print(np.median(arr7,axis=0))#中位数，2维及以上数组不指定axis则先展开排序再求中位数，axis=0沿列求，axis=1沿行求
print(np.median(arr7,axis=1))
print(np.var(arr7))#方差
print(np.std(arr7))#标准差
print(np.min(arr7),np.argmin(arr7))#最小值,argmin/max打出对应索引值
print(np.max(arr7),np.argmax(arr7))#最大值
print(np.percentile(arr7,4))#分位数
print(np.cumsum(arr7))#累计和,np.cumsum(arr7)[-1]总和
print(np.cumprod(arr7))#累计积
arr8=np.random.randn(5,3)
print(np.greater(arr7,arr8))#比arr8大输出True
print(np.less(arr7,[[1],[4],[8],[12],[35]]))#比[[1],[4],[8],[12],[35]]小输出True
print(np.equal(arr7,[1,4,8]))#与[1,4,8]相等输出True
print(np.logical_and([[0,1],[8,np.nan]],[[1,0],[np.nan,-7]]))#与运算
print(np.logical_or([[0,1],[8,np.nan]],[[1,0],[np.nan,-7]]))#或运算
print(np.logical_not([[0,1],[1,np.nan]]))#非运算
print(np.any(arr7))#任意元素为真则输出True
print(np.all(arr7))#全部元素为真则输出True
print(np.where(arr7<arr8,arr7,arr8))#条件，符合，不符合
print(np.select([arr7<arr8,(arr7<=arr8)&(arr7>=arr8),arr7>arr8],["小于","等于","大于"],default="错误"))#条件,结果,类型
print(np.sort(arr7))#升序排序
print(np.unique(arr7,return_counts=True))#去重,计数每个数出现次数
print(np.append(arr7,arr8,axis=0))#添加,axis=1按行添加
print(np.concatenate([arr7,arr8],axis=0))#拼接,axis=1行拼接
print(np.split(arr7,[3,5]))#分割,每份个数,份数,1维可按份数或索引分割
print(np.reshape(arr7,[3,5],order="F"))#重组形状,[3,-1]或[-1,3]指只指定行数或列数,"F"按列重组,"C"按行重组'''
'''import pandas as pd(Series)
a=pd.Series([10,5,6,np.nan,None,6],index=[i for i in range(7,1,-1)],name="数据")#创建，自定义索引,名字
b=pd.Series({"a":1,2:"b",3:"c"})
c=pd.Series(b,index=[1,3])#索引创建,不存在输出NaN
print(a.index)#索引
print(a.index.year)#获取每年的索引/月(month)/天(day)/小时(hour)/分钟(min)/秒(second)
print(a.values)#值
print(a.keys())#获取索引
print(a.shape,a.size,a.ndim)#形状,数量,维度
print(a.dtype,a.name)#类型,名字
print(a.loc[2:5:-2])#显式索引(自定义索引)
print(a.iloc[3:0:-2])#隐式索引(真正索引)
print(a.at[5])#显式索引(不支持切片)
print(a.iat[0])#隐式索引(不支持切片)
print(b["a"])#直接索引
print(a[a==5])#布尔索引(值)
print(a.head(6))#前6行(默认前5行)
print(a.tail(6))#后6行(默认后5行)
print(a.describe())#所有描述性信息
print(a.count())#计数
print(a.isna())#检查缺失值
print(a.isin([4,5,6]))#判断值是否在列表中
print(a.mean(),a.std(),a.var(),a.min(),a.idxmin(),a.max(),a.idxmax(),a.median(),a.abs())#平均数,标准差,方差,最小值,最小值索引,最大值,最大值索引,中位数,绝对值
print(a.sort_index(),a.sort_values(ascending=False))#按照索引,值降序排序(默认升序)
print(a.quantile(0.8))#分位数
print(a.mode())#众数
print(a.value_counts())#值的计数
print(a.drop_duplicates(),a.unique())#去重
print(a.nunique())#去重后元素个数
print(a.diff())#元素间差值
print(a.tolist())#转为列表
print(pd.date_range("2020-1-2",periods=10,freq="YE"))#日期,数量,年末/年初(YS)/月末(ME)/月初(MS)/周(W)/天(D)/小时(h)/分钟(min)/秒(s)
print(a.pct_change())#收益率(当天收益/前一天收益-1)
print(a.resample("3MS"))#重新采样(3个月)
print((a>0).rolling(3).sum())#向上滑动3格计数a>0的总数
d=a.between_time("8:00","22:00")#筛选8-22点间的数据
e=a.drop(d)#去除a中d的数据
print(a.nlargest(3))#最大的3个数据'''
'''import pandas as pd(DataFrame)
a1=pd.Series([1,2,3,4,5])
a2=pd.Series([6,7,8,9,10])
a=pd.DataFrame({1:a1,2:a2})#series创建
b=pd.DataFrame({"name":[1,2,3,4,2,6],"age":(7,8,9,10,11,12),"fat":(13,14,15,16,17,None)},index=[1,2,3,4,5,6],columns=("age","name","fat"))#字典创建
c=pd.DataFrame([[1,2,3],[4,5,6]],index=[1,2],columns=[1,2,3])#矩阵创建
c[4]=c.sum(axis=1)#增加第4列
print(b.index)#行索引
print(b.columns)#列标签
print(b.values)#值
print(b.ndim,b.dtypes,b.shape,b.size,b.T)#维度,类型,形状,数量,转置
print(b.info())#类型
print(b.loc[2:5:1,"age":"name":1])#显式索引
print(b.iloc[1:4:1,:3:1])#隐式索引
print(b.at[1,"name"])#显式索引
print(b.iloc[0,1])#隐式索引
print(b["age"],b.age)#单列数据
print(b[["name","age"]])#类型为DataFrame的多列数据
print(b[(b["age"]<10) & (b["name"]<4)])#布尔索引
print(b.head(6))#前6行数据(默认前5行)
print(b.tail(6))#后6行数据(默认后5行)
print(b.sample(3))#随机取3行
print(b.isin([2,13]))#查看元素是否在集合中
print(b.isna())#检查缺失值
print(b["name"].sum(),b["name"].max(),b["name"].min(),b["name"].mean(),b["name"].median(),b["name"].mode())#"name"列求和,最大值,最小值,平均数,中位数,众数(可用axis)
print(b["name"].std(),b["name"].var())#"name"列标准差,方差(可用axis)
print(b["name"].quantile(0.7))#"name"列分位数
print(b.describe())#所有描述性信息
print(b.count())#每一列非缺失值的个数
print(b.value_counts())#值出现的数量
print(b.drop_duplicates(subset=["name"],keep="last"))#"name"列去重(删整行),去除最先出现的重复数据(keep="first"去除最后出现的重复数据)
print(b.duplicated(subset=["name"]))#查看"name"列是否重复(默认行检查,整行记录相同输出true)
print(b.replace(13,20))#替换
print(b.cumsum(axis=0))#累计和,axis=0列,axis=1行
print(b.cumprod(axis=1))#累计积
print(b.cummin(axis=0))#累计最小值
print(b.cummax(axis=1))#累计最大值
print(b.sort_index(ascending=False))#索引降序排序(默认升序)
print(b.sort_values(by=["name","age"],ascending=[False,True]))#"name"列值降序排序(默认升序),"name"列排好后相同的值"age"列值按升序排序
print(b.nlargest(2,columns=["name","age"]))#取出"name","age"列最大的2行数据
print(b.nsmallest(2,columns=["name","age"]))#取出"name","age"列最小的2行数据
b.drop("name",inplace=True,axis=1)#去除"name"列
print(b["name"].apply(fun1))#对"name"列每个元素执行fun1函数
print(b[["age","name","fat"]].corr())#计算"name","age"和"fat"的相关系数'''
import pandas as pd
'''a=pd.read_csv("data/employees.csv")#文件导入
a.head().to_csv("data/new.csv")#文件导出'''
'''import json as js
with open('data/test.json',encoding="utf-8") as f:
    a=js.load(f)
    print(pd.DataFrame(a["users"]))#json文件处理'''
#数据清洗
#缺失值处理
'''s=pd.Series([1,2,np.nan,None,pd.NA])
df=pd.DataFrame([[1,pd.NA,np.nan],[2,4,5],[None,6,4]])
print(df.isna(),df.isnull())#查看缺失值
print(df.isna().sum(axis=1))#按行计算缺失值个数(默认按列计算缺失值个数)
print(s.dropna())#去除缺失值
print(df.dropna(axis=0))#按列去除缺失值的行
print(df.dropna(how="all"))#非全部缺失值不删
print(df.dropna(thresh=2))#至少有2个不是缺失值,就保留
print(df.dropna(subset=[0,1]))#去除第0,1列缺失值的行
c=pd.read_csv("data/weather_withna.csv")
print(c.isna().sum(axis=0))
print(c.fillna({"temp_max":20,"wind":3.7}).tail())#字典填充
print(c.fillna(c[["wind","temp_min"]].mean()).tail())#统计值填充
print(c.ffill().tail())#用上面的值填充
print(c.bfill().tail())#用下面的值填充'''
#重复值处理
'''data=pd.DataFrame({
                "name":["alice","alice","bob","alice","jack","bob"],
                "age":[26,25,30,25,35,30],
                "city":["NY","NY","LA","NY","SF","LA"]
})
print(data.duplicated())
print(data.drop_duplicates(subset=["age"],keep="first"))'''
#数据类型处理
'''df=pd.read_csv("data/sleep.csv")
df["age"]=df["age"].astype("int16")#数值类型转换
df["gender"]=df["gender"].astype("category")#转为分类
df["gender"]=df["gender"].map({"Female":True,"Male":False})#将男性变为True,女性变为False'''
#数据变形
'''data=pd.DataFrame({
                "ID":[1,2],
                "name":["alice","bob"],
                "Math":[90,85],
                "English":[88,92],
                "Science":[95,89]
})
print(data.T)
df=pd.melt(data,id_vars=["ID","name"],var_name="科目",value_name="分数")#宽表转长表(表,不变,变的名字)
print(df.sort_values(by=["name"],ascending=False))
print(pd.pivot(df,index=["ID","name"],columns="科目",values="分数"))#长表转宽表(列转行)'''
#分列
'''data=pd.DataFrame({
                "ID":[1,2],
                "name":["alice smith","bob smith"],
                "Math":[90,85],
                "English":[88,92],
                "Science":[95,89]
})
data[["First","last"]]=data["name"].str.split(" ",expand=True)
print(data)
df=pd.read_csv("data/sleep.csv")
df[["ceil_blood","floor_blood"]]=df["blood_pressure"].str.split("/",expand=True)
#df["ceil_blood"]=df["blood_pressure"].str.extract(r"(\\d+)/")#分列,正则表达式,\\d+表示多个数字,"/"表示分割位置
print(df[["ceil_blood","floor_blood"]].astype(int).dtypes)'''
#数据分箱
'''df=pd.read_csv("data/employees.csv")
df1=pd.cut(df["salary"],bins=[0,10000,20000,30000],labels=["低","中","高"])#按值分箱(表,分段区间,段名)
print(df1.value_counts())
df2=pd.qcut(df["salary"],3,labels=["低","中","高"])#等数量分箱(表,分段数,段名)
print(df2.value_counts())
data=pd.read_csv("data/sleep.csv")
data1=pd.cut(data["sleep_quality"],bins=3,labels=["差","中","好"])
data2=pd.qcut(data["sleep_quality"],3,labels=["差","中","好"])
data["gender"]=data["gender"].astype("category")
print(data["gender"].value_counts())
df3=pd.DataFrame({
                "name":["jack","alice","tom","bob"],
                "age":[20,30,40,50],
                "gender":["female","male","female","male"]
})
df3.set_index("name",inplace=True)#设置索引
df3.reset_index(inplace=True)#去除设置的索引
print(df3.rename(columns={"age":"年龄"},index={0:5}))#修改列名和索引
df3.index=[1,2,3,4]#修改索引
df3.columns=["姓名","年龄","性别"]#修改列名'''
#时间数据处理
'''d=pd.Timestamp("2025-05-02 10:22")
print(type(d))
print(d.quarter,d.year,d.month,d.week,d.day,d.hour,d.minute,d.second)#季度,年,月,周,日,时,分,秒
print(d.is_leap_year)#是否是闰年
print(d.day_name())#星期几
print(d.to_period("Q"))#转换为季度(年:Y,月:M,周:W,天:D,小时:h,分钟:min,秒:s)
a=pd.to_datetime("20250128102200")#字符串转日期时间
df=pd.DataFrame({
                "sales":[100,200,300],
                "date":["20250601","20250602","20250603"]
})
df["datetime"]=pd.to_datetime(df["date"])
print(df["datetime"].dt.day_name())#星期几
print(df["datetime"].dt.quarter)#季度
df1=pd.read_csv("data/weather.csv")
df1["datetime"]=pd.to_datetime(df1["date"])
print(df1["datetime"])
print(df1["datetime"].dt.day_name())
print(df1["datetime"].dt.minute)#分钟
df2=pd.read_csv("data/weather.csv",parse_dates=["date"])#解析为日期
df2.set_index("date",inplace=True)#将日期作为索引
d1=pd.Timestamp("20130115")
d2=pd.Timestamp("20230223")
print(d2-d1)#时间间隔
df3=pd.read_csv("data/weather.csv",parse_dates=["date"])
df3["delta"]=df3["date"]-df3["date"][0]
df3.set_index("delta",inplace=True)
df3.reset_index(inplace=True)
df3.set_index("date",inplace=True)
print(df3[["temp_max","temp_min"]].resample("YE").mean())#重新采样'''
#分组聚合
'''df=pd.read_csv("data/employees.csv")
df=df.dropna(subset=["department_id"])
df["department_id"].astype(int)
print(df.groupby(["department_id"]).groups)#查看分组
print(df.groupby(["department_id"]).get_group(20))#查看具体某个分组数据
print(df.groupby(["department_id"]).agg({"salary":["mean","count"]}))#查看分组后的工资的平均值和数量
df1=df.groupby(["department_id"])[["salary"]].mean()
df1["salary"]=df1["salary"].round(2)
print(df1.reset_index().sort_values(by="salary",ascending=False))
df2=df.groupby(["department_id","job_id"])[["salary"]].mean()
df2.reset_index()
df2["salary"]=df2["salary"].round(2)
print(df2.sort_values(by="salary",ascending=False))'''
'''import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
df=pd.read_csv("data/penguins.csv")
df.dropna(axis=0,inplace=True)
sns.histplot(data=df,x="species",bins=4,kde=True)#直方图,参数,横坐标,区间,核密度估计图是否在同一张图上
sns.kdeplot(data=df,x="bill_length_mm")#核密度估计图
sns.countplot(data=df,x="island")#计数图
sns.scatterplot(data=df,x="body_mass_g",y="flipper_length_mm",hue="sex")#散点图,按"sex"分组
sns.jointplot(data=df,x="body_mass_g",y="flipper_length_mm",kind="hex")#蜂窝图,按"hex"分组
sns.kdeplot(data=df,x="body_mass_g",y="flipper_length_mm",fill=True,cbar=True)#二维核密度估计图,填充,颜色示意条
sns.barplot(data=df,x="species",y="bill_length_mm",estimator="mean",errorbar=None)#条形图,平均值,异常值的显示
sns.boxplot(data=df,x="species",y="bill_length_mm")#箱线图
sns.pairplot(data=df,hue="species")#成对关系图(以"species"分类展示各变量间的关系,"species"为图例)
sns.heatmap(df,cmap="coolwarm")#热力图,cmap颜色("coolwarm"红蓝色)
plt.show()'''
'''from pyecharts.charts import Bar#柱状图
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType
bar=Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))#背景颜色(黑色)
bar.add_xaxis(xaxis_data=Faker.choose())#随机横坐标名称
bar.add_yaxis("A",#图例
              y_axis=Faker.values(),#随机值
              label_opts=opts.LabelOpts(is_show=False),#是否显示图像上的值
              markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均值",type_="average")]),#用直线表示平均值
              category_gap=3,#单个图像的间隔
              color="red")#图像颜色
bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="最大值",type_="max"),#用点表示最大值
                                                            opts.MarkPointItem(name="最小值",type_="min")]))#用点表示最小值
bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=True,#是否显示x轴
                                             min_=0,#x轴最小值
                                             max_=6,#x轴最大值
                                             boundary_gap=True,#横坐标两边是否与x轴有间距
                                             splitline_opts=opts.SplitLineOpts(is_show=False),#是否开启x轴网格线
                                             type_="category",#指定x轴类型为类目轴
                                             axispointer_opts=opts.AxisPointerOpts(is_show=True,#是否触发坐标轴指示器
                                                                                   type_="shadow")),#类型为阴影
                    tooltip_opts=opts.TooltipOpts(is_show=True,#是否触发提示框
                                                  trigger="axis",#坐标轴触发
                                                  axis_pointer_type="cross"),#触发显示十字
                    yaxis_opts=opts.AxisOpts(is_show=True,#是否显示y轴
                                             min_=0,#y轴最小值
                                             max_=200,#y轴最大值
                                             splitline_opts=opts.SplitLineOpts(is_show=True)),#是否开启y轴网格线
                    title_opts=opts.TitleOpts(title="柱状图",#标题
                                              subtitle="二级标题",
                                              title_link="https://ehall.fjjxu.edu.cn"))#点击标题跳转的域名
bar.render()#生成HTML文件'''
'''from pyecharts.charts import Bar#直方图
from pyecharts.faker import Faker
from pyecharts import options as opts
bar=Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("频率",Faker.values(),label_opts=opts.LabelOpts(is_show=False),
              markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均频率",type_="average")]),
              category_gap=3,color="black")
bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="频率最大",type_="max"),
                                                            opts.MarkPointItem(name="频率最小",type_="min")]))
bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=True,min_=-1,max_=8,boundary_gap=True,
                                             splitline_opts=opts.SplitLineOpts(is_show=False)),
                    yaxis_opts=opts.AxisOpts(is_show=True,min_=0,max_=200),
                    title_opts=opts.TitleOpts(title="直方图"))
bar.render()'''
'''from pyecharts.charts import Bar#条形图
from pyecharts.faker import Faker
from pyecharts import options as opts
bar=Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(position="right"),#图像上的值按右对齐
              markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="平均值",type_="average")]),
              category_gap=3,color="black")
bar.reversal_axis()#翻转xy轴
bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="最大值",type_="max"),
                                                            opts.MarkPointItem(name="最小值",type_="min")]))
bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=True,min_=0,max_=200,boundary_gap=True,
                                             splitline_opts=opts.SplitLineOpts(is_show=False)),
                    yaxis_opts=opts.AxisOpts(is_show=True,min_=-1,max_=8),
                    title_opts=opts.TitleOpts(title="条形图"))
bar.render()'''
'''from pyecharts.charts import Bar#堆叠图
from pyecharts.faker import Faker
from pyecharts import options as opts
bar=Bar()
bar.add_xaxis(Faker.choose())
bar.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(is_show=False),category_gap=3,color="black",
              stack="stack")#堆叠参数(若一致则堆叠)
bar.add_yaxis("B",Faker.values(),label_opts=opts.LabelOpts(is_show=False),category_gap=3,color="red",
              stack="stack")
bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=True,min_=-1,max_=8,boundary_gap=True,
                                             splitline_opts=opts.SplitLineOpts(is_show=False)),
                    yaxis_opts=opts.AxisOpts(is_show=True,min_=0,max_=300),
                    title_opts=opts.TitleOpts(title="堆叠图"))
bar.render()'''
'''from pyecharts.charts import Line#折线图
from pyecharts.faker import Faker
from pyecharts import options as opts
line=Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="black")
line.add_yaxis("B",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="red")
line.set_global_opts(xaxis_opts=opts.AxisOpts(min_=-1,max_=8,boundary_gap=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False)),
                     yaxis_opts=opts.AxisOpts(min_=0,max_=200),
                     title_opts=opts.TitleOpts(title="折线图"))
line.render()'''
'''from pyecharts.charts import Line#曲线图
from pyecharts.faker import Faker
from pyecharts import options as opts
line=Line()
x_values=Faker.choose()
y1_values=Faker.values()
y2_values=Faker.values()
line.add_xaxis(xaxis_data=x_values)
line.add_yaxis("A",y_axis=y1_values,label_opts=opts.LabelOpts(is_show=False),color="black",
               is_smooth=True,#是否以曲线显示
               markpoint_opts=opts.MarkPointOpts(
                   data=[opts.MarkPointItem(coord=[x_values[1],y1_values[1]],value=y1_values[1],name="该点的值")]))#标出某点的值
line.add_yaxis("B",y_axis=y2_values,label_opts=opts.LabelOpts(is_show=False),color="red",
               is_smooth=True,
               markpoint_opts=opts.MarkPointOpts(
                   data=[opts.MarkPointItem(coord=[x_values[1],y2_values[1]],value=y2_values[1],name="该点的值")]))
line.set_global_opts(xaxis_opts=opts.AxisOpts(min_=-1,max_=8,boundary_gap=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False)),
                     yaxis_opts=opts.AxisOpts(min_=0,max_=200),
                     title_opts=opts.TitleOpts(title="曲线图"))
line.render()'''
'''from pyecharts.charts import Line#堆图
from pyecharts.faker import Faker
from pyecharts import options as opts
line=Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="black",
               is_smooth=True,stack="stack")
line.add_yaxis("B",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="red",
               is_smooth=True,stack="stack")
line.set_global_opts(xaxis_opts=opts.AxisOpts(min_=-1,max_=8,boundary_gap=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False)),
                     yaxis_opts=opts.AxisOpts(min_=0,max_=300),
                     title_opts=opts.TitleOpts(title="堆图"))
line.render()'''
'''from pyecharts.charts import Line#面积图
from pyecharts.faker import Faker
from pyecharts import options as opts
line=Line()
line.add_xaxis(Faker.choose())
line.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="black",
               is_smooth=True,stack="stack",
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5))#覆盖面积(透明度)
line.add_yaxis("B",Faker.values(),label_opts=opts.LabelOpts(is_show=False),color="red",
               is_smooth=True,stack="stack",
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
line.set_global_opts(xaxis_opts=opts.AxisOpts(min_=-1,max_=8,boundary_gap=True,
                                              splitline_opts=opts.SplitLineOpts(is_show=False)),
                     yaxis_opts=opts.AxisOpts(min_=0,max_=300),
                     title_opts=opts.TitleOpts(title="面积图"))
line.render()'''
'''from pyecharts.charts import Pie#饼图
from pyecharts.faker import Faker
from pyecharts import options as opts
pie=Pie()
pie.add("A",
        [list(z) for z in zip(Faker.choose(),Faker.values())],#图例和值
        radius=["40%","70%"],#内外半径关于中心点的占比
        rosetype="area")#角度相同情况下根据数值调整半径大小(radius参数则角度不同)
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))#显示数据占比(b:数据,d:百分比,%表示在百分比后加%)
pie.set_global_opts(title_opts=opts.TitleOpts(title="饼图"))
pie.set_colors(["blue","red","green","yellow","pink","black","orange"])#设置颜色
pie.render()'''
'''from pyecharts.charts import Scatter#散点图
from pyecharts import options as opts
from pyecharts.faker import Faker
import random
sca=Scatter()
x=[random.randint(0,100) for i in range(10)]
sca.add_xaxis(x)
sca.add_yaxis("A",y_axis=Faker.values(),label_opts=opts.LabelOpts(is_show=False))#symbol_size=10,点大小,symbol="rect",点形状(矩形)
sca.set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"),#指定x轴类型为递增的值
                    visualmap_opts=opts.VisualMapOpts(type_="size",range_size=[5,15]),#点的大小按值的大小变化,大小范围
                    title_opts=opts.TitleOpts(title="散点图"))
sca.render()'''
'''from pyecharts.charts import Boxplot#箱线图
from pyecharts.faker import Faker
from pyecharts import options as opts
import random
box=Boxplot()
box.add_xaxis([f"{i}" for i in range(1,5)])
box.add_yaxis("A",box.prepare_data([[random.randint(50,80) for j in range(50)] for i in range(1,5)]))
box.add_yaxis("B",box.prepare_data([[random.randint(40,70) for j in range(50)] for i in range(1,5)]))
box.set_global_opts(title_opts=opts.TitleOpts(title="箱线图"))
box.render()'''
'''from pyecharts.charts import HeatMap#热力图
from pyecharts import options as opts
from pyecharts.faker import Faker
import random
hm=HeatMap()
value=[[i,j,random.randint(0,40)] for i in range(24) for j in range(7)]
hm.add_xaxis(Faker.clock)
hm.add_yaxis("A",Faker.week,value,label_opts=opts.LabelOpts(is_show=True,position="inside"))#positon数值的显示位置(inside中央)
hm.set_global_opts(title_opts=opts.TitleOpts(title="热力图"),
                   visualmap_opts=opts.VisualMapOpts())#可视化图
hm.render()'''
'''from pyecharts.charts import EffectScatter#涟漪散点图
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
sca=EffectScatter()
sca.add_xaxis(Faker.choose())
sca.add_yaxis("A",Faker.values(),label_opts=opts.LabelOpts(position="top"),
              symbol=SymbolType.DIAMOND)#星形
sca.set_global_opts(title_opts=opts.TitleOpts(title="涟漪散点图"))
sca.render()'''
'''from pyecharts.charts import Kline#K线图
from pyecharts.faker import Faker
from pyecharts import options as opts
kline=Kline()
data=[[2312.5,2336.7,2300,2377.41],[2313.4,2418.43,2404.6,2432.4],[2441.91,2421.56,2418.43,2444.8],[2383.49,2397.18,2370.61,2397.94]]
kline.add_xaxis([f"2030/10/{i+1}" for i in range(len(data))])
kline.add_yaxis("A",data,itemstyle_opts=opts.ItemStyleOpts(color="red",color0="blue"))
kline.set_global_opts(title_opts=opts.TitleOpts(title="K线图"))
kline.render()'''
'''from pyecharts.charts import Funnel#漏斗图
from pyecharts.faker import Faker
from pyecharts import options as opts
funnel=Funnel()
funnel.add("A",[list(z) for z in zip(Faker.choose(),Faker.values())],label_opts=opts.LabelOpts(position="inside"),
           sort_="ascending")#升序
funnel.set_global_opts(title_opts=opts.TitleOpts(title="漏斗图"))
funnel.render()'''
'''from pyecharts.charts import WordCloud#词云图
from pyecharts.faker import Faker
from pyecharts import options as opts
wc=WordCloud()
data=[["联想","14.5"],["ThinkPad","15.7"],["惠普","14.4"],["华硕","8.2"],["机械革命","2.4"],["外星人","1.5"],["戴尔","8.1"]]
wc.add("A",data_pair=data)
wc.set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
wc.render()'''
'''from pyecharts.charts import Radar#雷达图
from pyecharts import options as opts
from pyecharts.faker import Faker
radar=Radar()
data=[[8,7,8,8,9,7]]
data1=[[9,5,7,8,6,7]]
radar.add_schema(schema=[opts.RadarIndicatorItem(name="拍照",max_=10),
                 opts.RadarIndicatorItem(name="外观",max_=10),
                 opts.RadarIndicatorItem(name="性能",max_=10),
                 opts.RadarIndicatorItem(name="屏幕",max_=10),
                 opts.RadarIndicatorItem(name="内存",max_=10),
                 opts.RadarIndicatorItem(name="系统",max_=10)])
radar.add("OPPO",data,color="red")
radar.add("华为",data1,color="blue")
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.set_global_opts(title_opts=opts.TitleOpts(title="雷达图"))
radar.render()'''
'''from pyecharts.charts import Map#地图
from pyecharts import options as opts
map=Map()
map.add("A",[["北京",10],["上海",20]],
        is_map_symbol_show=False,#是否显示点,
        maptype="china-cities",#中国城市地图("maptype"参数可用"河北","上海"等)
        label_opts=opts.LabelOpts(is_show=False))
map.set_global_opts(title_opts=opts.TitleOpts(title="地图"),
                    visualmap_opts=opts.VisualMapOpts())#可视化地图
map.render()'''
'''from pyecharts.charts import Geo#坐标地图
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import SymbolType,GeoType
from pyecharts.types import VisualMap
geo=Geo()
geo.add_schema()
geo.add("A",[["北京","上海"],["北京","深圳"],["西藏","浙江"]],label_opts=opts.LabelOpts(is_show=False),
        type_=GeoType.LINES,#指定类型为直线图
        linestyle_opts=opts.LineStyleOpts(curve=0.3),#线弯曲程度
        color="blue",
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,color="blue"))#点形状改为箭头,type_=GeoType.EFFECT_SCATTER(涟漪特效散点图)
geo.set_global_opts(title_opts=opts.TitleOpts(title="坐标地图"),visualmap_opts=opts.VisualMapOpts())
geo.render()'''
'''from pyecharts.charts import Bar,Timeline#时间线图
from pyecharts.faker import Faker
from pyecharts import options as opts
x=Faker.choose()
t=Timeline()
for i in range(2000,2006):
    bar=Bar()
    bar.add_xaxis(x)
    bar.add_yaxis("A",Faker.values())
    bar.add_yaxis("B",Faker.values())
    bar.set_global_opts(title_opts=opts.TitleOpts(title="时间线图"))
    t.add(bar,f"第{i}年")
t.render()'''
'''from pyecharts.charts import Bar,Line#组合图
from pyecharts.faker import Faker
from pyecharts import options as opts
bar=Bar()
bar.add_xaxis(["1月","2月","3月","4月","5月","6月"])
bar.add_yaxis("蒸发量",[2.0,4.9,7.0,23.2,25.6,76.7],label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis("降水量",[2.6,5.9,9.0,26.4,28.7,70.7],label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(title_opts=opts.TitleOpts(title="组合图"),
                    tooltip_opts=opts.TooltipOpts(is_show=True,trigger="axis",axis_pointer_type="cross"),
                    xaxis_opts=opts.AxisOpts(type_="category",
                    axispointer_opts=opts.AxisPointerOpts(is_show=True,type_="shadow")))
bar.extend_axis(yaxis=opts.AxisOpts(#添加一条新y轴
                                    name="温度",min_=2,max_=11,
                                    interval=3,#新y轴值每次增加3,
                                    axislabel_opts=opts.LabelOpts(formatter="{value}°C")))#y轴显示的值后加上°C
line=Line()
line.add_xaxis(["1月","2月","3月","4月","5月","6月"])
line.add_yaxis("平均温度",[2.0,2.2,3.3,4.5,6.3,10.2],yaxis_index=1,label_opts=opts.LabelOpts(is_show=False))
bar.overlap(line)#合并图
bar.render()'''
'''import matplotlib.pyplot as plt#折线图
from matplotlib import rcParams#字体
rcParams["font.family"]="SimHei"#黑体
plt.figure(figsize=(10,5))#绘制的图纸长和宽为10,高为5
month=["1月","2月","3月","4月"]
sales=[100,150,80,130]
plt.plot(month,sales,#绘制图线(横坐标,纵坐标)
         label="产品A",#图例
         color="black",#颜色
         linewidth=2,#粗细
         linestyle="--",#线型(虚线,实线"-",点划线"-.",点线":")
         marker="o")#图像点形状(圆形,三角("<",">"),方形"s",五边形"p",六边形"h")
plt.legend(loc="upper left",fontsize=10)#图例位置(左(left),右(right),上(upper),下(lower),居中(center)),图例大小
plt.xlim(-1,4)#横坐标范围
plt.ylim(0,160)#纵坐标范围
plt.xticks(rotation=0,fontsize=12,color="green")#横坐标字体旋转角度,字体大小,字体颜色
plt.yticks(rotation=0,fontsize=12,color="green")#纵坐标字体旋转角度,字体大小,字体颜色
plt.title("2025年销售趋势",color="blue",fontsize=20)#图像标题,标题颜色,标题大小
plt.xlabel("月份",fontsize=10,color="red")#横坐标标题,标题大小,标题颜色
plt.ylabel("销售额(万元)",fontsize=10,color="red")#纵坐标标题,标题大小,标题颜色
for x,y in zip(month,sales):
    plt.text(x,y+1,y,ha="center",va="bottom",fontsize=10,color="pink")#图像点的数值显示位置,显示的文字,
    #位置对齐(左(left),居中(center),右(right)),位置对齐(上(top)，居中(center),下(bottom)),
    #文字大小,文字颜色
plt.grid(True,axis="y",alpha=0.4,color="orange",linestyle="--")#网格线,网格线在哪个轴,网格线深浅,网格线颜色,网格线线型
plt.show()#显示图像'''
'''import matplotlib.pyplot as plt#柱状图
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(10,5))
subjects=["语文","数学","英语","物理"]
scores=[85,92,78,88]
plt.bar(subjects,scores,label="小红",linewidth=0.4,color="black")
plt.legend(loc="upper left",fontsize=13)
plt.xlim(-1,4)
plt.ylim(0,100)
plt.title("小红2025年成绩分布",color="blue",fontsize=20)
plt.xlabel("科目",fontsize=10)
plt.ylabel("分数",fontsize=10)
for x,y in zip(subjects,scores):
    plt.text(x,y,y,color="red",fontsize=10,ha="center",va="bottom")
plt.grid(True,axis="y",alpha=0.5,color="pink",linestyle="--")
plt.tight_layout()#自动优化排版
plt.show()'''
'''import matplotlib.pyplot as plt#条形图
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(10,5))
subjects=["语文","数学","英语","物理"]
scores=[85,92,78,88]
plt.barh(subjects,scores,label="小红",linewidth=0.7,color="black")#纵坐标,横坐标
plt.legend(loc="upper left",fontsize=13)
plt.xlim(0,100)
plt.ylim(-1,4)
plt.title("小红2025年成绩分布",color="blue",fontsize=20)
plt.xlabel("分数",fontsize=10)
plt.ylabel("科目",fontsize=10)
for x,y in zip(scores,subjects):
    plt.text(x+1,y,x,color="red",fontsize=10,ha="left",va="center")
plt.grid(True,axis="x",alpha=0.5,color="pink",linestyle="--")
plt.tight_layout()
plt.show()'''
'''import matplotlib.pyplot as plt#饼图
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(10,5))
things=["学习","娱乐","运动","睡觉","其他"]
times=[6,3,1,8,5]
plt.pie(times,labels=things,autopct="%.1f%%",startangle=45,#数据,名称,占比,起始角度
        colors=["red","white","blue","orange","pink"],wedgeprops={"width":0.6},#颜色,圆环占比
        pctdistance=0.7,explode=[0.1,0,0,0,0])#圆环占比的位置离圆心的距离与总距离的占比,各块距离圆心的距离
plt.title("一天的时间分布",color="red",fontsize=20)
plt.text(0,0,"总计:\n100%",ha="center",va="center",color="black",fontsize=15)
plt.tight_layout()
plt.show()'''
'''import matplotlib.pyplot as plt#散点图
import random
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(10,8))
x=[]
y=[]
for i in range(1000):
        tmp=random.uniform(0,10)
        x.append(tmp)
        tmp1=2*tmp+random.uniform(-2,2)
        y.append(tmp1)
plt.scatter(x,y,color="black",alpha=0.5,label="数据",
            s=20)#点大小
plt.legend(loc="upper left",fontsize=13)
plt.xlim(-1,11)
plt.ylim(-3,23)
plt.xticks(rotation=0,fontsize=12,color="green")
plt.yticks(rotation=0,fontsize=12,color="green")
plt.title("X变量与Y变量的关系",color="red",fontsize=20)
plt.xlabel("X自变量",fontsize=10)
plt.ylabel("Y因变量",fontsize=10)
plt.grid(True,alpha=0.5,color="pink",linestyle="--")
plt.plot([0,10],[0,20],color="black",linewidth=2,linestyle="-")
plt.tight_layout()
plt.show()'''
'''import matplotlib.pyplot as plt#箱线图
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(8,6))
data={"语文":[82,85,88,70,90,76,84,83,95],"数学":[75,80,79,93,88,82,87,89,92],"英语":[70,72,68,65,78,80,85,90,95]}
plt.boxplot(data.values(),tick_labels=data.keys())#箱线图数据,横坐标
plt.title("各科成绩分布")
plt.ylabel("分数")
plt.grid(True,axis="y",alpha=0.5,linestyle="--")
plt.show()'''
'''import matplotlib.pyplot as plt#直方图
from matplotlib import rcParams
rcParams["font.family"]="SimHei"
plt.figure(figsize=(10,10))
scores=[85,92,78,88]
plt.hist(scores,bins=4,color="blue",linewidth=0.2)#数据,区间
plt.axis("off")#不显示坐标轴
plt.show()'''
'''import matplotlib.pyplot as plt#多个图绘制在一张图
month=["1","2","3","4"]
sales=[100,150,80,130]
f1=plt.subplot(221)#行,列,图表计数
f1.plot(month,sales)
f2=plt.subplot(222)
f2.bar(month,sales)
f3=plt.subplot(223)
f3.barh(month,sales)
f4=plt.subplot(224)
f4.scatter(month,sales)
plt.show()'''