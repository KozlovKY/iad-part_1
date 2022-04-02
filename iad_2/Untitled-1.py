import glob
import pandas as pd
import numpy as np
file_list = glob.glob('Data'+ "/*.csv")
df_00, df_01 = pd.DataFrame(pd.read_csv(file_list[0])), pd.DataFrame(pd.read_csv(file_list[1]))
main_df = pd.merge(df_00,df_01, on ='index')
for i in range(2,len(file_list)-1,2):
   df1, df2 = pd.DataFrame(pd.read_csv(file_list[i])), pd.DataFrame(pd.read_csv(file_list[i+1]))
   side_df = pd.merge(df1,df2, on ='index')
   main_df = pd.concat([main_df, side_df])
df = main_df.sort_values(by="index")


df = df.rename(columns={"parental level of education":"education","test preparation course":"test preparation"})
azbuka = ['A', 'B', 'C', 'D','E'] # cпособ не оч хороший, но суть задания в циклах, в любом случае, если групп будет больше я смогу достать все группы с помощью unique
for j in range(len(azbuka)):
    a = np.array(df[df["race/ethnicity"] == ('group ' + azbuka[j])]["reading score"])
    sum = 0
    for i in range(0,len(a)):
        sum += a[i]
    print('group', azbuka[j], sum/len(a))


educat = df["education"].unique()
for j in range(len(educat)-1):
    b = np.array(df[df["education"] == educat[j]]["writing score"])
    for i in range(len(b)-1):
        for k in range(len(b)-i-1):
            if b[k] >= b[k+1]:
                t = b[k]
                b[k] = b[k+1]
                b[k+1] = t
    print(educat[j], ':', b[0])
    